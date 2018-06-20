import networkx as nx
import scipy as sp
from scipy.sparse import linalg

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

    

def centralityEigenvector(G, max_iter=50, tol=0):
    M = nx.to_scipy_sparse_matrix(G, nodelist = list(G), weight = None,
                                  dtype=float)
    eigenvalue, eigenvector = linalg.eigs(M.T, k=1, which='LR',
                                          maxiter=max_iter, tol=tol)
    largest = eigenvector.flatten().real
    norm = sp.sign(largest.sum()) * sp.linalg.norm(largest)
    return dict(zip(G, largest / norm))
                    

                                       
                                
readNetWork("input.data")
eigenvector = centralityEigenvector(G)
eigenvector = sorted(eigenvector.items(), key = lambda item:item[1], reverse = True)
print(eigenvector)
