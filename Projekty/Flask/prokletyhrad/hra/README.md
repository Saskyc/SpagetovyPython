# ⚔️ Prokletý hrad – Flask Adventure Game

Textová dobrodružná hra běžící v prohlížeči. Prozkoumej 10 lokací, sbírej předměty, bojuj s nepřáteli a snaž se porazit Stínového Pána.

---

## O hře

Temné prokletí leží na kraji. Ve věži starého hradu spočívá **Kámen Světla** – jediný artefakt schopný prokletí zlomit. Tvým cílem je dostat se do hradu, zdolat Stínového Pána a přinést kámen zpět.

**Win condition:** Porazit Stínového Pána v Trůnním sále.
**Lose condition:** Životy hrdiny klesnou na 0.

---

## Instalace a spuštění

```bash
# 1. Naklonuj nebo rozbal projekt
cd hra/

# 2. Vytvoř virtuální prostředí (doporučeno)
python -m venv venv
venv\Scripts\activate      # Windows
# nebo
source venv/bin/activate   # Linux / macOS

# 3. Nainstaluj závislosti
pip install -r requirements.txt

# 4. Spusť hru
python app.py
# nebo
flask run

# 5. Otevři prohlížeč na
# http://127.0.0.1:5000
```

---

## Ovládání

| Akce | Popis |
|------|-------|
| Tlačítka směrů | Pohyb mezi lokacemi (Sever / Jih / Východ / Západ) |
| Sebrat | Sebrání předmětu z lokace |
| Inventář | Zobrazení a správa inventáře |
| Použít | Použití předmětu (lektvar, zbraň, brnění) |
| Zahodit | Vyhození předmětu |
| Útočit | Útok na nepřítele v souboji |
| Utéct | Pokus o útěk ze souboje (50 % šance) |

---

## Struktura projektu

```
hra/
├── app.py                ← Flask routes, session management
├── requirements.txt
├── README.md
├── game/
│   ├── __init__.py
│   ├── hrdina.py         ← třída Hrdina (životy, inventář, statistiky)
│   ├── mapa.py           ← třída Mapa, Lokace, načítání svet.json
│   ├── souboj.py         ← třída Nepritel, logika boje
│   └── inventar.py       ← třídy Predmet a Inventar
├── data/
│   └── svet.json         ← definice lokací, předmětů a nepřátel
├── templates/
│   ├── base.html         ← základní layout
│   ├── index.html        ← úvodní stránka (zadání jména)
│   ├── index_hra.html    ← hlavní herní obrazovka
│   ├── inventar.html     ← správa inventáře
│   ├── souboj.html       ← obrazovka souboje
│   └── konec.html        ← výhra / prohra
└── static/
    └── css/style.css     ← styly
```

---

## Mapa světa (10 lokací)

```
                  [Kamenné hory]
                 /      |
           [Les]   [Ruiny]
             |          |
         [Vesnice] [Přístav]

      [Hrad brána]   ← potřebuješ Zlatý klíč
           |
      [Hrad nádvoří]
     /      |        \
[Kaple] [Věž★]  [Zbrojnice]
```

★ = win condition

---

## Předměty

| Předmět | Typ | Efekt |
|---------|-----|-------|
| Lektvar života | lektvar | +30 životů |
| Lektvar síly | lektvar | +10 útok (dočasně) |
| Rezavý mečík | zbraň | +8 útok |
| Legendární meč | zbraň | +20 útok |
| Kožené brnění | brnění | +10 obrana |
| Zlatý klíč | klíčový | otvírá hradní bránu |
| Mapa hradu | klíčový | orientace v hradu |

---

## Nepřátelé

| Nepřítel | Životy | Útok | Odměna |
|----------|--------|------|--------|
| Divoký vlk | 30 | 8 | Lektvar života |
| Horský troll | 50 | 14 | – |
| Oživlý kostlivec | 25 | 10 | Lektvar síly |
| Prokletá stráž | 40 | 12 | – |
| Hradní rytíř | 55 | 16 | Lektvar života |
| Zbrojnický duch | 35 | 12 | – |
| **Stínový Pán** | **100** | **25** | **Výhra** |

---

## Použité knihovny

- **Flask** – webový framework
- **json** – načítání dat světa (stdlib)
- **random** – výpočty souboje (stdlib)
- **os** – cesty k souborům (stdlib)
