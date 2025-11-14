while True:
    mode = input("Mode: ")

    if mode == "exit":
        break

    while True:
        try:
            cisla = (int(input("Zadej první číslo: ")), int(input("Zadej druhé číslo: ")))
        except:
            continue
        break

    if mode == "plus":
        print(cisla[0] + cisla[1])
        break
    elif mode == "minus":
        print(cisla[0] - cisla[1])
        break
    elif mode == "multiply":
        print(cisla[0] * cisla[1])
        break
    elif mode == "devide":
        print(cisla[0] / cisla[1])
        break
    elif mode == "power":
        print(cisla[0] ** cisla[1])
        break
    elif mode == "root":
        print(cisla[0] ** (1 / cisla[1]))
        break