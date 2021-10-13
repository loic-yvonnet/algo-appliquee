"""
Generation of the graphs for the lecture 11.

PyGraphViz has a few system dependencies:
```
sudo apt-get install python3.9-dev
sudo apt-get install graphviz-dev
python3.9 -m pip install pygraphviz
```

Other dependency:
```
sudo apt-get install gifsicle
python3.9 -m pip install pygifsicle
```
"""
# Standard library
import os
import imageio
from PIL import Image
from math import floor

# External libraries
import pygraphviz as pgv
from pygifsicle import optimize

# Local libraries
import arbre_binaire as binary_tree
import arbre_rouge_noir as red_black_bst
import dfs_bfs as adj

# Globals
lecture_dir = "/home/lyvonnet/Dev/algo-appliquee/cours/11-graphes"
source_dir = f"{lecture_dir}/graphviz"
target_dir = f"{lecture_dir}/assets"
temp_dir = "/home/lyvonnet/Dev/algo-appliquee/dist/tmp/"
empty_dot_file_name = "000-vide.dot"
empty_dot_path = f"{source_dir}/{empty_dot_file_name}"
force_transparent = False # gifs are not generated if True

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

def init_empty_graph(splines=False):
    """Initialize from a empty dot file with the right parameters."""
    if force_transparent:
        return pgv.AGraph(empty_dot_path, bgcolor="transparent", splines=splines)
    else:
        return pgv.AGraph(empty_dot_path, splines=splines)

def create_binary_tree(*args):
    """Create a binary tree from the list of arguments"""
    # Initialize a binary tree with the input list
    tree = binary_tree.creer_arbre_binaire_avec_liste(args)
    
    # Initialize from a empty dot file with the right parameters
    G = init_empty_graph()

    # Fill in the graph
    binary_tree.convertir_arbre_vers_graphviz(tree, G)

    return G

def create_red_black_tree(*args):
    """Create a red-black tree from the list of arguments"""
    # Initialize a binary tree with the input list
    tree = red_black_bst.creer_arbre_rouge_noir_avec_liste(args)
    
    # Initialize from a empty dot file with the right parameters
    G = init_empty_graph()

    # Fill in the graph
    red_black_bst.convertir_arbre_vers_graphviz(tree, G)

    return G

def create_graph_from_adjacency_matrix(m):
    """Create a graph from an adjacency matrix."""  
    # Initialize from a empty dot file with the right parameters
    G = init_empty_graph(splines=True)

    # Fill in the graph
    adj.convertir_matrice_adjacence_vers_graphviz(m, G)

    return G

def highlight_node(G, value, color="red"):
    """Highlight the specified value."""
    G.get_node(value).attr["color"] = color
    G.get_node(value).attr["fontcolor"] = color

def resize_canvas_top(image_path, width, height, max_width=450):
    """Resize the image canvas (like Gimp > Set Image Canvas Size).

    The resulting image is centered at the top since the trees stick
    to the top of the images.
    """
    # Open the image whose canvas has to be resized
    img = Image.open(image_path)
    old_width, old_height = img.size

    # Compute the location of the image within the new canvas
    x = int(floor((width - old_width) / 2))
    y = 0

    # Choose a background color
    if force_transparent:
        background = (255, 255, 255, 0)
    else:
        background = (255, 255, 255, 255) # white

    # Create a blank image with the right dimensions
    blank_image = Image.new("RGBA", (width, height), background)

    # Paste the input image at the right location
    blank_image.paste(img, (x, y, x + old_width, y + old_height))
    img.close()
    
    # Minimize the size of the image
    if width > max_width:
        ratio = max_width / width
        new_height = floor(height * ratio)
        blank_image = blank_image.resize((max_width, new_height), Image.BICUBIC)

    # Save the result (overwrite the input image)
    blank_image.save(image_path)
    blank_image.close()

def resize_to_top_and_create_gif(images_paths, target):
    """Resize the input images and create an animated gif from them."""
    # Get the largest dimensions
    images = [imageio.imread(file_path) for file_path in images_paths]
    shapes = [img.shape for img in images]
    max_height = max([shape[0] for shape in shapes])
    max_width = max([shape[1] for shape in shapes])

    # Resize the canvas of all images
    for image_path in images_paths:
        resize_canvas_top(image_path, max_width, max_height)

    # Transparent gif does not work well so we skip it in this case
    if not force_transparent:
        # Create the gif
        images = [imageio.imread(file_path) for file_path in images_paths]
        target = os.path.join(target_dir, target)
        imageio.mimsave(target, images, fps=0.75)

        # Optimize the gif size
        optimize(target)

