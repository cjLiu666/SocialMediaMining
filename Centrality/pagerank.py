import networkx as nx
import numpy as np


G = nx.Graph()


def Matrix(G, alpha=0.85, personalization=None, nodelist=None, weight='weight'):
    if personalization is None: 
        nodelist=G.nodes()
    else:  
        nodelist=personalization.keys()
    M=nx.to_numpy_matrix(G,nodelist=nodelist,weight=weight)
    (n,m)=M.shape 
    if n == 0:
        return M
    dangling=np.where(M.sum(axis=1)==0)
    for d in dangling[0]:
        M[d]=1.0/n
    M=M/M.sum(axis=1)
    e=np.ones((n))
    if personalization is not None:
        v=np.array(list(personalization.values()),dtype=float)
    else:
        v=e
    v=v/v.sum()
    P=alpha*M+(1-alpha)*np.outer(e,v)
    return P

def PageRank(G, alpha=0.85, personalization=None, weight='weight'):
    if personalization is None: 
        nodelist=G.nodes()
    else:  
        nodelist=personalization.keys()
    M = Matrix(G, alpha, personalization=personalization,
                    nodelist=nodelist, weight=weight)
    
    eigenvalues,eigenvectors=np.linalg.eig(M.T)
    ind=eigenvalues.argsort()
    largest=np.array(eigenvectors[:,ind[-1]]).flatten().real
    norm=float(largest.sum())
    centrality=dict(zip(nodelist,map(float,largest/norm)))
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
pagerank = PageRank(G, alpha = 0.3)
pagerank = sorted(pagerank.items(), key = lambda item:item[1], reverse = True)
print(pagerank)
