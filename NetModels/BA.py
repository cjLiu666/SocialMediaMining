import networkx as nx
import matplotlib.pyplot as plt
import itertools
import math
import random


def empty_graph(n):
    G=nx.Graph()
    G.add_nodes_from(range(n))
    return G


def random_subset(seq, m):
    targets = set()
    while len(targets) < m:
        x = random.choice(seq)
        targets.add(x)
    return targets


def baModel(n, m):
    G = empty_graph(m)
    targets = list(range(m))
    repeated_nodes = []
    source = m
    while source < n:
        G.add_edges_from(zip([source] * m, targets))  
        repeated_nodes.extend(targets)
        repeated_nodes.extend([source] * m)
        targets = random_subset(repeated_nodes, m)
        source += 1  
    return G

    
BA = baModel(20, 1)
pos = nx.spring_layout(BA)         
nx.draw(BA,pos,with_labels=False,node_size = 30)
plt.show()
