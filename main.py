# animacion de un grafo de nodos y aristas
# desde una lista que contiene informacion del grafo en cada frame
# con netwrorkx y matplotlib

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns

# lista de grafos
frames = [
    {
        'nodes': [1, 2, 3, 4, 5],
        'edges': [
          (1, 2, {'weight': 1.0}),
          (2, 3, {'weight': 1.0}),
          (3, 4, {'weight': 1.0}),
          (4, 5, {'weight': 1.0}),
          (5, 1, {'weight': 1.0})
          ]
    },
    {
        'nodes': [1, 2, 3, 4, 5],
        'edges': [
          (1, 2, {'weight': 1.0}),
          (2, 3, {'weight': 1.0}),
          (3, 4, {'weight': 1.0}),
          (4, 5, {'weight': 1.0}),
          (5, 1, {'weight': 1.0})
        ]
    },
    {
        'nodes': [1, 2, 3, 4, 5],
        'edges': [
          (1, 2, {'weight': 1.0}),
          (2, 3, {'weight': 1.0}),
          (3, 4, {'weight': 1.0}),
          (4, 5, {'weight': 1.0}),
          (5, 1, {'weight': 1.0})
        ]
    }
]

# inicializar figura  
fig, ax = plt.subplots()
sns.set_style('whitegrid')
G = nx.Graph()
G.add_nodes_from(frames[0]['nodes'])
for i in range(len(frames[0]['edges'])):
    G.add_edge(frames[0]['edges'][i][0], frames[0]['edges'][i][1], weight=frames[0]['edges'][i][2]['weight'])
# G.add_edges_from(frames[0]['edges'])
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', edge_color='gray', font_size=10, font_weight='bold')
plt.tight_layout()

# funcion de animacion
def update(num):
    ax.clear()
    G = nx.Graph()
    G.add_nodes_from(frames[num]['nodes'])
    G.add_edges_from(frames[num]['edges'])
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', edge_color='gray', font_size=10, font_weight='bold')
    plt.tight_layout()

# animacion
ani = animation.FuncAnimation(fig, update, frames=len(frames), interval=1000, repeat=True)
plt.show()