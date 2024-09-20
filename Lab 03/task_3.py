def merge(arr1, arr2):
    arr = []
    i, j = 0, 0
    count = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            count += len(arr1) - i
            arr.append(arr2[j])
            j += 1
        else:
            arr.append(arr1[i])
            i += 1
    arr += arr1[i:]
    arr += arr2[j:]
    return arr, count
def mergeSort(arr):
    if len(arr) > 1:
        l = len(arr)
        mid = l // 2
        left, lc = mergeSort(arr[:mid])
        right, rc = mergeSort(arr[mid:])
        new_arr, count = merge(left, right)
        total = lc + rc + count
        return new_arr, total
    return arr, 0


with open('input3.txt', 'r') as f:
    N, arr = f.readlines()
    N, arr = int(N), list(map(int, arr.split()))

with open ('output3.txt', 'w') as f:
    x, y = mergeSort(arr)
    f.write(str(y))