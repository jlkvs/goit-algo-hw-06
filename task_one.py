import networkx as nx
import matplotlib.pyplot as plt

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

plt.figure(figsize=(10, 8))
pos_social = nx.spring_layout(G_social)  
nx.draw(G_social, pos_social, with_labels=True, node_color="lightgreen", edge_color="purple", node_size=1200, font_size=10, font_weight="bold")
plt.title("Соціальна мережа дружніх зв'язків")
plt.show()

num_nodes_social = G_social.number_of_nodes()  
num_edges_social = G_social.number_of_edges()  
degree_distribution_social = dict(G_social.degree())  

num_nodes_social, num_edges_social, degree_distribution_social
