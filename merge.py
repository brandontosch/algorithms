def mergesort(a):
    _mergesort(a, 0, len(a) - 1, [None] * len(a))


def _mergesort(a, leftStart, rightEnd, t):
    if leftStart >= rightEnd:
        return
    mid = int((leftStart + rightEnd) / 2)
    _mergesort(a, leftStart, mid, t)
    _mergesort(a, mid + 1, rightEnd, t)
    return merge(a, leftStart, rightEnd, t)


def merge(a, leftStart, rightEnd, t):
    leftEnd = int((rightEnd + leftStart) / 2)
    rightStart = leftEnd + 1
    size = rightEnd - leftStart + 1

    l = leftStart
    r = rightStart
    i = leftStart

    while l <= leftEnd and r <= rightEnd:
        if a[l] <= a[r]:
            t[i] = a[l]
            l += 1
        else:
            t[i] = a[r]
            r += 1
        i += 1

    while l <= leftEnd:
        t[i] = a[l]
        i += 1
        l += 1

    while r <= rightEnd:
        t[i] = a[r]
        i += 1
        r += 1

    for x in range(leftStart, size):
        a[x] = t[x]


arr = [9, 5, 2, 6, 3, 10, 4, 13, 11]
mergesort(arr)
print(arr)