import heapq

graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    graph[i] = []

e = int(input("Enter number of edges: "))

print("Enter edges: source destination cost")
for i in range(e):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))
    graph[v].append((u, cost))

h = list(map(int, input("Enter heuristic values: ").split()))

start = int(input("Enter start node: "))
goal = int(input("Enter goal node: "))

pq = [(h[start], 0, start)]
parent = {start: None}
cost = {start: 0}

while pq:
    f, g, node = heapq.heappop(pq)

    if node == goal:
        break

    for next_node, edge_cost in graph[node]:
        new_cost = g + edge_cost

        if next_node not in cost or new_cost < cost[next_node]:
            cost[next_node] = new_cost
            f = new_cost + h[next_node]
            heapq.heappush(pq, (f, new_cost, next_node))
            parent[next_node] = node

# Print path
path = []
node = goal

while node is not None:
    path.append(node)
    node = parent.get(node)

path.reverse()

print("Path:", " -> ".join(map(str, path)))
print("Cost:", cost.get(goal, "No path"))