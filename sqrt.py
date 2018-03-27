def sqrt(n):
    if n < 2:
        return n
    l = 2
    r = int(n / 2)

    while l <= r:
        m = int((l + r) / 2)

        if n < m * m:
            r = m - 1
        elif n > m * m:
            l = m + 1
        else:
            return m

    return None


r = sqrt(10)
print(r)