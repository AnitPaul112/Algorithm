input_file = open('input1.txt', 'r')
output_file = open('output1.txt', 'w')

node, edge = list(map(int, input_file.readline().split()))

graph1 = {}

for i in range(1, edge):
  if i not in graph1:
    graph1[i] = {}

for i in range(edge):
  array1=list(map(int,input_file.readline().split()))
  if array1[0] in graph1:
    graph1[array1[0]].update({array1[1]: array1[2]})

source = input_file.readline().strip()

def dijkstra(graph, start, destination):
  distance = {}
  unvisited_graph = graph.copy()

  for i in unvisited_graph:
    distance[i] = float('inf')
  distance[start] = 0

  while unvisited_graph:
    d_node = None

    for j in unvisited_graph:
      if d_node is None:
        d_node = j
      elif distance[j] < distance[d_node]:
        d_node = j

    adj_routes = graph[d_node].items()

    for child, cost in adj_routes:

      if cost + distance[d_node] < distance[child]:
        distance[child] = cost + distance[d_node]

    unvisited_graph.pop(d_node)

  if distance[destination] != float('inf'):
    print(f'{distance[destination]}', end = " ", file = output_file)

  else:
    print('-1 ', end = ' ', file = output_file)

for i in range(1, node + 1):
  dijkstra(graph1, int(source), i)

output_file.close()