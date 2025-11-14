for p in range(1000):
    print(p, ":", chr(p))

def getBin():
    myIndex = 10

    binDict = {}

    for i in range(65, 91):
        binDict[myIndex] = chr(i)
        myIndex += 1

    return binDict

def convertDecimal(number, to):
    binary = getBin()

    list = []

    while number != 0:
        zbytek = number % to

        if zbytek >= 10:
            list.insert(0, binary[zbytek])
        else:
            list.insert(0, zbytek)
        number = number // to

    vys = ""
    for y in list:
        vys = vys + str(y)

    return vys

x = 1

while True:
    try:
        x = int(input("Vypiš číslo v 10 tkové soustavě: "))
    except:
        print("Něco je špatně")
        continue
    break

print("Binary:", convertDecimal(x, 2))
print("Octal:", convertDecimal(x, 8))
print("Hexadecimal:", convertDecimal(x, 16))