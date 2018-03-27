def fib(n):
    a = [0, 1, 1]

    if n < 3:
        return a[n]

    for _ in range(3, n + 1):
        a = a[1], a[2], a[1] + a[2]

    return a[2]


print(0, fib(0))

print(1, fib(1))

print(5, fib(5))

print(10, fib(10))

print(100, fib(100))