def quicksort(arr):
    _quicksort(arr, 0, len(arr) - 1)


def _quicksort(arr, left, right):
    if left >= right:
        return

    pivot = partition(arr, left, right)

    _quicksort(arr, left, pivot - 1)
    _quicksort(arr, pivot + 1, right)


def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


a = [5, 8, 2, 9, 4, 7, 0, 10, 17, -1]
quicksort(a)
print(a)