import networkx as nx 

G = nx.Graph()


def closenessCentrality(G):
    path_length = nx.single_source_shortest_path_length
    nodes = G.nodes()
    closeness_centrality = {}
    for n in nodes:
        sp = path_length(G, n)
        totsp = sum(sp.values())
        if totsp > 0.0 and len(G) > 1:
            closeness_centrality[n] = (len(sp)-1.0) / totsp
            # normalize to number of nodes-1 in connected part
            s = (len(sp)-1.0) / (len(G) - 1)
            closeness_centrality[n] *= s
        else:
            closeness_centrality[n] = 0.0
    
    return closeness_centrality


def topNBetweeness():
    score = closenessCentrality(G)
    score = sorted(score.items(), key=lambda item: item[1], reverse=True)
    print("closenessCentrality:", score)
    output = []
    for node in score:
        output.append(node[0])
    
    print(output)


def readNetwork(filename):
    fin = open(filename, 'r')

    rowCount = 1
    colCount = 1
    for line in fin.readlines():
        line = line.split(" ")
        for node in line:
            if node == '1':
                G.add_edge(rowCount, colCount)
            colCount += 1
        colCount = 1
        rowCount += 1

    print(G.edges())


readNetwork("input.data")
topNBetweeness()
