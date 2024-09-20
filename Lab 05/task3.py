def dfs(node, adj_list, visited, stack):
    visited[node] = 1

    for adj_node in adj_list[node]:
        if visited[adj_node] == 0:
            dfs(adj_node, adj_list, visited, stack)

    stack.append(node)

def dfs_transpose(transpose_list, visited_transpose, source, component):
    visited_transpose[source] = 1
    component.append(source)

    for adj_node in transpose_list[source]:
        if visited_transpose[adj_node] == 0:
            dfs_transpose(transpose_list, visited_transpose, adj_node, component)

with open("input3.txt", "r") as f:
    n, m = map(int, f.readline().split())
    adj_list = [[] for _ in range(n + 1)]
    transpose_list = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    visited_transpose = [0] * (n + 1)
    stack = []

    for i in range(m):
        u, v = map(int, f.readline().split())
        adj_list[u].append(v)
        transpose_list[v].append(u)

    for i in range(1, n + 1):
        if visited[i] == 0:
            dfs(i, adj_list, visited, stack)

    strongly_connected_components = []
    while stack:
        print(stack)
        node = stack.pop()
        if visited_transpose[node] == 0:
            component = []
            dfs_transpose(transpose_list, visited_transpose, node, component)
            print(component,'c')
            strongly_connected_components.append(component)

with open("output3.txt", "w") as f:
    for component in strongly_connected_components:
        for i in component:
            f.write(str(i) + " ")
    f.write("\n")
