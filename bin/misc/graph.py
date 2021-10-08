"""
Generation of the graphs for the lecture 11.

PyGraphViz has a few system dependencies:
```
sudo apt-get install python3.9-dev
sudo apt-get install graphviz-dev
python3.9 -m pip install pygraphviz
```
"""
# Standard library
import os
import imageio

# External libraries
import pygraphviz as pgv

# Local libraries
from arbre_binaire import *

# Globals
lecture_dir = "/home/lyvonnet/Dev/algo-appliquee/cours/11-graphes"
source_dir = f"{lecture_dir}/graphviz"
target_dir = f"{lecture_dir}/assets"
temp_dir = "/home/lyvonnet/Dev/algo-appliquee/dist/tmp/"
empty_dot_file_name = "000-vide.dot"
empty_dot_path = f"{source_dir}/{empty_dot_file_name}"

def generate_png_from_dot():
    """Generate the png files from the dot files in target directory."""
    for file_name in os.listdir(source_dir):
        if file_name.endswith(".dot") and file_name != empty_dot_file_name:
            file_path = os.path.join(source_dir, file_name)
            G = pgv.AGraph(file_path)

            target_file_name = file_name.replace(".dot", ".png")
            target_file_path = os.path.join(target_dir, target_file_name)
            G.draw(target_file_path, prog="dot")

def create_temp_dir():
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)

def illustrate_insertion_in_binary_tree():
    """Create a git to illustrate the insertion in a binary tree."""
    # Initialize from a empty dot file with the right parameters
    G = pgv.AGraph(empty_dot_path)

    # Closure variables for the flush_image internal function
    images = []
    i = 0

    def flush_image():
        """Internal helper to create an intermediary image with the current 
        state of the graph."""
        nonlocal G, i, images
        file_path = os.path.join(temp_dir, f"insert-binary-tree-{i}.png")
        images.append(file_path)
        G.draw(file_path, prog="dot")
        i += 1

    def insert_node(new_node, parent_node):
        """Insert new_node under parent_node."""
        nonlocal G
        G.add_node(new_node, color="red", fontcolor="red", shape="circle")
        G.add_edge(parent_node, new_node)
        flush_image()
        G.get_node(new_node).attr["color"] = "black"
        G.get_node(new_node).attr["fontcolor"] = "black"

    # Root node: 42
    G.add_node(42, color="red", fontcolor="red", shape="circle")
    flush_image()
    G.get_node(42).attr["color"] = "black"
    G.get_node(42).attr["fontcolor"] = "black"

    # Insert 7, 108, 21, 1, 88, 128
    insert_node(7, 42)
    insert_node(108, 42)
    insert_node(21, 7)
    insert_node(1, 7)
    insert_node(88, 108)
    insert_node(128, 108)


generate_png_from_dot()
create_temp_dir()
illustrate_insertion_in_binary_tree()