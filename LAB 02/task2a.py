def merge(arr1, arr2, N, M):
    arr = []
    x, y = 0, 0
    while x < N and y < M:
        if arr1[x] < arr2[y]:
            arr.append(arr1[x])
            x += 1
        else:
            arr.append(arr2[y])
            y += 1
    arr += arr1[x:]
    arr += arr2[y:]
    return arr
def merge_sort(arr):
    if len(arr) > 1:
        l = len(arr)
        mid = l // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right, len(left), len(right))
    return arr


with open('input2a.txt', 'r') as f:
    N, arr1, M, arr2 = f.readlines()
    N, arr1, M, arr2 = int(N), list(map(int, arr1.split())), int(M), list(map(int, arr2.split()))

with open ('output2a.txt', 'w') as f:
    x = merge_sort(arr1+arr2)
    f.write(" ".join(map(str, x)))