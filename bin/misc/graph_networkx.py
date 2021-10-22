"""
Dependencies:
```
python3.9 -m pip install networkx
```
"""
import random

import matplotlib.pyplot as plt
import networkx as nx

def tutorial():
    G = nx.Graph()

    G.add_node(1)
    G.add_nodes_from([2, 3])
    G.add_nodes_from([
        (4, {"color": "red"}),
        (5, {"color": "green"}),
    ])

    H = nx.path_graph(10)
    G.add_nodes_from(H)

    G.add_edge(1, 2)
    e = (2, 3)
    G.add_edge(*e)
    G.add_edges_from([(3, 4), (4, 5)])

    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()

def random_graph(nb_nodes=20, nb_edges=50):
    G = nx.Graph()

    G.add_nodes_from(list(range(nb_nodes)))
    
    alea = lambda: random.randint(0, nb_nodes)
    edges = [(alea(), alea()) for _ in range(nb_edges)]
    
    G.add_edges_from(edges)

    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()

def barabasi_albert_graph():
    G = nx.barabasi_albert_graph(100, 3, 42)

    options = {
        'node_size': 80,
        'width': 1
    }
    nx.draw(G, **options)
    plt.show()

def star_graph():
    G = nx.star_graph(20)

    options = {
        'width': 1
    }
    nx.draw(G, with_labels=True, **options)
    plt.show()

#random_graph()
#barabasi_albert_graph()
star_graph()