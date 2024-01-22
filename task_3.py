graph = {
    "Westerstede": {"Oldenburg": 0.4, "Leer": 0.5},
    "Leer": {"Westerstede": 0.5, "Cloppenburg": 1},
    "Oldenburg": {"Bremen": 0.7, "Cloppenburg": 0.7, "Bremerhaven": 1.1},
    "Bremen": {
        "Hannover": 1.5,
        "Hamburg": 1.4,
        "Bremerhaven": 0.8,
        "Cloppenburg": 0.9,
        "Bielefeld": 2.1,
    },
    "Bremerhaven": {"Bremen": 0.8, "Hamburg": 2, "Oldenburg": 1.1},
    "Hamburg": {"Bremen": 1.4, "Bremerhaven": 2, "Hannover": 1.9, "Berlin": 3.2},
    "Hannover": {"Bremen": 1.5, "Hamburg": 1.9, "Bielefeld": 1.3, "Berlin": 3.3},
    "Cloppenburg": {"Oldenburg": 0.7, "Leer": 1, "Bremen": 0.9, "Osnabruck": 1},
    "Osnabruck": {"Cloppenburg": 1, "Bielefeld": 0.8, "Munster": 0.9},
    "Bielefeld": {"Osnabruck": 0.8, "Hannover": 1.3, "Bremen": 2.1},
    "Berlin": {"Hamburg": 3.2, "Hannover": 3.3},
    "Munster": {"Osnabruck": 0.9},
}

# G["Westerstede"]["Oldenburg"]["weight"] = 0.4
# G["Westerstede"]["Leer"]["weight"] = 0.5
# G["Cloppenburg"]["Leer"]["weight"] = 1
# G["Cloppenburg"]["Oldenburg"]["weight"] = 0.7
# G["Bremen"]["Oldenburg"]["weight"] = 0.7
# G["Bremerhaven"]["Oldenburg"]["weight"] = 1.1
# G["Bremen"]["Hannover"]["weight"] = 1.5
# G["Bremen"]["Hamburg"]["weight"] = 1.4
# G["Bremen"]["Bremerhaven"]["weight"] = 0.8
# G["Bremen"]["Cloppenburg"]["weight"] = 0.9
# G["Bremen"]["Bielefeld"]["weight"] = 2.1
# G["Bremerhaven"]["Hamburg"]["weight"] = 2
# G["Hamburg"]["Hannover"]["weight"] = 1.9
# G["Hamburg"]["Berlin"]["weight"] = 3.2
# G["Hannover"]["Berlin"]["weight"] = 3.3
# G["Hannover"]["Bielefeld"]["weight"] = 1.3
# G["Cloppenburg"]["Osnabruck"]["weight"] = 1
# G["Bielefeld"]["Osnabruck"]["weight"] = 0.8
# G["Munster"]["Osnabruck"]["weight"] = 0.9


def dijkstra(graph, start):
    # distances and unvisited vertexes initialisation
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        # find vertex with the shortest distance between unvisited
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float("infinity"):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # if new distance is shorter we update shortest path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
            # deleting current vertex from visited ones
        unvisited.remove(current_vertex)

    return distances


if __name__ == "__main__":
    print('\n')
    print(f"{'City':<12}  |  {'Distance':<12}")
    print("-" * 30)
    for city, distance in dijkstra(graph, "Westerstede").items():
        print(f"{city:<12} --> {distance:<12}")
    print("-" * 30)
