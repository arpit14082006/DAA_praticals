# Practical 8
# Implementation of Graph and Searching (DFS and BFS)

from collections import deque

# Graph using adjacency list
'''
     A 
    / \
   B   C
  / \   \
 D   E   F
'''
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}


# Depth First Search (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)


# Breadth First Search (BFS)
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


# Starting vertex
start = 'A'

print("DFS Traversal:")
dfs(graph, start)

print("\nBFS Traversal:")
bfs(graph, start)