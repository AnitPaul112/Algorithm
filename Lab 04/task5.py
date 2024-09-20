from collections import deque

with open("input5.txt", "r") as inputFileOpening:
    inputFile = inputFileOpening.readlines()

N, M, D = map(int, inputFile[0].split())
destination = int(D)

graph = {}
for i in range(1, N + 1):
    graph[i] = []

for i in inputFile[1:]:
    u, v = map(int, i.split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(graph, start, end):
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        current, path = queue.popleft()
        if current == end:
            return path
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return []

shortest_path = bfs(graph, 1, destination)

if not shortest_path:
    with open("output5.txt", "w") as outputFile:
        outputFile.write("IMPOSSIBLE")
else:
    with open("output5.txt", "w") as outputFile:
        outputFile.write(f"Time: {len(shortest_path) - 1}\n")
        outputFile.write("Shortest Path: " + " ".join(map(str, shortest_path)))
