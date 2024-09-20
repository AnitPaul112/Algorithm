def sum(N, S, arr):
    d = {}
    for i in range(N):
        j = S - arr[i]
        if j in d:
            return d[j] + 1, i+1
        else:
            d[arr[i]] = i
    return "IMPOSSIBLE"


with open('input1b.txt', 'r') as f:
    N, S = map(int, f.readline().split())
    arr = list(map(int, f.readline().split()))
with open('output1b.txt', 'w') as f:
    idx = sum(N, S, arr)
    if idx == 'IMPOSSIBLE':
        f.write(idx)
    else:
        f.write(f'{idx[0]} {idx[1]}')