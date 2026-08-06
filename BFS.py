graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

visited = []
queue = []

start = 'A'
visited.append(start)
queue.append(start)

print("BFS Traversal:", end=" ")

while queue:
    node = queue.pop(0)
    print(node, end=" ")

    for i in graph[node]:
        if i not in visited:
            visited.append(i)
            queue.append(i)