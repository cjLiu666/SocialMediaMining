import networkx as nx
import itertools
import random
import matplotlib.pyplot as plt


def random_graph(n, p):
    G = nx.Graph()
    G.add_nodes_from(range(n))
    if p < 0:
        return G
    if p > 1:
        return nx.complete_graph(n, create_using=G)
    edges = itertools.combinations(range(n), 2)
    for e in edges:
        if random.random() < p:
            G.add_edge(*e)
    return G


ER = random_graph(15, 0.2)

pos = nx.shell_layout(ER)
nx.draw(ER, pos, with_labels=False, node_size=30)
plt.show()
