while True:
    myInput = input("Zadej číslo: ")
    try:
        myInput = int(myInput)
    except:
        continue
    break

if(myInput == 5):
    print("Hodnota je 5")
elif (myInput > 5):
    print("Hodnota je větší než 5")
else:
    print("Hodnota je menší než 5")