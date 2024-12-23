import networkx as nx

with open('data.txt') as f:
    data = f.read().split()

G = nx.Graph()
for connection in data:
    nodes = connection.split("-")
    G.add_edge(nodes[0], nodes[1])

print(",".join(sorted(sorted(list(nx.find_cliques(G)), key = lambda x: len(x))[-1])))