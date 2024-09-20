def partition(arr, l, h):
    pivot = arr[h]
    i = l - 1
    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1

def quicksort(arr, l, h):
    if l < h:
        p = int(partition(arr, l, h))
        quicksort(arr, l, p - 1)
        quicksort(arr, p + 1, h)
    return arr

with open('input5.txt', 'r') as f:
    N, arr = f.readlines()
    N, arr = int(N), list(map(int, arr.split()))

with open('output5.txt', 'w') as f:
    x = quicksort(arr, 0, N-1)
    f.write(" ".join(map(str, x)))