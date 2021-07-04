""" Compress and resize a folder of png images to a folder of jpeg images.
    Usage: python3.9 bin/compressimg.py 
                     --input=./cours/01-intro-programmation/work-assignment-01/steps
                     --output=./cours/01-intro-programmation/work-assignment-01/distrib
"""

import os
import click
import numpy as np
from skimage import io, color, transform

MAX_HEIGHT=600
MAX_WIDTH=800
JPEG_QUALITY=75

def get_target_filenames(files):
    filenames_no_ext = [ os.path.splitext(file)[0] for file in files ]
    target_files = [ file + ".jpeg" for file in filenames_no_ext ]
    return target_files

def process_one_file(input_dir, input_file, output_dir, output_file):
    full_input_path = os.path.join(input_dir, input_file)
    image = io.imread(full_input_path).astype(np.uint8)
    height, width, _ = image.shape
    print(f"height: {height}; width: {width}")
    
    if width > MAX_WIDTH:
        scale = MAX_WIDTH / width
        height = round(height * scale)
        width = MAX_WIDTH
        print(f"width-rescaled: {scale}")
        image = transform.resize(image, (height, width), anti_aliasing=True)
    elif height > MAX_HEIGHT:
        scale = MAX_HEIGHT / height
        height = MAX_HEIGHT
        width = round(width * scale)
        print(f"height-rescaled: {scale}")
        image = transform.resize(image, (height, width), anti_aliasing=True)

    image = image[:,:,:3]
    full_output_path = os.path.join(output_dir, output_file)
    io.imsave(full_output_path, image, "imageio", quality=JPEG_QUALITY)

@click.command()
@click.option("--input",
              prompt="Input folder",
              help="Folder containing input images to compress")
@click.option("--output",
              prompt="Output folder",
              help="Folder that should be empty and will contain the compressed images")
def compress(input, output):
    """ Compress the image files in the input directory as jpeg
    images to the output directory
    """
    if not os.path.isdir(output):
        os.mkdir(output)

    files = os.listdir(input)
    files.sort()
    target_files = get_target_filenames(files)

    for input_file, target_file in zip(files, target_files):
        print(input_file + "...")
        process_one_file(input, input_file, output, target_file)

    print("Done")

if __name__ == "__main__":
    compress()