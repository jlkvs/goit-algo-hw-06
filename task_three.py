import networkx as nx
import random

social_edges = [
    ("Аліна", "Богдан"),
    ("Аліна", "Катерина"),
    ("Аліна", "Данило"),
    ("Богдан", "Данило"),
    ("Богдан", "Єва"),
    ("Катерина", "Єва"),
    ("Катерина", "Федір"),
    ("Данило", "Ганна"),
    ("Єва", "Ганна"),
    ("Федір", "Ганна"),
    ("Ганна", "Григорій"),
    ("Григорій", "Іванка"),
    ("Федір", "Іванка"),
    ("Іванка", "Катерина")
]

G_weighted_social = nx.Graph()
weighted_edges = [(u, v, random.randint(1, 10)) for u, v in social_edges]  
G_weighted_social.add_weighted_edges_from(weighted_edges)

shortest_paths_dijkstra = dict(nx.all_pairs_dijkstra_path(G_weighted_social))

print("Ваги ребер:")
for edge in weighted_edges:
    print(f"{edge[0]} - {edge[1]}: {edge[2]}")

print("\nНайкоротші шляхи між усіма вершинами:")
for source, paths in shortest_paths_dijkstra.items():
    for target, path in paths.items():
        print(f"{source} до {target}: Шлях - {path}")
