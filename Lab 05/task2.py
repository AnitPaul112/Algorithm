from queue import PriorityQueue

def adjacency_list(arr, n):
    li = [[] for _ in range(n + 1)]
    for i in arr:
        li[i[0]].append(i[1])
    return li

def BFS_topSort(li, in_degree):

    for node in range(1, len(in_degree)):
        if in_degree[node] == 0:
            queue.put(node)
            visited[node] = True

    while not queue.empty():
        current_node = queue.get(0)
        result.append(current_node)

        for i in li[current_node]:
            in_degree[i] -= 1
            if in_degree[i] == 0 and not visited[i]:
                queue.put(i)
                visited[i] = True

    if len(result) == n:
        return result
    else:
        return 'IMPOSSIBLE'

with open('input2.txt') as f:
    n, m = map(int, f.readline().split())
    input_data = [tuple(map(int, i.split())) for i in f.readlines()]
    visited = [False] * (n + 1)
    source = input_data[0][0]
    queue = PriorityQueue()
    result = []
    in_degree = [0] * (n + 1)
    li = adjacency_list(input_data, n)
    for neighbors in li:
        for neighbor in neighbors:
            in_degree[neighbor] += 1

    result = BFS_topSort(li, in_degree)
    with open('output2.txt', 'w') as out:
        if result == 'IMPOSSIBLE':
            out.write("IMPOSSIBLE")
        else:
            out.write(' '.join(map(str,result)))
