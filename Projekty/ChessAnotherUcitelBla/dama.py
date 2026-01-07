
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dáma online pro dva hráče (GUI: Pygame, síť: TCP sockets)
Autor: M365 Copilot – připraveno pro Frantu Nováka a Pepu Svobodu :-)
Pravidla: anglická dáma (8x8), povinné braní, vícenásobné braní, král oběma směry.
"""

import sys
import json
import socket
import threading
import argparse
from queue import Queue
import time

# --- Grafika (pygame) ---
try:
    import pygame
except Exception as e:
    print("Chybí Pygame. Nainstaluj: pip install pygame (nebo sudo apt-get install python3-pygame)")
    raise

# ----------------- Konstanta a barvy -----------------
BOARD_SIZE = 8
TILE_SIZE = 80
MARGIN = 40
WINDOW_W = BOARD_SIZE * TILE_SIZE
WINDOW_H = BOARD_SIZE * TILE_SIZE + 80  # místo pro stavový řádek

COLOR_BG = (26, 26, 26)
COLOR_LIGHT = (235, 235, 208)
COLOR_DARK = (119, 148, 85)
COLOR_WHITE_PIECE = (245, 245, 245)
COLOR_BLACK_PIECE = (30, 30, 30)
COLOR_HL = (255, 215, 0)  # zvýraznění (zlatá)
COLOR_VALID = (66, 135, 245)  # platný tah
COLOR_TEXT = (240, 240, 240)
COLOR_NAME_WHITE = (210, 210, 255)
COLOR_NAME_BLACK = (255, 210, 210)

FPS = 60

# ----------------- Model -----------------
class Piece:
    def __init__(self, color: str, king: bool = False):
        self.color = color  # "white" nebo "black"
        self.king = king

    def copy(self):
        return Piece(self.color, self.king)

def create_initial_board():
    """Vytvoří počáteční rozestavení: černé nahoře, bílé dole."""
    board = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    # Černé (nahoře) na prvních 3 řadách
    for r in range(3):
        for c in range(BOARD_SIZE):
            if (r + c) % 2 == 1:
                board[r][c] = Piece("black")
    # Bílé (dole) na posledních 3 řadách
    for r in range(BOARD_SIZE - 3, BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if (r + c) % 2 == 1:
                board[r][c] = Piece("white")
    return board

def serialize_board(board):
    return [
        [
            None if board[r][c] is None else {"color": board[r][c].color, "king": board[r][c].king}
            for c in range(BOARD_SIZE)
        ]
        for r in range(BOARD_SIZE)
    ]

def deserialize_board(data):
    board = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            cell = data[r][c]
            if cell is not None:
                board[r][c] = Piece(cell["color"], cell["king"])
    return board

def in_bounds(r, c):
    return 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE

def has_any_capture(board, color):
    """Zjistí, zda aktuální hráč má k dispozici nějaké braní (povinné braní)."""
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            p = board[r][c]
            if p and p.color == color:
                moves = get_moves_for_piece(board, r, c, must_capture_only=True)
                if moves:
                    return True
    return False

def get_moves_for_piece(board, r, c, must_capture_only=False, force_piece_pos=None):
    """
    Vrátí slovník { (dr,dc): {"captures":[(r1,c1),...], "is_jump":True/False } } pro daný kámen.
    - Pravidla: anglická dáma (pěšák bere jen dopředu; král oběma směry).
    - must_capture_only=True vynutí pouze braní.
    - force_piece_pos: je-li zadáno (r,c), povolí tahy pouze z této pozice (vícenásobné braní).
    """
    p = board[r][c]
    if not p:
        return {}

    # Pokud pokračujeme ve vícenásobném braní, dovol jen tento kámen
    if force_piece_pos is not None and (r, c) != force_piece_pos:
        return {}

    moves = {}
    directions = []
    if p.king:
        directions = [(-1, -1), (-1, +1), (+1, -1), (+1, +1)]
    else:
        # Pěšák: bílý dopředu (r-1), černý dopředu (r+1)
        if p.color == "white":
            directions = [(-1, -1), (-1, +1)]
        else:
            directions = [(+1, -1), (+1, +1)]

    # Jednokrokové tahy (pokud není vynucené braní)
    if not must_capture_only:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc) and board[nr][nc] is None:
                moves[(nr, nc)] = {"captures": [], "is_jump": False}

    # Skoky (braní)
    for dr, dc in [(-1, -1), (-1, +1), (+1, -1), (+1, +1)] if p.king else directions:
        mr, mc = r + dr, c + dc
        jr, jc = r + 2 * dr, c + 2 * dc
        if in_bounds(jr, jc) and in_bounds(mr, mc):
            mid = board[mr][mc]
            if mid is not None and mid.color != p.color and board[jr][jc] is None:
                moves[(jr, jc)] = {"captures": [(mr, mc)], "is_jump": True}

    # Pokud existuje aspoň jeden skok, vynutíme skoky (povinné braní)
    has_jump = any(info["is_jump"] for info in moves.values())
    if has_jump:
        moves = {dst: info for dst, info in moves.items() if info["is_jump"]}
    elif must_capture_only:
        return {}

    return moves

def promote_if_needed(board, r, piece):
    """Povýší na krále, pokud dojde na poslední řadu."""
    if piece.king:
        return
    if piece.color == "white" and r == 0:
        piece.king = True
    elif piece.color == "black" and r == BOARD_SIZE - 1:
        piece.king = True

# ----------------- Síťová vrstva -----------------
class NetEndpoint:
    """
    Jednoduchý TCP „host-klient“. Posílá JSON zprávy ukončené \n.
    Typy zpráv:
      - SYNC: počáteční synchronizace (stav desky, tah, jména, barvy)
      - MOVE: tah {"src":[r,c],"dst":[r,c],"captures":[[r,c],...]}
      - CHAT: textový vzkaz (nepovinné)
    """
    def __init__(self, mode, host, port, on_message):
        self.mode = mode
        self.host = host
        self.port = port
        self.on_message = on_message
        self.sock = None
        self.reader = None
        self.write_lock = threading.Lock()
        self.running = False
        self.thread = None

    def start(self):
        if self.mode == "host":
            srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            srv.bind(("0.0.0.0", self.port))
            srv.listen(1)
            print(f"[NET] Čekám na klienta na portu {self.port}...")
            conn, addr = srv.accept()
            print(f"[NET] Klient připojen z {addr}")
            self.sock = conn
        else:
            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(f"[NET] Připojuji se na {self.host}:{self.port} ...")
            conn.connect((self.host, self.port))
            print("[NET] Připojeno.")
            self.sock = conn

        self.reader = self.sock.makefile("r", encoding="utf-8", newline="\n")
        self.running = True
        self.thread = threading.Thread(target=self._recv_loop, daemon=True)
        self.thread.start()

    def _recv_loop(self):
        try:
            while self.running:
                line = self.reader.readline()
                if not line:
                    print("[NET] Odpojeno.")
                    self.running = False
                    break
                try:
                    msg = json.loads(line.strip())
                    self.on_message(msg)
                except Exception as e:
                    print("[NET] Chybná zpráva:", e)
        except Exception as e:
            print("[NET] Chyba příjmu:", e)
        finally:
            self.running = False

    def send(self, msg: dict):
        if not self.sock:
            return
        data = json.dumps(msg, ensure_ascii=False) + "\n"
        with self.write_lock:
            try:
                self.sock.sendall(data.encode("utf-8"))
            except Exception as e:
                print("[NET] Chyba při odesílání:", e)
                self.running = False

    def close(self):
        self.running = False
        try:
            if self.reader:
                self.reader.close()
        except:
            pass
        try:
            if self.sock:
                self.sock.close()
        except:
            pass

# ----------------- Hra -----------------
class Game:
    def __init__(self, mode, host, port, my_name):
        self.mode = mode
        self.host = host
        self.port = port
        self.my_name = my_name or ("Franta Novák" if mode == "host" else "Pepa Svoboda")

        # Stav hry
        self.board = create_initial_board()
        self.turn = "white"  # bílý začíná
        self.my_color = "white" if mode == "host" else "black"
        self.opponent_name = "Neznámý"
        self.must_continue_from = None  # pozice (r,c), pokud probíhá vícenásobné braní tímto kamenem
        self.selected = None
        self.valid_moves = {}

        # Síť
        self.incoming = Queue()
        self.net = NetEndpoint(mode, host, port, self._on_net_message)
        self.net.start()

        # Výměna SYNC informací
        initial_state = {
            "board": serialize_board(self.board),
            "turn": self.turn,
            "players": {
                "white": self.my_name if self.my_color == "white" else None,
                "black": self.my_name if self.my_color == "black" else None,
            }
        }
        # Host pošle SYNC hned, klient počká a po obdržení doplní jména
        if self.mode == "host":
            self.net.send({"type": "SYNC", "state": initial_state})
        else:
            # klient počká na SYNC, poté pošle svoje jméno
            pass

    # -------- Síťové zprávy zpracování --------
    def _on_net_message(self, msg):
        self.incoming.put(msg)

    def process_incoming(self):
        while not self.incoming.empty():
            msg = self.incoming.get()
            t = msg.get("type")
            if t == "SYNC":
                state = msg.get("state", {})
                self.board = deserialize_board(state["board"])
                self.turn = state["turn"]
                players = state.get("players", {})
                # doplnění jmen
                if players.get("white"):
                    if self.my_color == "black":
                        self.opponent_name = players["white"]
                if players.get("black"):
                    if self.my_color == "white":
                        self.opponent_name = players["black"]
                # po SYNC klient pošle své jméno
                if self.mode == "client":
                    my_players = {
                        "white": self.my_name if self.my_color == "white" else None,
                        "black": self.my_name if self.my_color == "black" else None,
                    }
                    self.net.send({"type": "SYNC", "state": {
                        "board": serialize_board(self.board),
                        "turn": self.turn,
                        "players": my_players
                    }})
            elif t == "MOVE":
                mv = msg.get("move", {})
                self.apply_remote_move(mv)
            elif t == "CHAT":
                # případně zobrazit v UI
                print("[CHAT]", msg.get("text"))
            else:
                print("[NET] Neznámý typ zprávy:", t)

    # -------- Herní logika --------
    def is_my_turn(self):
        return self.turn == self.my_color

    def click_on(self, r, c):
        """Zpracování kliknutí uživatele."""
        if not self.is_my_turn():
            return
        # Pokud probíhá vícenásobné braní, dovol jen ten vybraný kámen
        force_pos = self.must_continue_from

        p = self.board[r][c]
        if p and p.color == self.my_color:
            # výběr/změna výběru
            self.selected = (r, c)
            must_capture = has_any_capture(self.board, self.my_color)
            self.valid_moves = get_moves_for_piece(self.board, r, c,
                                                   must_capture_only=must_capture,
                                                   force_piece_pos=force_pos)
        elif self.selected and (r, c) in self.valid_moves:
            # pokus o tah na platný cíl
            self.perform_move(self.selected, (r, c), self.valid_moves[(r, c)])
            self.selected = None
            self.valid_moves = {}

    def perform_move(self, src, dst, info):
        """Lokální tah hráče + odeslání přes síť."""
        sr, sc = src
        dr, dc = dst
        piece = self.board[sr][sc]
        captures = info["captures"]

        # Přesun
        self.board[sr][sc] = None
        self.board[dr][dc] = piece

        # Odebrání braných kamenů
        for (cr, cc) in captures:
            self.board[cr][cc] = None

        # Povýšení na krále (pokud došel na konec)
        promote_if_needed(self.board, dr, piece)

        # Odeslat tah
        self.net.send({"type": "MOVE", "move": {
            "src": [sr, sc],
            "dst": [dr, dc],
            "captures": captures
        }})

        # Vícenásobné braní?
        continued = False
        if captures:
            must_capture_more = get_moves_for_piece(self.board, dr, dc,
                                                    must_capture_only=True,
                                                    force_piece_pos=(dr, dc))
            if must_capture_more:
                # Musí pokračovat stejným kamenem
                self.must_continue_from = (dr, dc)
                self.selected = (dr, dc)
                self.valid_moves = must_capture_more
                continued = True
            else:
                self.must_continue_from = None

        # Pokud se nepokračuje, střídá se tah
        if not continued:
            self.turn = "white" if self.turn == "black" else "black"

    def apply_remote_move(self, mv):
        """Aplikuje tah protivníka (přijatý ze sítě)."""
        sr, sc = mv["src"]
        dr, dc = mv["dst"]
        captures = mv.get("captures", [])
        piece = self.board[sr][sc]
        self.board[sr][sc] = None
        self.board[dr][dc] = piece
        for (cr, cc) in captures:
            self.board[cr][cc] = None
        promote_if_needed(self.board, dr, piece)

        # Zjisti, zda protivník musí pokračovat (vícenásobné braní)
        # Pokud ano, tah se NEMĚNÍ (protivník stále na tahu).
        continued = False
        if captures:
            more = get_moves_for_piece(self.board, dr, dc,
                                       must_capture_only=True,
                                       force_piece_pos=(dr, dc))
            if more:
                continued = True

        if not continued:
            self.turn = "white" if self.turn == "black" else "black"

    def game_over_state(self):
        """Zjistí konec hry (nemá tahy / bez kamenů)."""
        # pokud aktuální hráč nemá žádný tah, prohrává
        current = self.turn
        any_piece = False
        any_move = False
        must_cap = has_any_capture(self.board, current)
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                p = self.board[r][c]
                if p and p.color == current:
                    any_piece = True
                    moves = get_moves_for_piece(self.board, r, c,
                                                must_capture_only=must_cap,
                                                force_piece_pos=self.must_continue_from)
                    if moves:
                        any_move = True
                        break
            if any_move:
                break
        if not any_piece or not any_move:
            # druhý vyhrává
            winner = "white" if current == "black" else "black"
            return winner
        return None

# ----------------- UI vykreslování -----------------
def draw_board(screen, font, game: Game):
    screen.fill(COLOR_BG)

    # Deska
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            rect = pygame.Rect(c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            col = COLOR_LIGHT if (r + c) % 2 == 0 else COLOR_DARK
            pygame.draw.rect(screen, col, rect)

    # Zvýraznění výběru
    if game.selected:
        sr, sc = game.selected
        rect = pygame.Rect(sc * TILE_SIZE, sr * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, COLOR_HL, rect, 4)

    # Platné tahy
    for (dr, dc), info in game.valid_moves.items():
        cx = dc * TILE_SIZE + TILE_SIZE // 2
        cy = dr * TILE_SIZE + TILE_SIZE // 2
        pygame.draw.circle(screen, COLOR_VALID, (cx, cy), 12)

    # Kameny
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            p = game.board[r][c]
            if p:
                cx = c * TILE_SIZE + TILE_SIZE // 2
                cy = r * TILE_SIZE + TILE_SIZE // 2
                color = COLOR_WHITE_PIECE if p.color == "white" else COLOR_BLACK_PIECE
                pygame.draw.circle(screen, color, (cx, cy), TILE_SIZE // 2 - 8)
                # Král – kroužek navíc
                if p.king:
                    pygame.draw.circle(screen, (255, 215, 0), (cx, cy), TILE_SIZE // 2 - 20, 4)

    # Stavový panel
    bar_rect = pygame.Rect(0, BOARD_SIZE * TILE_SIZE, WINDOW_W, WINDOW_H - BOARD_SIZE * TILE_SIZE)
    pygame.draw.rect(screen, COLOR_BG, bar_rect)

    turn_text = f"Na tahu: {'Bílý' if game.turn == 'white' else 'Černý'}"
    you_text = f"Ty: {game.my_name} ({'Bílý' if game.my_color == 'white' else 'Černý'})"
    opp_text = f"Soupeř: {game.opponent_name}"

    t_surf = font.render(turn_text, True, COLOR_TEXT)
    y_surf = font.render(you_text, True, COLOR_NAME_WHITE if game.my_color == "white" else COLOR_NAME_BLACK)
    o_surf = font.render(opp_text, True, COLOR_NAME_BLACK if game.my_color == "white" else COLOR_NAME_WHITE)

    screen.blit(t_surf, (10, BOARD_SIZE * TILE_SIZE + 10))
    screen.blit(y_surf, (10, BOARD_SIZE * TILE_SIZE + 40))
    screen.blit(o_surf, (10, BOARD_SIZE * TILE_SIZE + 70))

    # Konec hry?
    winner = game.game_over_state()
    if winner:
        msg = f"Konec hry! {'Bílý' if winner == 'white' else 'Černý'} vítězí."
        end_surf = font.render(msg, True, (255, 100, 100))
        screen.blit(end_surf, (WINDOW_W - end_surf.get_width() - 10, BOARD_SIZE * TILE_SIZE + 40))

def pos_from_mouse(mx, my):
    r = my // TILE_SIZE
    c = mx // TILE_SIZE
    if r < 0 or r >= BOARD_SIZE or c < 0 or c >= BOARD_SIZE:
        return None
    return (r, c)

# ----------------- Hlavní smyčka -----------------
def main():
    parser = argparse.ArgumentParser(description="Dáma online pro dva (Pygame + TCP)")
    parser.add_argument("--mode", choices=["host", "client"], required=True, help="host = bílý, client = černý")
    parser.add_argument("--host", help="IP adresa hostitele (pro klienta)")
    parser.add_argument("--port", type=int, default=50007, help="TCP port (výchozí 50007)")
    parser.add_argument("--name", type=str, default=None, help="Tvé jméno (zobrazí se v UI)")
    args = parser.parse_args()

    if args.mode == "client" and not args.host:
        print("Pro klienta je nutné zadat --host <IP>")
        sys.exit(1)

    pygame.init()
    screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
    pygame.display.set_caption("Dáma online (Pygame)")
    font = pygame.font.SysFont(None, 28)
    clock = pygame.time.Clock()

    game = Game(args.mode, args.host, args.port, args.name)

    running = True
    while running:
        clock.tick(FPS)

        # Síťové zprávy
        game.process_incoming()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pos_from_mouse(*event.pos)
                if pos:
                    r, c = pos
                    game.click_on(r, c)

        draw_board(screen, font, game)
        pygame.display.flip()

    game.net.close()
    pygame.quit()

if __name__ == "__main__":
    main()