def flush_image(G, basename, images_paths):
    """Internal helper to create an intermediary image with the current 
    state of the graph."""
    i = len(images_paths)
    file_path = os.path.join(temp_dir, f"{basename}-{i}.png")
    images_paths.append(file_path)
    G.draw(file_path, prog="dot")

def illustrate_search_in_binary_tree():
    """Create a gif to illustrate the search in a binary tree."""
    images_paths = []

    def step(highligth_value):
        """One step in the algorithm."""
        nonlocal images_paths
        G = create_binary_tree(42, 7, 108, 21, 1, 88, 128, 50, 
                               100, 0, 25, 256, 125, 2, 15)
        highlight_node(G, highligth_value)
        flush_image(G, "search-binary-tree", images_paths)

    # Simulation steps
    step(42)
    step(7)
    step(21)
    step(25)

    resize_to_top_and_create_gif(images_paths, "005-recherche-arbre-binaire.gif")

def illustrate_insertion_in_binary_tree():
    """Create a gif to illustrate the insertion in a binary tree."""  
    images_paths = []

    def step(nodes, new_value):
        """One step in the algorithm."""
        nonlocal images_paths
        nodes.append(new_value)
        G = create_binary_tree(*nodes)
        highlight_node(G, nodes[len(nodes) - 1])
        flush_image(G, "insert-binary-tree", images_paths)

    # Simulation steps
    nodes = []
    step(nodes, 42)
    step(nodes, 7)
    step(nodes, 108)
    step(nodes, 21)
    step(nodes, 1)
    step(nodes, 88)
    step(nodes, 128)
    step(nodes, 50)
    step(nodes, 100)
    step(nodes, 0)
    step(nodes, 25)
    step(nodes, 256)
    step(nodes, 125)
    step(nodes, 3)
    step(nodes, 15)

    resize_to_top_and_create_gif(images_paths, "007-insertion-arbre-binaire.gif")

def illustrate_unbalanced_binary_tree():
    """Create a gif to illustrate a unbalanced binary tree."""  
    images_paths = []

    def step(nodes, new_value):
        """One step in the algorithm."""
        nonlocal images_paths
        nodes.append(new_value)
        G = create_binary_tree(*nodes)
        highlight_node(G, nodes[len(nodes) - 1])
        flush_image(G, "unbalanced-tree", images_paths)

    # Simulation steps
    nodes = []
    step(nodes, 0)
    step(nodes, 1)
    step(nodes, 3)
    step(nodes, 7)
    step(nodes, 15)
    step(nodes, 21)
    step(nodes, 25)

    resize_to_top_and_create_gif(images_paths, "009-arbre-binaire-non-equilibre.gif")

def illustrate_balanced_red_black_binary_tree():
    """Create a gif to illustrate a balanced red-black binary search tree."""  
    images_paths = []

    def step(nodes, new_value):
        """One step in the algorithm."""
        nonlocal images_paths
        nodes.append(new_value)
        G = create_red_black_tree(*nodes)
        highlight_node(G, new_value)
        flush_image(G, "balanced-tree", images_paths)

    # Simulation steps
    nodes = []
    step(nodes, 0)
    step(nodes, 1)
    step(nodes, 3)
    step(nodes, 7)
    step(nodes, 15)
    step(nodes, 21)
    step(nodes, 25)
    step(nodes, 42)
    step(nodes, 50)
    step(nodes, 88)
    step(nodes, 100)
    step(nodes, 108)
    step(nodes, 125)
    step(nodes, 128)
    step(nodes, 256)

    resize_to_top_and_create_gif(images_paths, "011-arbre-rouge-noir.gif")

def init_adjacency_matrix_with_a_tree():
    M = [
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # s0
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], # s1
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], # s2
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0], # s3
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], # s4
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # s5
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # s6
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], # s7
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # s8
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # s9
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # s10
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # s11
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # s12
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # s13
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # s14
    ]

    return M, create_graph_from_adjacency_matrix(M)

def init_adjacency_matrix_with_a_simple_graph():
    M = [
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    return M, create_graph_from_adjacency_matrix(M)

def init_adjacency_matrix_with_a_graph():
    M = [
        #0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 0
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 1
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 2
        [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 3
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], # 4
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], # 5
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 6
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0], # 7
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 8
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 9
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], # 10
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 11
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], # 12
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], # 13
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 14
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], # 15
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], # 16
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], # 17
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 18
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]  # 19
        #0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
    ]

    return M, create_graph_from_adjacency_matrix(M)

