def adjacency_list(arr, n):
    li = [[] for _ in range(n+1)]
    for i in arr:
        li[i[0]].append(i[1])
    return li

def DFS_topSort(source, li, visited, stack):
    if visited[source] == 'Checked':
        return
    visited[source] = True
    for i in li[source]:
        if visited[i] is not True:
            DFS_topSort(i, li, visited, stack)
        elif visited[i] is True:
            visited[0] = "IMPOSSIBLE"
    visited[source] = 'Checked'
    stack.append(source)
    for i in range(1, n+1):
        if visited[i] is not True:
            DFS_topSort(i, li, visited, stack)

with open('input1a.txt') as f:
    n, m = map(int, f.readline().split())
    input_data = [tuple(map(int, i.split())) for i in f.readlines()]
    visited = [False] * (n+1)
    source = input_data[0][0]
    stack = []

    DFS_topSort(source, adjacency_list(input_data, n), visited, stack)
    with open('output1a.txt', 'w') as out:
        if visited[0] == 'IMPOSSIBLE':
            out.write('IMPOSSIBLE')
        else:
            out.write(" ".join(map(str, reversed(stack))))