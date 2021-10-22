"""
Generate the images and animated gifs for the lecture 9.
"""

# Standard library
import os
import imageio

# External libraries
import matplotlib.pyplot as plt
import numpy as np

# Globals
dir_path = "/home/lyvonnet/Dev/algo-appliquee/dist/tmp/"

def gen_data():
    """Generate the list to be sorted"""
    max = 1000
    size = 100
    np.random.seed(0)
    y = [alpha.real for alpha in np.random.randint(max, size=size)]

    return y

def plot_data(y, id, series):
    x = [i for i in range(len(y))]
    
    alias = f"{series}-{id:04d}"
    path = os.path.join(dir_path, f"{alias}.png")
    
    plt.figure(alias, figsize=(4, 2.1))
    plt.axis("off")
    plt.stem(x, y, markerfmt=" ")
    plt.savefig(path, transparent=True)

def create_gif(series):
    file_paths = []
    for file_name in os.listdir(dir_path):
        if file_name.endswith(".png") and file_name.startswith(series):
            file_path = os.path.join(dir_path, file_name)
            file_paths.append(file_path)

    file_paths.sort()
    images = [imageio.imread(file_path) for file_path in file_paths]
    
    target = os.path.join(dir_path, f"{series}.gif")
    imageio.mimsave(target, images, fps=2)

def bubble_sort(y):
    count = 0
    a = y[:]
    plot_data(a, count, "tri-bulle")
    N = len(a)

    for i in range(N - 1):
        for j in range(N - (i + 1)):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

        count += 1
        plot_data(a, count, "tri-bulle")

    create_gif("tri-bulle")

    return a

def selection_sort(y):
    count = 0
    a = y[:]
    plot_data(a, count, "tri-selection")
    N = len(a)

    for i in range(N):
        min = i
        for j in range(i, N):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
        count += 1
        plot_data(a, count, "tri-selection")

    create_gif("tri-selection")

    return a

def insertion_sort(y):
    count = 0
    a = y[:]
    plot_data(a, count, "tri-insertion")
    N = len(a)

    for i in range(1, N):
        j = i
        while j > 0 and a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1
        
        count += 1
        plot_data(a, count, "tri-insertion")

    create_gif("tri-insertion")

    return a

def shell_sort(y):
    count = 0
    a = y[:]
    N = len(a)
    plot_data(a, count, "tri-coquille")
    h = 1
    filter = 0
    while h < N // 3:
        h = 3 * h + 1

    while h >= 1:
        for i in range(h, N):
            j = i
            while j >= h and a[j] < a[j-h]:
                a[j], a[j-h] = a[j-h], a[j]
                j -= h

            if filter == 0:
                count += 1
                plot_data(a, count, "tri-coquille")
            
            filter += 1
            if filter == 3:
                filter = 0
        h //= 3

    create_gif("tri-coquille")

    return a

def merge_sort(y):
    count = 0
    a = y[:]
    plot_data(a, count, "tri-fusion")
    N = len(a)

    def merge(a, debut, milieu, fin):
        i = debut
        j = milieu + 1

        auxiliaire = a[:]

        for k in range(debut, fin + 1):
            if i > milieu:
                a[k] = auxiliaire[j]
                j += 1
            elif j > fin:
                a[k] = auxiliaire[i]
                i += 1
            elif auxiliaire[j] < auxiliaire[i]:
                a[k] = auxiliaire[j]
                j += 1
            else:
                a[k] = auxiliaire[i]
                i += 1

        nonlocal count
        count += 1
        plot_data(a, count, "tri-fusion")

    def sort(a, debut, fin):
        if fin > debut:
            milieu = debut + (fin - debut) // 2
            sort(a, debut, milieu)
            sort(a, milieu + 1, fin)
            merge(a, debut, milieu, fin)
    
    sort(a, 0, N - 1)

    create_gif("tri-fusion")

    return a

def quick_sort(y):
    count = 0
    a = y[:]
    plot_data(a, count, "tri-rapide")
    N = len(a)

    def partition(a, debut, fin):
        i = debut
        j = fin + 1
        valeur = a[debut]

        while True:
            # Scan vers la droite
            i += 1
            while a[i] < valeur and i != fin:
                i += 1

            # Scan vers la gauche
            j -= 1
            while valeur < a[j] and j != debut:
                j -= 1

            # Si les indices se croisent on s'arrête
            if i >= j:
                break

            # Echange des éléments dans les 2 partitions
            a[j], a[i] = a[i], a[j]
        
        # Met la valeur de partitionnment entre les 2 partitions
        a[j], a[debut] = a[debut], a[j]

        nonlocal count
        count += 1
        plot_data(a, count, "tri-rapide")

        return j

    def sort(a, debut, fin):
        if fin > debut:
            j = partition(a, debut, fin)
            sort(a, debut, j - 1)
            sort(a, j + 1, fin)

    sort(a, 0, N - 1)

    create_gif("tri-rapide")

    return a

y = gen_data()
bubble_sort(y)
selection_sort(y)
insertion_sort(y)
shell_sort(y)
merge_sort(y)
quick_sort(y)