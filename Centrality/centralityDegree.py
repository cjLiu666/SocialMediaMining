import networkx as nx

G = nx.Graph()

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

def centralityDegree(G):
    centrality = {}
    s = 1.0 / (len(G) - 1.0)
    centrality = {n : d * s for n, d in G.degree()}

    centrality = sorted(centrality.items(), key = lambda item:item[1], reverse = True)
    print(centrality)
    
readNetWork("input.data")
centralityDegree(G)
