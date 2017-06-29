def distance(x_1, y_1, x_2, y_2):
    r = ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5

    return r

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(distance(a, b, c, d))
