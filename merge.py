def mergesort(arr):
    return _mergesort(arr, 0, len(arr) - 1)

def _mergesort(arr, l, r):
    if l >= r:
        return

    m = int((l + r) / 2)

    _mergesort(arr, l, m)
    _mergesort(arr, m + 1, r)

    merge(arr, l, m, r)

def merge(arr, l, m, r):
    larr = arr[l:m + 1]
    rarr = arr[m + 1:r + 1]

    li = ri = 0
    i = l

    while li < len(larr) and ri < len(rarr):
        if larr[li] < rarr[ri]:
            arr[i] = larr[li]
            li += 1
        else:
            arr[i] = rarr[ri]
            ri += 1
        i += 1
    
    while ri < len(rarr):
        arr[i] = rarr[ri]
        ri += 1
        i += 1
    
    while li < len(larr):
        arr[i] = larr[li]
        li += 1
        i += 1

a = [9,3,7,5,0,1,10,17,-1,4,-2]
mergesort(a)
print(a)