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
        'edges': [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]
    },
    {
        'nodes': [1, 2, 3, 4, 5],
        'edges': [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3)]
    },
    {
        'nodes': [1, 2, 3, 4, 5],
        'edges': [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3), (2, 4)]
    },
    {
        'nodes': [1, 2, 3, 4, 5],
        'edges': [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3), (2, 4), (3, 5)]
    },
    {
        'nodes': [1, 2, 3, 4, 5],
        'edges': [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3), (2, 4), (3, 5), (4, 1)]
    },
    {
        'nodes': [1, 2, 3, 4, 5],
        'edges': [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3), (2, 4), (3, 5), (4, 1), (5, 2)]
    }
]

# inicializar figura  
fig, ax = plt.subplots()
sns.set_style('whitegrid')
G = nx.Graph()
G.add_nodes_from(frames[0]['nodes'])
G.add_edges_from(frames[0]['edges'])
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