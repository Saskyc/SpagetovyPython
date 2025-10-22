fraze = input("Fráze: ")

searching = input("Jaké písmena hledáš? ")

found = ""
for i in range(len(fraze)):
    for j in range(len(searching)):
        if fraze[i] == searching[j]:
            founded = False
            for k in range(len(found)):
                if found[k] == searching[j]:
                    founded = True
            if founded == True:
                continue

            found += fraze[i]

print(f"Písmena ve frázi: {found}")