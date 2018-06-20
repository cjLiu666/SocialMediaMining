import networkx as nx
import numpy as np


G = nx.Graph()

def centralityKatz(G, alpha = 0.1, beta = 1.0):
    try:
        nodelist = beta.keys()
        b = np.array(list(beta.values(), dtype = float))
    except AttributeError:
        nodelist = list(G)
        b = np.ones((len(nodelist), 1)) * float(beta)
      
    A = nx.adj_matrix(G, nodelist=nodelist, weight= None).todense().T
    n = A.shape[0]
    centrality = np.linalg.solve(np.eye(n, n) - (alpha * A), b)
    norm = np.sign(sum(centrality)) * np.linalg.norm(centrality)
    centrality = dict(zip(nodelist, map(float, centrality / norm)))
    return centrality



def readNetWork(filename):
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

readNetWork("input.data")
Katzeigenvector = centralityKatz(G, alpha = 0.3, beta = 0.3)
Katzeigenvector = sorted(Katzeigenvector.items(), key = lambda item:item[1], reverse = True)
print(Katzeigenvector)
    
    

