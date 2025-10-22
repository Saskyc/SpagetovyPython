import time
from datetime import datetime

def GetDefined():
    myTuples = \
        [
            ("a", 1),
            ("b", 2),
            ("c", 3),
            ("d", 4),
            ("e", 5),
            ("f", 6),
            ("g", 7),
            ("h", 8),
            ("i", 9),
            ("j", 10),
            ("k", 11),
            ("l", 12),
            ("m", 13),
            ("n", 14),
            ("o", 15),
            ("p", 16),
            ("q", 17),
            ("r", 18),
            ("s", 19),
            ("t", 20),
            ("u", 21),
            ("v", 22),
            ("w", 23),
            ("x", 24),
            ("y", 25),
            ("z", 26),
        ]
    return myTuples

def GetNumberByLetter(letterArgument):
    for tuple in GetDefined():
        letter = tuple[0]
        number = int(tuple[1])

        if letter == letterArgument:
            return number
    return None


def GetLetterByNumber(numberArgument):
    for tuple in GetDefined():
        letter = tuple[0]
        number = int(tuple[1])

        if number == numberArgument:
            return letter
    return None


"""
Can't be used to lower index by more then 20.
"""
def NumberLowerBy(number, lowerIndex):
    for i in range(lowerIndex):
        number -= 1
        number = GetEqualInIndexes(number)

    return number

def NumberAppendBy(number, appendIndex):
    for i in range(appendIndex):
        number += 1
        number = GetEqualInIndexes(number)
    return number

def GetEqualInIndexes(number):
    inIndex = number % GetDefined().__len__()

def GetOpposite(number):
    return (number - number) - number

def Encode(sentence, posun):
    sentence = str(sentence).lower()

    sentenceParsed = ""

    for letter in sentence:

        if(letter == " "):
            sentenceParsed += " "
            continue

        number = GetNumberByLetter(letter)
        number = NumberLowerBy(number, int(posun))
        letter = GetLetterByNumber(number)
        sentenceParsed += str(letter)

    return sentenceParsed

def Decode(sentence, posun):
    sentence = str(sentence).lower()

    sentenceParsed = ""

    for letter in sentence:

        if (letter == " "):
            sentenceParsed += " "
            continue

        number = GetNumberByLetter(letter)
        number = NumberLowerBy(number, int(posun))
        letter = GetLetterByNumber(number)
        sentenceParsed += letter
    return sentenceParsed


startingTime = datetime.now()



"""
CODE (DOLU)
"""

print("\n-------------\n")

print(100 % 26)

print("[Test 0.1]")
print(GetLetterByNumber(5))

print("[Test 0.2]")
print(GetNumberByLetter("e"))

print("[Test 1] Now should print: 26")
print(NumberLowerBy(1, 1))

print("[Test 2] Now should print: 4")
print((-4 - -4) - -4)

print("[Test 3] Now should print: 18")
print(GetOpposite(-18))

print("[Test 4] Now should print: -18")
print(GetOpposite(18))

print("[Test 5] Now should print: 25")
print(GetEqualInIndexes(-1))

print("[Test 6] Now should print: 1")
print(GetEqualInIndexes(27))

print("[Test 7] Now should print: 18")
print(NumberAppendBy(199, 1))

print("[Test 8] Now should print: izqzm bjiiv bdqz tjp pk izqzm bjiiv gzo tjp yjri")
encoded = Encode("Never gonna give you up never gonna let you down", 5)
print(encoded)

print("[Test 9] Now should print: never gonna give you up never gonna let you down")
print(Decode(encoded, 5))

print("[Test 10] Now should print: 1")
print(GetNumberByLetter("a"))

print("[Test 11] Now should print: 2")
print(GetNumberByLetter("b"))

print("[Test 12] Now should print: 3")
print(GetNumberByLetter("c"))

print("[Test 13] Now should print: 24")
print(GetNumberByLetter("x"))

print("[Test 14] Now should print: a")
print(GetLetterByNumber(1))

print("[Test 15] Now should print: f")
print(GetLetterByNumber(5))

print("[Test 16] Now should print: j")
print(GetLetterByNumber(10))

print("[Test 17] Now should print: le epic epic le omg")
print(Decode("qj junh junh qj trl", 5))

while True:
    fraze, mode, posun = input("Vlož frázi: ").lower(), input("E/D: "), input("Posun: ")

    try:
        posun = int(posun)
    except:
        print(" Posun nebylo číslo.")
        continue

    if(mode == "e"):
        print(Encode(fraze, posun))
        break
    elif(mode == "d"):
        print(Decode(fraze, posun))
        break
    else:
        print(" Špatně zadaný mód")
        continue

"""
CODE (NAHORU)
"""














print("\n-------------\n")
endingTime = datetime.now()

elapsed = endingTime - startingTime

print(f"Time elapsed in seconds: {elapsed.total_seconds()}")

print("\n-------------\n")