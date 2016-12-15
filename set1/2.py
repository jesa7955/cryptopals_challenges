def fixed_xor(a, b):
    return hex(int(a, 16) ^ int(b, 16))[2:]
a = input()
b = input()
print(fixed_xor(a, b))
