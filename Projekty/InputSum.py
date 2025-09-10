from Library.MyMath import *
from Library.color import *

wrongOperation = True
operation = ""

while wrongOperation:
    print(Color.Intensity.High.Purple + "Operations:\n"
          "- Sum\n"
          "- Minus\n"
          "- Deleni\n"
          "- Multiplication\n"
          "- Power\n"
          "- Root\n")

    operation = input(Color.Regular.Cyan + "Enter your choice: ").lower()
    if operation == "sum" or operation == "minus" or operation == "deleni" or operation == "multiplication" or operation == "power" or operation == "root":
        break
    print(Color.Regular.Red + "Wrong operation")
exceptionVar = True

while exceptionVar:


    firstInput = input(Color.Regular.Cyan + "Enter first number: " + Color.Bold.Yellow)
    secondInput = input(Color.Regular.Cyan + "Enter second number: " + Color.Bold.Yellow)
    try:
        if operation == "sum":
            print(MyMath.Sum(int(firstInput), int(secondInput)))
            break
        elif operation == "minus":
            print(MyMath.Minus(int(firstInput), int(secondInput)))
            break
        elif operation == "deleni":
            print(MyMath.Deleni(int(firstInput), int(secondInput)))
            break
        elif operation == "multiplication":
            print(MyMath.Multiplication(int(firstInput), int(secondInput)))
            break
        elif operation == "power":
            print(MyMath.Power(int(firstInput), int(secondInput)))
            break
        elif operation == "root":
            print(MyMath.Root(int(firstInput), int(secondInput)))
            break
        else:
            print(Color.Bold.Red + "Jak jsi pojebal můj program?")
    except:
        exceptionVar = True
        print(Color.Regular.Red + "I was casted wrong :(")
        continue
    excpetionVar = False