def illustrate_dfs_in_tree():
    """Create a gif to illustrate depth-first search in a tree."""
    images_paths = []
    M, G = init_adjacency_matrix_with_a_tree()

    def step(highligth_value):
        """One step in the algorithm."""
        nonlocal images_paths, G
        highlight_node(G, highligth_value, "red")
        flush_image(G, "dfs-tree", images_paths)
        highlight_node(G, highligth_value, "green")

    # Simulation steps
    adj.parcours_en_profondeur(M, step)
    flush_image(G, "dfs-tree", images_paths)

    resize_to_top_and_create_gif(images_paths, "043-dfs-arbre.gif")

def illustrate_dfs_in_simple_graph():
    """Create a gif to illustrate depth-first search in a graph."""
    images_paths = []
    M, G = init_adjacency_matrix_with_a_simple_graph()

    def step(highligth_value):
        """One step in the algorithm."""
        nonlocal images_paths, G
        highlight_node(G, highligth_value, "red")
        flush_image(G, "dfs-simple-graph", images_paths)
        highlight_node(G, highligth_value, "green")

    # Simulation steps
    adj.parcours_en_profondeur(M, step)
    flush_image(G, "dfs-simple-graph", images_paths)

    resize_to_top_and_create_gif(images_paths, "044-dfs-simple-graphe.gif")

def illustrate_dfs_in_graph():
    """Create a gif to illustrate depth-first search in a graph."""
    images_paths = []
    M, G = init_adjacency_matrix_with_a_graph()

    def step(highligth_value):
        """One step in the algorithm."""
        nonlocal images_paths, G
        highlight_node(G, highligth_value, "red")
        flush_image(G, "dfs-graph", images_paths)
        highlight_node(G, highligth_value, "green")

    # Simulation steps
    adj.parcours_en_profondeur(M, step)
    flush_image(G, "dfs-graph", images_paths)

    resize_to_top_and_create_gif(images_paths, "045-dfs-graphe.gif")

def illustrate_bfs_in_tree():
    """Create a gif to illustrate breadth-first search in a tree."""
    images_paths = []
    M, G = init_adjacency_matrix_with_a_tree()

    def step(highligth_value):
        """One step in the algorithm."""
        nonlocal images_paths, G
        highlight_node(G, highligth_value, "red")
        flush_image(G, "bfs-tree", images_paths)
        highlight_node(G, highligth_value, "green")

    # Simulation steps
    adj.parcours_en_largeur(M, step)
    flush_image(G, "bfs-tree", images_paths)

    resize_to_top_and_create_gif(images_paths, "046-bfs-arbre.gif")

def illustrate_bfs_in_simple_graph():
    """Create a gif to illustrate breadth-first search in a graph."""
    images_paths = []
    M, G = init_adjacency_matrix_with_a_simple_graph()

    def step(highligth_value):
        """One step in the algorithm."""
        nonlocal images_paths, G
        highlight_node(G, highligth_value, "red")
        flush_image(G, "bfs-simple-graph", images_paths)
        highlight_node(G, highligth_value, "green")

    # Simulation steps
    adj.parcours_en_largeur(M, step)
    flush_image(G, "bfs-simple-graph", images_paths)

    resize_to_top_and_create_gif(images_paths, "047-bfs-simple-graphe.gif")

def illustrate_bfs_in_graph():
    """Create a gif to illustrate breadth-first search in a graph."""
    images_paths = []
    M, G = init_adjacency_matrix_with_a_graph()

    def step(highligth_value):
        """One step in the algorithm."""
        nonlocal images_paths, G
        highlight_node(G, highligth_value, "red")
        flush_image(G, "bfs-graph", images_paths)
        highlight_node(G, highligth_value, "green")

    # Simulation steps
    adj.parcours_en_largeur(M, step)
    flush_image(G, "bfs-graph", images_paths)

    resize_to_top_and_create_gif(images_paths, "048-bfs-graphe.gif")

def main():
    generate_png_from_dot()
    create_temp_dir()
    illustrate_search_in_binary_tree()
    illustrate_insertion_in_binary_tree()
    illustrate_unbalanced_binary_tree()
    illustrate_balanced_red_black_binary_tree()
    illustrate_dfs_in_tree()
    illustrate_dfs_in_simple_graph()
    illustrate_dfs_in_graph()
    illustrate_bfs_in_tree()
    illustrate_bfs_in_simple_graph()
    illustrate_bfs_in_graph()

if __name__ == "__main__":
    main()