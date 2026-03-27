from pathlib import Path
from datetime import datetime
from datetime import time
import random
import os

_DAYNAMES = [None, "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

datum = datetime.now().date()


hodina = time.hour


cisloDne = datum.toordinal() % 7 or 7
nazev = _DAYNAMES[cisloDne]

cestaLog = Path("logy") / "zalohalogu" / f"{nazev}.txt"
cesta = Path("logy") / "mojepc" / f"{nazev}.txt"

if cesta.exists():
    if not cestaLog.exists():
        cestaLog.parent.mkdir(parents=True, exist_ok=True)  # ensure folders exist

    with open(cesta, "r", encoding="utf-8") as f:
        obsah = f.read()
        with open(cestaLog, "a", encoding="utf-8") as logF:
            logF.write(obsah)
    os.remove(cesta)