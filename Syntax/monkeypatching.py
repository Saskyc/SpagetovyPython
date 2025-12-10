from forbiddenfruit import curse

def __iter__(self : int):
    for u in str(self):
        yield int(u)
int.__iter__ = __iter__

for i in 5:
    print(i)