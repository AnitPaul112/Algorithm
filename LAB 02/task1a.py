def sum(N, S, arr):
    for i in range(N):
        for j in range(i + 1, N):
            if arr[i] + arr[j] == S:
                return i + 1, j + 1
    return "IMPOSSIBLE"


with open('input1a.txt', 'r') as f:
    N, S = map(int, f.readline().split())
    arr = list(map(int, f.readline().split()))
with open('output1a.txt', 'w') as f:
    idx = sum(N, S, arr)
    if idx == 'IMPOSSIBLE':
        f.write(idx)
    else:
        f.write(f'{idx[0]} {idx[1]}')