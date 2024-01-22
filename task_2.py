from collections import deque
import networkx as nx

from task_1 import graph, G


# Deep First search realisation
def dfs_search(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=" ")  # print visited vertexes

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_search(graph, neighbor, visited)


# Bread First search realisation
def bfs_search(graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return
    vertex = queue.popleft()

    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
    bfs_search(graph, queue, visited)


if __name__ == "__main__":
    print("\n", "-" * 70)
    print("DFS programm realisation: ")
    dfs_search(graph, "Westerstede")
    print("\n", "-" * 70)
    print("BFS programm realisation: ")
    bfs_search(graph, deque(["Westerstede"]))
    print("\n", "-" * 70)

    # DFS
    dfs_tree = nx.dfs_tree(G, source="Westerstede")
    print(list(dfs_tree.nodes()))

    # BFS
    bfs_tree = nx.bfs_tree(G, source="Westerstede")
    print(list(bfs_tree.nodes()))
