# animacion de un grafo de nodos y aristas
# desde una lista que contiene informacion del grafo en cada frame
# con netwrorkx y matplotlib

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns

# lista de grafos
# frames = [
#     {
#         'nodes': [
#             (1, {'color': 'skyblue', 'label': 'A'}),
#             (2, {'color': 'skyblue', 'label': 'B'}),
#             (3, {'color': 'skyblue', 'label': 'C'}),
#             (4, {'color': 'skyblue', 'label': 'D'}),
#             (5, {'color': 'skyblue', 'label': 'E'})
#         ],
#         'edges': [
#             (1, 2, {'weight': 1.0}),
#             (2, 3, {'weight': 1.0}),
#             (3, 4, {'weight': 1.0}),
#             (4, 5, {'weight': 1.0}),
#             (5, 1, {'weight': 1.0})
#         ]
#     },
#     {
#         'nodes': [
#             (1, {'color': 'skyblue', 'label': 'A'}),
#             (2, {'color': 'skyblue', 'label': 'B'}),
#             (3, {'color': 'skyblue', 'label': 'C'}),
#             (4, {'color': 'skyblue', 'label': 'D'}),
#             (5, {'color': 'red', 'label': 'E'})
#         ],
#         'edges': [
#             (1, 2, {'weight': 2.0}),
#             (2, 3, {'weight': 2.0}),
#             (3, 4, {'weight': 2.0}),
#             (4, 5, {'weight': 2.0}),
#             (5, 1, {'weight': 2.0})
#         ]
#     },
#     {
#         'nodes': [
#             (1, {'color': 'skyblue', 'label': 'A'}),
#             (2, {'color': 'skyblue', 'label': 'B'}),
#             (3, {'color': 'skyblue', 'label': 'C'}),
#             (4, {'color': 'red', 'label': 'D'}),
#             (5, {'color': 'red', 'label': 'E'})
#         ],
#         'edges': [
#             (1, 2, {'weight': 3.0}),
#             (2, 3, {'weight': 3.0}),
#             (3, 4, {'weight': 3.0}),
#             (4, 5, {'weight': 3.0}),
#             (5, 1, {'weight': 3.0})
#         ]
#     },
# ]

def read_json(file):
    import json
    with open(file) as f:
        data = json.load(f)
    return data

frames=read_json('frames.json')
# print(frames)

# inicializar figura  
fig, ax = plt.subplots()
sns.set_style('whitegrid')
G = nx.Graph()
G.add_nodes_from(frames[0]['nodes'])
for i in range(len(frames[0]['edges'])):
    G.add_edge(frames[0]['edges'][i][0], frames[0]['edges'][i][1], weight=frames[0]['edges'][i][2]['weight'])
pos = nx.spring_layout(G)
node_colors = [node[1]['color'] for node in G.nodes(data=True)]
nx.draw(G, pos, with_labels=False, node_size=700, node_color=node_colors, edge_color='gray', font_size=10, font_weight='bold')
print({node[0]: node[1] for node in G.nodes(data=True)})
nx.draw_networkx_labels(G, pos, labels={node[0]: node[1]['label'] for node in G.nodes(data=True)}, font_color='black')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"peso:{G[u][v]['weight']}\nR=\nD=V\n"  for u, v in G.edges()}, font_color='red') 

plt.tight_layout()


def init():
    G = nx.Graph()
    G.add_nodes_from(frames[0]['nodes'])
    G.add_edges_from(frames[0]['edges'])
    pos = nx.spring_layout(G)
    # nx.draw(G, pos, with_labels=False, node_size=700, node_color='skyblue', edge_color='gray', font_size=10, font_weight='bold')
    node_colors = [node[1]['color'] for node in G.nodes(data=True)]
    node_labels = {node[0]: node[1]['label'] for node in G.nodes(data=True)}
    nx.draw(G, pos, with_labels=False, node_size=700, node_color=node_colors, edge_color='gray', font_size=10, font_weight='bold')
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_color='black')

# funcion de animacion
def update(num):
    ax.clear()
    G = nx.Graph()
    G.add_nodes_from(frames[num]['nodes'])
    G.add_edges_from(frames[num]['edges'])
    node_colors = [node[1]['color'] for node in G.nodes(data=True)]
    nx.draw(G, pos, with_labels=False, node_size=700, node_color=node_colors, edge_color='gray', font_size=10, font_weight='bold')

    edge_labels = nx.get_edge_attributes(G, 'weight')
    edge_labels = edge_labels = {(u, v): f"peso:{G[u][v]['weight']}\nR=\nD=V\n"  for u, v in G.edges()}  # Obtener pesos de las aristas
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')  # Dibujar etiquetas de las aristas

    node_labels = {node[0]: f"{node[1]['label']}\n{node[1]['weight']}" for node in G.nodes(data=True)}
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_color='black')  # Dibujar etiquetas de los nodos

    plt.tight_layout()

# animacion
ani = animation.FuncAnimation(fig, update, frames=len(frames), interval=2500, repeat=True, init_func=init)
plt.show()