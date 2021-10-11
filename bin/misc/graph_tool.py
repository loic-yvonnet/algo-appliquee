"""
Dependencies:
```
# Cairo
sudo apt-get install libcairo2
sudo apt-get install python3-cairo
sudo apt-get install libcairo2-dev pkg-config python3-dev
python3.9 -m pip install pycairo

# graph-tool
sudo apt-key adv --keyserver keys.openpgp.org --recv-key 612DEFB798507F25
sudo echo "" >> /etc/apt/sources.list
sudo echo "For graph-tool" >> /etc/apt/sources.list
sudo echo "deb [ arch=amd64 ] https://downloads.skewed.de/apt bionic main" >> /etc/apt/sources.list
sudo apt-get update
sudo apt-get install python3-graph-tool
```
"""


from graph_tool.all import *
from graph_tool.draw import *

g = Graph()

v1 = g.add_vertex()
v2 = g.add_vertex()

e = g.add_edge(v1, v2)

graph_draw(g, vertex_text=g.vertex_index, output="two-nodes.png")