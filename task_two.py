import networkx as nx

G_social = nx.Graph()

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

G_social.add_edges_from(social_edges)

def dfs_path(graph, start, goal):
    try:
        return list(nx.dfs_edges(graph, source=start))
    except nx.NetworkXNoPath:
        return []

def bfs_path(graph, start, goal):
    try:
        return list(nx.bfs_edges(graph, source=start))
    except nx.NetworkXNoPath:
        return []

start_node = "Аліна"
end_node = "Іванка"

dfs_path_edges = dfs_path(G_social, start_node, end_node)
bfs_path_edges = bfs_path(G_social, start_node, end_node)

print("Шлях, знайдений DFS:", dfs_path_edges)
print("Шлях, знайдений BFS:", bfs_path_edges)
