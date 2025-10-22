text = input("Zadej frázi k zašifrování/dešifrování: ")
klic = input("Zadej klíč: ")
operace = input("1 - zašifrovat / 2 - rozšifrovat? ")
c = ""

while len(klic) < len(text):
    klic += klic

if operace == "1":
    for i in range(len(text)): #Opeakuje přes každý písmeno
        c += chr(ord(text[i])-50+ord(klic[i]))
    print("Zašifrováno: ", c)

if operace == "2":
    for i in range(len(text)): #Opeakuje přes každý písmeno
        c += chr(ord(text[i]) + 50 - ord(klic[i]))
    print("Rozšifrováno: ", c)