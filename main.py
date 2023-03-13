
import igraph as ig
from igraph import Graph
import networkx as nx
import sys

if __name__ == "__main__":
    var = sys.argv[1]
    G = nx.read_adjlist(var, nodetype=int)
    g = Graph.from_networkx(G)
    print(g.independence_number())