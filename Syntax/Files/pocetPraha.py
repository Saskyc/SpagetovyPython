praha = 0
with open("praha.txt", "r", encoding="utf-8") as f:
    for radek in f:
        for slovo in radek.split():
            if slovo.lower() == "praha":
                praha += 1
print(f"clanek ma napsany praha {praha}x")