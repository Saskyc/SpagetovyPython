"""
Integer
"""
a=5

print("====Integer test====")
print(type(a))
print(a)


"""
Float
"""
b=5.1

print("Float test")
print(type(b))
print(b)


"""
String
"""
c="string"

print("====String test====")
print(type(c))
print(c)


"""
List
"""
d=\
    [
        1,
        2,
        3,
        "string",
    ]
print("====List test====")
print(type(d))

print(d[0]); """1"""
print(d[3]); """string"""

print(d[-1]); """string"""
print(d[-2]); """3"""


"""
Dictionary
"""
e=\
    {
        1: "one",
        2: "two",
        3: "three",
        "Four": 4,
        5: {
            1: {
                2: {
                    3: "Epic le",
                }
            }
        }
    }
print("====Dictionary test====")
print(type(e))
print(e[2])
print(e["Four"])
print(e[5][1][2][3])