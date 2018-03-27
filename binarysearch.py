def binarysearch(arr, v):
    l = 0
    r = len(arr) - 1

    while l <= r:
        m = int((l + r) / 2)

        if v < arr[m]:
            r = m - 1
        elif v > arr[m]:
            l = m + 1
        else:
            return m

    return -1


a = [-1, 0, 2, 4, 5, 7, 8, 9, 10, 17]
i = binarysearch(a, -4)
print(i)