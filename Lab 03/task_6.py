def partition(arr, l, h):
    pivot = arr[h]
    i = l - 1
    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1

def quickfind(arr, l, h, k):

    p = partition(arr, l, h)
    if p == k-1:
        return arr[p]
    elif p > k-1:
        return quickfind(arr, l, p - 1, k)
    else:
        return quickfind(arr, p + 1, h, k)


with open('input6.txt', 'r') as f:
    N = int(f.readline().strip("\n"))
    arr = [int(i) for i in f.readline().strip("\n").split()]
    q = int(f.readline().strip("\n"))

    with open('output6.txt', 'w') as f1:
        for i in range(q):
            k = int(f.readline().strip("\n"))
            x = quickfind(arr, 0, N-1, k)
            f1.write(f"{x}\n")

