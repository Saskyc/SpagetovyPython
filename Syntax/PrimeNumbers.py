def IsNumber(n):
    try:
        int(n)
        return True
    except:
        return False

def IsEven(n):
    return n % 2 == 0

def IsPrime(n):
    print(f"Priming {n}")
    if IsNumber(n) is False:
        return False

    if n < 2:
        return False
    if n == 2:
        return True

    AllNumbers = []
    b = 2
    while True:

        AllNumbers.append(b)
        print(f" {b} >= {n} / 2")
        if b >= (n / 2)+1:
            break
        print(f"  B: {b}")
        b = b + 1

    for number in AllNumbers:
        print(f"  Checking {number}")
        print(f"  N: {IsEven(number / n) == True}")
        if IsEven(number / n) == True:
            return False

    return True


def GetPrimeNumberInRange(start, end):

    if IsNumber(start) == False or IsNumber(end) == False:
        return []

    start = int(start)
    end = int(end)

    if(start < 1):
        return []


print(IsPrime(50))
