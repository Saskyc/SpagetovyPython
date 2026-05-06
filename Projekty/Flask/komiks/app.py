from flask import Flask, render_template, abort

app = Flask(__name__)

# Data komiksu – každá strana má číslo, název a panely
STRANKY = [
    {
        "cislo": 1,
        "nazev": "Začátek dobrodružství",
        "panely": [
            {
                "text_bublina": "Musím najít ten poklad!",
                "popis": "Hrdina stojí před tajemnou mapou.",
                "pozice": "vlevo nahoře",
                "efekt": "BOOM!",
            },
            {
                "text_bublina": "Mapa říká... jít na sever.",
                "popis": "Hrdina se dívá do kompasu.",
                "pozice": "vpravo nahoře",
                "efekt": None,
            },
            {
                "text_bublina": "Ale tam je les plný nebezpečí!",
                "popis": "Temný les se rýsuje v pozadí.",
                "pozice": "vlevo dole",
                "efekt": "AAAH!",
            },
            {
                "text_bublina": "Nevadí. Jsem připraven!",
                "popis": "Hrdina vytasí meč a vyráží.",
                "pozice": "vpravo dole",
                "efekt": "WHOOSH!",
            },
        ],
    },
    {
        "cislo": 2,
        "nazev": "V temném lese",
        "panely": [
            {
                "text_bublina": "Co to bylo za zvuk?!",
                "popis": "Prasknutí větve v temnotě.",
                "pozice": "vlevo nahoře",
                "efekt": "CRACK!",
            },
            {
                "text_bublina": "Jen liška. Fúúú.",
                "popis": "Malá liška vyběhne z keřů.",
                "pozice": "vpravo nahoře",
                "efekt": None,
            },
            {
                "text_bublina": "Počkej... vidím světlo!",
                "popis": "Zlaté světlo problikává mezi stromy.",
                "pozice": "střed",
                "efekt": "✨",
            },
            {
                "text_bublina": "To musí být jeskyně pokladu!",
                "popis": "Hrdina běží k záři.",
                "pozice": "vpravo dole",
                "efekt": "ZAP!",
            },
        ],
    },
    {
        "cislo": 3,
        "nazev": "Poklad nalezen!",
        "panely": [
            {
                "text_bublina": "Nevěřím vlastním očím!",
                "popis": "Obrovská truhla plná zlata.",
                "pozice": "vlevo nahoře",
                "efekt": "WOW!",
            },
            {
                "text_bublina": "Ale... není to past?",
                "popis": "Hrdina si všimne podezřelých drátů.",
                "pozice": "vpravo nahoře",
                "efekt": "?!",
            },
            {
                "text_bublina": "Opatrně...",
                "popis": "Ruka pomalu sahá pro poklad.",
                "pozice": "vlevo dole",
                "efekt": None,
            },
            {
                "text_bublina": "DOBYL JSEM TĚ, POKLADE!",
                "popis": "Hrdina triumfálně zdvihá truhlu.",
                "pozice": "vpravo dole",
                "efekt": "VICTORY!",
            },
        ],
    },
]


@app.route("/")
def index():
    return render_template("index.html", stranky=STRANKY)


@app.route("/strana/<int:cislo>")
def strana(cislo):
    # Najdi stranu podle čísla
    aktualni = next((s for s in STRANKY if s["cislo"] == cislo), None)
    if aktualni is None:
        abort(404)

    predchozi = cislo - 1 if cislo > 1 else None
    nasledujici = cislo + 1 if cislo < len(STRANKY) else None

    return render_template(
        "strana.html",
        strana=aktualni,
        predchozi=predchozi,
        nasledujici=nasledujici,
        celkem=len(STRANKY),
    )


if __name__ == "__main__":
    app.run(debug=True)