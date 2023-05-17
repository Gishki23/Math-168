from DataParser import Parser
import networkx as nx
import matplotlib.pyplot as plt


def CreateGraph():
    G = nx.Graph()
    Sim, Group = Parser("amazon-meta.txt")

    for ASIN in Group:
        G.add_node(ASIN)
    
    nx.set_node_attributes(G, Group, name="group")

    for ASIN in Sim:
        for prod in Sim[ASIN]:
            #uncomment below to remove unspecified items
            # if prod not in Sim:
            #     continue
            G.add_edge(ASIN, prod)

        
    return G

if __name__ == "__main__":
    #validate that this works
    G = CreateGraph()
    print(G.number_of_nodes())
    r = nx.degree_assortativity_coefficient(G)
    print(r)

