import os
import matplotlib.pyplot as plt
import numpy as np
import imageio

dir_path = "/home/lyvonnet/Dev/algo-appliquee/dist/"

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
    N = len(a)

    for i in range(N - 1):
        for j in range(N - (i + 1)):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

        count += 1
        plot_data(a, count, "bubble-sort")

    create_gif("bubble-sort")

    return a

def selection_sort(y):
    count = 0
    a = y[:]
    N = len(a)

    for i in range(N):
        min = i
        for j in range(i, N):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
        count += 1
        plot_data(a, count, "selection-sort")

    create_gif("selection-sort")

    return a

def insertion_sort(y):
    count = 0
    a = y[:]
    N = len(a)

    for i in range(1, N):
        j = i
        while j > 0 and a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1
        
        count += 1
        plot_data(a, count, "insertion-sort")

    create_gif("insertion-sort")

    return a

def shell_sort(y):
    count = 0
    a = y[:]
    N = len(a)
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
                plot_data(a, count, "shell-sort")
            
            filter += 1
            if filter == 3:
                filter = 0
        h //= 3

    create_gif("shell-sort")

    return a

def merge_sort(y):
    count = 0
    a = y[:]
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
        plot_data(a, count, "merge-sort")

    def sort(a, debut, fin):
        if fin > debut:
            milieu = debut + (fin - debut) // 2
            sort(a, debut, milieu)
            sort(a, milieu + 1, fin)
            merge(a, debut, milieu, fin)
    
    sort(a, 0, N - 1)

    create_gif("merge-sort")

    return a

y = gen_data()
bubble_sort(y)
selection_sort(y)
insertion_sort(y)
shell_sort(y)
merge_sort(y)