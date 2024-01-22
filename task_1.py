import networkx as nx
import matplotlib.pyplot as plt

graph = {
    "Westerstede": ["Oldenburg", "Leer"],
    "Leer": ["Westerstede", "Cloppenburg"],
    "Oldenburg": ["Bremen", "Cloppenburg", "Bremerhaven"],
    "Bremen": ["Hannover", "Hamburg", "Bremerhaven", "Cloppenburg", "Bielefeld"],
    "Bremerhaven": ["Bremen", "Hamburg", "Oldenburg"],
    "Hamburg": ["Bremen", "Bremerhaven", "Hannover", "Berlin"],
    "Hannover": ["Bremen", "Hamburg", "Bielefeld", "Berlin"],
    "Cloppenburg": ["Oldenburg", "Leer", "Bremen", "Osnabruck"],
    "Osnabruck": ["Cloppenburg", "Bielefeld", "Munster"],
    "Bielefeld": ["Osnabruck", "Hannover", "Bremen"],
    "Berlin": ["Hamburg", "Hannover"],
    "Munster": ["Osnabruck"],
}

G = nx.Graph(graph)
G.nodes["Westerstede"]["color"] = "green"
G.nodes["Hannover"]["color"] = "yellow"
G.nodes["Bremen"]["color"] = "yellow"

G["Westerstede"]["Oldenburg"]["weight"] = 0.4
G["Westerstede"]["Leer"]["weight"] = 0.5
G["Cloppenburg"]["Leer"]["weight"] = 1
G["Cloppenburg"]["Oldenburg"]["weight"] = 0.7
G["Bremen"]["Oldenburg"]["weight"] = 0.7
G["Bremerhaven"]["Oldenburg"]["weight"] = 1.1
G["Bremen"]["Hannover"]["weight"] = 1.5
G["Bremen"]["Hamburg"]["weight"] = 1.4
G["Bremen"]["Bremerhaven"]["weight"] = 0.8
G["Bremen"]["Cloppenburg"]["weight"] = 0.9
G["Bremen"]["Bielefeld"]["weight"] = 2.1
G["Bremerhaven"]["Hamburg"]["weight"] = 2
G["Hamburg"]["Hannover"]["weight"] = 1.9
G["Hamburg"]["Berlin"]["weight"] = 3.2
G["Hannover"]["Berlin"]["weight"] = 3.3
G["Hannover"]["Bielefeld"]["weight"] = 1.3
G["Cloppenburg"]["Osnabruck"]["weight"] = 1
G["Bielefeld"]["Osnabruck"]["weight"] = 0.8
G["Munster"]["Osnabruck"]["weight"] = 0.9

if __name__ == "__main__":
    plt.figure(figsize=(15, 10))
    pos = nx.spring_layout(G, seed=30)
    options = {
        "node_color": "lightblue",
        "edge_color": "blue",
        "node_size": 3000,
        "width": 3,
        "with_labels": True,
    }
    nx.draw(G, pos, **options)
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Graph analisys
    number_of_nodes = G.number_of_nodes()
    number_of_edges = G.number_of_edges()
    is_connected = nx.is_connected(G)
    neighbours_of_Hannover = G["Hannover"]

    degree_centrality = nx.degree_centrality(G)
    closeness_centrality = nx.closeness_centrality(G)
    betweenness_centrality = nx.betweenness_centrality(G)

    print("-" * 70)
    print("Number of graph nodes: ", number_of_nodes)
    print("Number of graph edges: ", number_of_edges)
    print("Graph is connected" if is_connected else "Graph isn't connected")
    print("Neighbour nodes of Hannover: ", neighbours_of_Hannover)

    print("-" * 70)
    print("Degree centrality: ", degree_centrality)
    print("-" * 70)
    print("Closeness centrality: ", closeness_centrality)
    print("-" * 70)
    print("Betweenness centrality: ", betweenness_centrality)
    print("-" * 70)

    path = nx.shortest_path(G, source="Westerstede", target="Hannover")
    avr_path_length = nx.average_shortest_path_length(G)
    print("The sortest path from Weaterstede to Hannover is: ", path)
    print("Average lehgth of the shortest path is: ", avr_path_length)
    print("-" * 70)

    plt.title("North of Germany Map")
    plt.show()
