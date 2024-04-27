import math
import time
import json
"""
M es el tamano de dato que enviaremos
"""
M = 100
class Node:
    def __init__(self, name, label=None):
        self.name = name
        self.color = 'skyblue'
        self.neighbors = {}  # Dictionary to store neighbors and edge information
        self.parent = None  # Parent node in the path self.heuristic_value = 0  # default Heuristic value for A* search def add_neighbor(self, neighbor, speed, distance, retransmission): self.neighbors[neighbor] = {'speed': speed, 'distance': distance, 'retransmission': retransmission}
        self.heuristic_value = 0
        self.attr = {}
        self.label = label
    
    def add_neighbor(self, neighbor, speed, distance, retransmission):
        self.neighbors[neighbor] = {'speed': speed, 'distance': distance, 'retransmission': retransmission}



    def __repr__(self):
        if type(self.name) == int:
            return str(self.name)
        return str(self.name)
    def __str__(self):
        return str(self.name)

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def add_edge(self, node1, node2, speed, distance, retransmission):
        if node1.name in self.nodes and node2.name in self.nodes:
            self.nodes[node1.name].add_neighbor(node2, speed, distance, retransmission)
            self.nodes[node2.name].add_neighbor(node1, speed, distance, retransmission)
        else:
            raise ValueError("Nodes not in graph")

def heuristic(edge_info, parent_node):
    def serverLatency(speed, distance, retransmission):
        s1 = float(M)/float(speed)
        s2 = math.floor(distance/retransmission)
        return s1 + s2
    suma = parent_node.heuristic_value + serverLatency(edge_info['speed'], edge_info['distance'] , edge_info['retransmission'])
    return suma

def beam_search(graph, start, goal, beam, heuristic=heuristic):
    open_set = [start]
    closed_set = []
    counter = 0
    frames = []
    while open_set:
        print(f"open_set={open_set}")
        current_node = open_set.pop(0)
        current_node.color = 'red'

        current_frame = {
            'nodes': [(node.name, {'color': node.color, 'weight': node.heuristic_value, 'label': node.label}) for node in graph.nodes.values()],
            'edges': [(node1.name, node2.name, {'weight': weight['distance'], 'retr':weight['retransmission'], 'speed':weight['speed']}) for node1 in graph.nodes.values() for node2, weight in node1.neighbors.items()]
        }
        frames.append(current_frame)

        if current_node == goal:
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = current_node.parent
            return frames, path

        else:
            # Generate children of current_node
            for neighbor, edge_info in graph.nodes[current_node.name].neighbors.items():
                if neighbor not in open_set and neighbor not in closed_set:
                    neighbor.parent = current_node
                    neighbor.heuristic_value = heuristic(edge_info, current_node)
                    open_set.append(neighbor)
                elif neighbor in open_set:
                    if neighbor.heuristic_value > heuristic(edge_info, current_node):
                        print(f"Updating heuristic value of {neighbor} from {neighbor.heuristic_value} to {heuristic(edge_info, current_node)}")
                        neighbor.parent = current_node
                        neighbor.heuristic_value = heuristic(edge_info, current_node)
        closed_set.append(current_node)
        print(closed_set)
        print("\t",[(h, h.heuristic_value) for h in open_set])
        open_set.sort(key=lambda x: x.heuristic_value)
        print("\t",[(h, h.heuristic_value) for h in open_set])
        open_set = open_set[:beam]
        counter += 1
        print(f"{counter:>80}")
        # time.sleep(2)

    return frames, "FAIL"

if __name__=='__main__':
    node_a = Node(1, 'A')
    node_b = Node(2, 'B')
    node_c = Node(3, 'C')
    node_d = Node(4, 'D')
    node_e = Node(5, 'E')
    node_f = Node(6, 'F')
    node_g = Node(7, 'G')
    node_h = Node(8, 'H')
    node_i = Node(9, 'I')
    node_j = Node(10, 'J')
    # node_k = Node(11, 'K')
    # node_l = Node(12, 'L')
    
    graph = Graph()
    [graph.add_node(node) for node in [node_a, node_b, node_c, node_d, node_e, node_f, node_g, node_h, node_i, node_j]]
    
    graph.add_edge(node_a, node_b, speed=10, distance=50, retransmission=2)
    graph.add_edge(node_a, node_d, speed=100, distance=50, retransmission=1)
    graph.add_edge(node_b, node_c, speed=100, distance=5, retransmission=2)
    graph.add_edge(node_c, node_d, speed=100, distance=50, retransmission=20)
    graph.add_edge(node_d, node_e, speed=10, distance=50, retransmission=299)
    graph.add_edge(node_a, node_f, speed=1, distance=50, retransmission=2)
    graph.add_edge(node_f, node_g, speed=10, distance=5, retransmission=22)
    graph.add_edge(node_j, node_b, speed=10, distance=50, retransmission=2)
    graph.add_edge(node_h, node_i, speed=1, distance=500, retransmission=4)
    graph.add_edge(node_c, node_j, speed=10, distance=50, retransmission=2)
    start_node = node_a
    start_node.heuristic_value=0
    goal_node = node_j
    # path = beam_search(graph, start_node, goal_node, beam=2)
    frames, path = beam_search(graph, start_node, goal_node, beam=2)
    with open('frames.json', 'w') as f:
        json.dump(frames, f)
    
    print(frames)
