def IsSorted(list):

    lastItem = None
    for item in list:
        if lastItem is None:
            lastItem = item
            continue

        if item >= lastItem:
            lastItem = item
            print(f"I: {item} was bigger then LI: {lastItem}")
            continue

        print(f"I: {item} was lower then LI: {lastItem}")
        return False

    return True

def SortOneNumber(list):
    lastItem = None
    lastIndex = None

    index = 0

    wasBroke = False
    set = False
    returnList = []

    for item in list:
        if set is True:
            returnList.append(item)
            continue

        index += 1
        if lastItem is None:
            print(f"LastItem was set, because it was None to: {item}")
            lastItem = item
            lastIndex = index
            continue

        if lastItem <= item:
            print(f"lA: {lastItem} <= {item}")
            returnList.append(lastItem)
            lastItem = item
            continue

        print(f"lA: {lastItem} > {item}")
        returnList.append(item)
        returnList.append(lastItem)
        set = True

    return returnList

seznam = [5, 9, 3, 6, 4, 7, 7, 2, 1, 8]

seznamA = [1, 2, 2, 2, 7, 7, 9]

print(IsSorted(seznam))
print(IsSorted(seznamA))

print("First Sort")
print(seznam)

while IsSorted(seznam) is False:
    print("Sort")
    seznam = SortOneNumber(seznam)
    print(seznam)

print(seznam)

