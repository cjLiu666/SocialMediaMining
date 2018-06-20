import networkx as nx
import matplotlib.pyplot as plt
import random

def smallWorld_graph(n, k, p):
    G = nx.Graph()
    nodes = list(range(n))
    
    for j in range(1, k // 2 + 1):
        targets = nodes[j:] + nodes[0:j]
        G.add_edges_from(zip(nodes, targets))
        
    for j in range(1, k // 2 + 1):  
        targets = nodes[j:] + nodes[0:j]  
        for u, v in zip(nodes, targets):
            if random.random() < p:
                w = random.choice(nodes)
                while w == u or G.has_edge(u, w):
                    w = random.choice(nodes)
                    if G.degree(u) >= n - 1:
                        break  
                else:
                    G.remove_edge(u, v)
                    G.add_edge(u, w)
    return G
    
    
    
#生成包含20个节点、每个节点4个近邻、随机化重连概率为0.2的小世界网络
WS = smallWorld_graph(20, 4, 0.2)

pos = nx.circular_layout(WS)          #定义一个布局，此处采用了circular布局方式
nx.draw(WS,pos,with_labels=False,node_size = 30)  #绘制图形

plt.show()
