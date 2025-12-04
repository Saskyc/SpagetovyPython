def bubblesort(seznam : list[int]) -> list[int]:
    for i in range(len(seznam)):
        for j in range(len(seznam) - i - 1):
            if seznam[j] > seznam[j + 1]:
                seznam[j], seznam[j + 1] = seznam[j + 1], seznam[j]
    return seznam

print(bubblesort([64, 34, 25, 12, 22, 11, 90]))