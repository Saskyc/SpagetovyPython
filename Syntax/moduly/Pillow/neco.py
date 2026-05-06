from PIL import Image, ImageDraw

def draw_square(draw, x, y, size, fill="white", outline="black", width=1):
    """
    Nakreslí čtverec.
    (x, y) = levý horní roh
    size = délka strany
    """
    draw.rectangle(
        [x, y, x + size, y + size],
        fill=fill,
        outline=outline,
        width=width
    )


def draw_rectangle(draw, x, y, w, h, fill="white", outline="black", width=1):
    """
    Obdélník (hodí se na tělo domu apod.)
    """
    draw.rectangle(
        [x, y, x + w, y + h],
        fill=fill,
        outline=outline,
        width=width
    )


def draw_triangle(draw, points, fill="white", outline="black", width=1):
    """
    Trojúhelník podle 3 bodů:
    points = [(x1,y1), (x2,y2), (x3,y3)]
    """
    draw.polygon(
        points,
        fill=fill,
        outline=outline
    )


def draw_line(draw, x1, y1, x2, y2, fill="black", width=1):
    """
    Čára mezi dvěma body
    """
    draw.line(
        [x1, y1, x2, y2],
        fill=fill,
        width=width
    )

img = Image.new("RGB", (300, 300), "white")
draw = ImageDraw.Draw(img)

draw_rectangle(draw, 0, 0, 1200, 1200, fill="lightblue", outline="white", width=2)
draw_rectangle(draw, 0, 200, 1200, 100, fill="lightgreen", outline="lightblue", width=2)
draw_rectangle(draw, 20, 20, 50, 50, fill="yellow", outline="lightblue", width=2)

house_y = 20;

# dům (tělo)
draw_rectangle(draw, 100, 150 + house_y, 100, 100, fill="lightyellow", outline="black", width=2)

# střecha
draw_triangle(draw, [(100, 150 + house_y), (200, 150 + house_y), (150, 80 + house_y)], fill="brown", outline="black")

# okno
draw_square(draw, 115, 165 + house_y, 20, fill="yellow", outline="black")
draw_square(draw, 165, 165 + house_y, 20, fill="yellow", outline="black")

# dveře
draw_rectangle(draw, 135, 200 + house_y, 30, 50, fill="darkred", outline="black")

img.save("image.png") 