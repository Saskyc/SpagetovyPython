while True:
    print("Arcane Number Interpreter")
    s = input("Input number: ").strip()

    if not s.isdigit():
        print("Error: input must be a non-negative integer (only 0-9 digits).") 
    else:
        break

n = int(s)

if n == 0:
    data = b"\x00"
else:
    out = bytearray()
    x = n
    while x > 0:
        out.append(x & 0xFF)
        x >>= 8
    out.reverse()
    data = bytes(out)

text = data.decode("latin-1")
print("Result:", text)