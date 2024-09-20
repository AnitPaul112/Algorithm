input_file = open('input2.txt', 'r')
output_file = open('output2.txt', 'w')

node, edge = list(map(int, input_file.readline().split()))

graph1 = {}

for i in range(1, node+1):
  if i not in graph1:
    graph1[i]={}

for i in range(edge):
  arr = list(map(int, input_file.readline().split()))
  if arr[0] in graph1:
    graph1[arr[0]].update({arr[1]: arr[2]})

alice_pos, bob_pos= list(map(int, input_file.readline().split()))


def dijkstra(graph, start):
  minimum_distance = {}
  unvisited_graph = graph.copy()

  for i in unvisited_graph:
    minimum_distance[i]= float('inf')
  minimum_distance[start]=0

  while unvisited_graph:

    d_node=None

    for j in unvisited_graph:
      if d_node is None:
        d_node= j
      elif minimum_distance[j]< minimum_distance[d_node]:
        d_node= j

    adj_routes = graph[d_node].items()

    for child, cost in adj_routes:
      if cost + minimum_distance[d_node] < minimum_distance[child]:
          minimum_distance[child] = cost + minimum_distance[d_node]

    unvisited_graph.pop(d_node)
  return minimum_distance

x = dijkstra(graph1, alice_pos)
y = dijkstra(graph1, bob_pos)

min_node = -1
min_time = float('inf')
distance = None
alice = []
bob = []

for u,v in x.items():
  alice.append(v)
for u, v in y.items():
  bob.append(v)

for i in range(1, node):
  if alice[i] != float('inf') and bob[i] != float('inf'):
    distance = max(alice[i], bob[i])
    if distance < min_time:
      min_time = distance
      min_node = i + 1

if distance == None:
    output_file.write("Impossible")
else:
    output_file.write(f'Time {min_time}\nNode {min_node}')

output_file.close()
