import sys


def fibonachiSingle(num1, num2):
    num3 = num1+num2
    return (num2, num3)

x = 0
y = 1

index = 0

maxFibonachi = 4000000
sys.set_int_max_str_digits(999999)
while True:
    if index == 0:
        if maxFibonachi == 0:
            print(f"F0 = 0")
            break

        index += 1
        continue

    if index == 2:
        if maxFibonachi == 2:
            print(f"F2 = 1")
            break
        index += 1
        continue

    z = fibonachiSingle(x, y)
    x = z[0]
    y = z[1]

    if maxFibonachi <= index:
        print(f"F{index} = {z[1]}")
        break
    else:
        index += 1