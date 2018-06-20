import networkx as nx
import random
import itertools
import math


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


def setAttr(G, p):
    for i in range(G.number_of_nodes()):
        if random.random() < p/2:
            G.node[i]['Attr'] = 1.0
        elif random.random() < p:
            G.node[i]['Attr'] = 0.0
        else:
            G.node[i]['Attr'] = 0.5

    return G


def wvRN(G):
    flag = True
    while(flag):
        flag = False
        for i in range(G.number_of_nodes()):
            if G.node[i]['Attr'] != 0 and G.node[i]['Attr'] != 1:
                tmp = G.node[i]['Attr']
                total = 0.0
                nums = 0.0
                # faster to access the adjacency dictionary
                for v in G[i]:
                    total += G.node[v]['Attr']
                    nums += 1

                G.node[i]['Attr'] = total / nums

                if math.fabs(tmp - G.node[i]['Attr']) < 0.01:
                    G.node[i]['Attr'] = round(G.node[i]['Attr'])

        for i in range(G.number_of_nodes()):
            if G.node[i]['Attr'] != 0 and G.node[i]['Attr'] != 1:
                flag = True
                break

    return G


G = random_graph(100, 0.2)
G = setAttr(G, 0.5)
G = wvRN(G)
print("小数是已知的结果，预测的结果用整数来表示:")
for i in range(G.number_of_nodes()):
    print(i, ":", G.node[i]['Attr'])
