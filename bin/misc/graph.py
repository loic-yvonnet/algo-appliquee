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

def create_binary_tree(*args):
    """Create a binary tree from the list of arguments"""
    # Initialize a binary tree with the input list
    binary_tree = creer_arbre_binaire_avec_liste(args)
    
    # Initialize from a empty dot file with the right parameters
    G = pgv.AGraph(empty_dot_path)

    # Fill in the graph
    convertir_arbre_vers_graphviz(binary_tree, G)

    return G

def highlight_node(G, value):
    """Highlight in red the specified value."""
    G.get_node(value).attr["color"] = "red"
    G.get_node(value).attr["fontcolor"] = "red"

def resize_canvas(image_path, width, height):
    """Resize the image canvas (like Gimp > Set Image Canvas Size).

    The resulting image is centered at the top since the trees stick
    to the top of the images.
    """
    img = Image.open(image_path)
    old_width, old_height = img.size

    x = int(floor((width - old_width) / 2))
    y = 0
    transparent = (255, 255, 255, 0)

    blank_image = Image.new("RGBA", (width, height), transparent)
    blank_image.paste(img, (x, y, x + old_width, y + old_height))
    img.close()
    blank_image.save(image_path, optimize=False)
    blank_image.close()

def generate_gif_frame(image_path):
    """Generate a transparent gif frame.
    
    Source: https://stackoverflow.com/questions/46850318/transparent-background-in-gif-using-python-imageio
    """
    img = Image.open(image_path)
    alpha = img.getchannel('A')

    # Convert the image into P mode but only use 255 colors in the palette out of 256
    img = img.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)

    # Set all pixel values below 128 to 255 , and the rest to 0
    mask = Image.eval(alpha, lambda a: 255 if a <=128 else 0)

    # Paste the color of index 255 and use alpha as a mask
    img.paste(255, mask)

    # The transparency index is 255
    img.info['transparency'] = 255

    return img

def create_gif(images_paths):
    """Create a gif from a list of images paths."""
    images = [generate_gif_frame(img_path) for img_path in images_paths]
    first = images.pop(0)
    first.save('GIF.gif', save_all=True, append_images=images, loop=5, duration=200)

def illustrate_insertion_in_binary_tree():
    """Create a git to illustrate the insertion in a binary tree."""  
    # Closure variables for the flush_image internal function
    images_paths = []
    i = 0

    def flush_image(G):
        """Internal helper to create an intermediary image with the current 
        state of the graph."""
        nonlocal i, images_paths
        file_path = os.path.join(temp_dir, f"insert-binary-tree-{i}.png")
        images_paths.append(file_path)
        G.draw(file_path, prog="dot")
        i += 1

    def step(*args):
        """One step in the algorithm."""
        G = create_binary_tree(*args)
        highlight_node(G, args[len(args) - 1])
        flush_image(G)

    # Simulation steps
    step(42)
    step(42, 7)
    step(42, 7, 108)
    step(42, 7, 108, 21)
    step(42, 7, 108, 21, 1)
    step(42, 7, 108, 21, 1, 88)    
    step(42, 7, 108, 21, 1, 88, 128)
    step(42, 7, 108, 21, 1, 88, 128, 50)
    step(42, 7, 108, 21, 1, 88, 128, 50, 100)
    step(42, 7, 108, 21, 1, 88, 128, 50, 100, 0)
    step(42, 7, 108, 21, 1, 88, 128, 50, 100, 0, 25)
    step(42, 7, 108, 21, 1, 88, 128, 50, 100, 0, 25, 256)
    step(42, 7, 108, 21, 1, 88, 128, 50, 100, 0, 25, 256, 125)
    step(42, 7, 108, 21, 1, 88, 128, 50, 100, 0, 25, 256, 125, 3)
    step(42, 7, 108, 21, 1, 88, 128, 50, 100, 0, 25, 256, 125, 3, 15)

    # Get the largest dimensions
    images = [imageio.imread(file_path) for file_path in images_paths]
    shapes = [img.shape for img in images]
    max_height = max([shape[0] for shape in shapes])
    max_width = max([shape[1] for shape in shapes])

    # Resize the canvas of all images
    for image_path in images_paths:
        resize_canvas(image_path, max_width, max_height)

    # Create the gif
    create_gif(images_paths, "005-insertion-arbre-binaire.gif")

    # Optimize the gif size
    #optimize(target)
    
generate_png_from_dot()
create_temp_dir()
illustrate_insertion_in_binary_tree()