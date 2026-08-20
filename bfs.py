import heapq

n = int(input("Enter number of vertices: "))

graph = {}

for i in range(n):
    graph[i] = []

e = int(input("Enter number of edges: "))

for i in range(e):
    u, v = map(int, input("Enter edge (u v): ").split())
    graph[u].append(v)
    graph[v].append(u)

heuristic = {}

print("Enter heuristic values:")

for i in range(n):
    heuristic[i] = int(input(f"h({i}) = "))

start = int(input("Enter starting vertex: "))
goal = int(input("Enter goal vertex: "))

visited = set()
priority_queue = [(heuristic[start], start)]

print("Best-First Search: ", end=" ")

while priority_queue:
    h, current = heapq.heappop(priority_queue)

    if current in visited:
        continue

    visited.add(current)
    print(current, end=" ")

    if current == goal:
        break

    for neighbour in graph[current]:
        if neighbour not in visited:
            heapq.heappush(priority_queue, (heuristic[neighbour], neighbour))