def power(a, n):
    if n == 0:
        return 1

    if n < 0:
        n_m = -n
        a_n = a * power(a, n_m - 1)
        return 1 / a_n

    if n > 0:
        a_n = a * power(a, n - 1)
        return a_n

a = float(input())
n = int(input())

print(power(a, n))
