# HeroQuest Komiks – Flask aplikace

## Struktura projektu

```
komiks/
├── app.py                  # Hlavní Flask aplikace
├── requirements.txt
├── templates/
│   ├── base.html           # Základní layout (header, footer)
│   ├── index.html          # Úvodní strana s přehledem
│   └── strana.html         # Šablona jedné strany komiksu
└── static/
    ├── css/style.css       # Styly
    └── js/main.js          # Klávesová navigace + animace
```

## Spuštění

```bash
pip install -r requirements.txt
python app.py
```

Otevři prohlížeč na `http://127.0.0.1:5000`

## Navigace

- **Šipky ← →** nebo klávesy **A / D** – přechod mezi stranami
- Kliknutí na čísla v headeru – přímý skok na stranu

## Jak přidat novou stranu

V `app.py` přidej do seznamu `STRANKY` nový slovník:

```python
{
    "cislo": 4,
    "nazev": "Název strany",
    "panely": [
        {
            "text_bublina": "Co postava říká",
            "popis": "Co se děje v panelu",
            "pozice": "vlevo nahoře",
            "efekt": "POW!",   # nebo None
        },
        # ... další panely
    ],
}
```

## Jak přidat obrázky do panelů

V `templates/strana.html` nahraď `<div class="panel-obrazek">` za:

```html
<div class="panel-obrazek">
    <img src="{{ url_for('static', filename='img/strana' + strana.cislo|string + '_panel' + loop.index|string + '.png') }}"
         alt="{{ p.popis }}">
</div>
```
