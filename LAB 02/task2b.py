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


with open('input2b.txt', 'r') as f:
    N, arr1, M, arr2 = f.readlines()
    N, arr1, M, arr2 = int(N), list(map(int, arr1.split())), int(M), list(map(int, arr2.split()))

with open ('output2b.txt', 'w') as f:
    x = merge(arr1, arr2, N, M)
    f.write(" ".join(map(str, x)))