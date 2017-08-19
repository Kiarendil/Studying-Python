def sum(a, b):
    if a == 1:
        return b + 1
    if b == 1:
        return a + 1

    s = a + sum(1, b - 1)
    return s


a = int(input())
b = int(input())

s = sum(a, b)

print(s)
