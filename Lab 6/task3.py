input_file = open('input3.txt', 'r')
output_file = open('output3.txt', 'w')

node, edge = list(map(int, input_file.readline().split()))

graph1 = {}

for i in range(1, edge):
    if i not in graph1:
        graph1[i] = {}

for i in range(edge):
    array1=list(map(int,input_file.readline().split()))
    if array1[0] in graph1:
        graph1[array1[0]].update({array1[1]: array1[2]})


def dijkstra(graph, start, destination):
    minimum_distance = {}
    unvisited_graph = graph.copy()
    track_predecessor = {}
    track_path = []
    edges = {}

    for i in unvisited_graph:
        minimum_distance[i] = float('inf')
    minimum_distance[start] = 0

    while unvisited_graph:
        d_node = None

        for j in unvisited_graph:
            if d_node is None:
                d_node = j
            elif minimum_distance[j] < minimum_distance[d_node]:
                d_node = j

        adj_routes = graph[d_node].items()

        for child, cost in adj_routes:

            if minimum_distance[d_node] < minimum_distance[child]:
                minimum_distance[child] = cost
                track_predecessor[child] = d_node
                edges[d_node] = cost

        unvisited_graph.pop(d_node)

    currentNode = destination

    while currentNode != start:
        try:
            track_path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]
        except KeyError:
            output_file.write("Impossible")
            return
    track_path.insert(0, start)

    danger = []
    for i in track_path:
        danger.append(minimum_distance[i])
    output_file.write(str(max(danger)))

dijkstra(graph1, 1, int(node))

output_file.close()
