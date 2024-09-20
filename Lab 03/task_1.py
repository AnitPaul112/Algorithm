def merge(arr1, arr2):
    arr = []
    x, y = 0, 0
    while x < len(arr1) and y < len(arr2):
        if arr1[x] < arr2[y]:
            arr.append(arr1[x])
            x += 1
        else:
            arr.append(arr2[y])
            y += 1
    arr += arr1[x:]
    arr += arr2[y:]
    return arr
def mergeSort(arr):
    if len(arr) > 1:
        l = len(arr)
        mid = l // 2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])
        return merge(left, right)
    return arr


with open('input1.txt', 'r') as f:
    N, arr = f.readlines()
    N, arr = int(N), list(map(int, arr.split()))

with open ('output1.txt', 'w') as f:
    x = mergeSort(arr)
    f.write(" ".join(map(str, x)))
