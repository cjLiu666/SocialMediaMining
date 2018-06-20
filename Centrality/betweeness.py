import networkx as nx
from heapq import heappush, heappop
from itertools import count
import random
G = nx.Graph()

def readNetwork(filename):
    fin = open(filename, 'r')

    rowCount = 1;
    colCount = 1;
    for line in fin.readlines():
        line = line.split(" ")
        for node in line:
            if node == '1':
                G.add_edge(rowCount, colCount)
            colCount += 1
        colCount = 1
        rowCount += 1

    print(G.edges())


def centralityBetweenness(G, k=None, normalized=True):
    betweenness = dict.fromkeys(G, 0.0)  
    nodes = G
    
    for s in nodes:
        S, P, sigma = _single_source_shortest_path(G, s)
        betweenness = _accumulate(betweenness, S, P, sigma, s)
    
    betweenness = _rescale(betweenness, len(G), normalized=normalized)
    return betweenness


def _single_source_shortest_path(G, s):
    S = []
    P = {}
    for v in G:
        P[v] = []
    sigma = dict.fromkeys(G, 0.0)    # sigma[v]=0 for v in G
    D = {}
    sigma[s] = 1.0
    D[s] = 0
    Q = [s]
    while Q:   # use BFS to find shortest paths
        v = Q.pop(0)
        S.append(v)
        Dv = D[v]
        sigmav = sigma[v]
        for w in G[v]:
            if w not in D:
                Q.append(w)
                D[w] = Dv + 1
            if D[w] == Dv + 1:   # this is a shortest path, count paths
                sigma[w] += sigmav
                P[w].append(v)  # predecessors
    return S, P, sigma



def _accumulate(betweenness, S, P, sigma, s):
    delta = dict.fromkeys(S, 0)
    while S:
        w = S.pop()
        coeff = (1.0 + delta[w]) / sigma[w]
        for v in P[w]:
            delta[v] += sigma[v] * coeff
        if w != s:
            betweenness[w] += delta[w]
    return betweenness


def _rescale(betweenness, n, normalized, directed=False):
    if normalized:
        if n <= 2:
            scale = None  # no normalization b=0 for all nodes
        else:
            scale = 1.0 / ((n - 1) * (n - 2))
    else:  
        scale = 0.5
        
    if scale is not None:
        for v in betweenness:
            betweenness[v] *= scale
    return betweenness


def topNBetweeness():
    score = centralityBetweenness(G)
    score = sorted(score.items(), key = lambda item:item[1], reverse = True)
    print("betweenness_centrality:", score)
    output = []
    for node in score:
        output.append(node[0])
    
    print(output)

readNetwork("input.data")
topNBetweeness()
