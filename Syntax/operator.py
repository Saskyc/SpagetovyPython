"""
Python operátory:
+ - * / <= < > >= = == ...
"""
a = 5
b = 4


print(b < a)
print(b > a)

print(b != a)

age = 17

if age < 15:
    print("Dítě")
elif age >= 15 and age < 18:
    print("Mladistvé")
else:
    print("Dospělí")

if age >= 18:
    print("Alkohol může být prodán")
else:
    print("Alkohol nemůže být prodán")