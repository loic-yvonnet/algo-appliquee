# Generate the diagrams for lecture 7

import matplotlib.pyplot as plt
import math

# Target folder
path = "/home/lyvonnet/Dev/algo-appliquee/cours/07-complexite/assets/"

# Data to plot
x = [i for i in range(1, 100000, 100)]
constant = [1 for _ in x]
logarithmique = [math.log10(i) for i in x]
lineaire = x
linearithmique = [i * math.log10(i) for i in x]
quadratique = [(i ** 2) for i in x]
cubique = [(i ** 3) for i in x]

def fig01_cst_log_lin():
    plt.figure("Constant, logarithmique, et linéaire", figsize=(12.5, 5))

    plt1 = plt.subplot(1, 2, 1)
    plt1.plot(x, constant, color="green", label="constant")
    plt1.plot(x, logarithmique, color="blue", label="logarithmique")
    plt.xlabel("Taille des entrées N")
    plt.ylabel("Temps")
    plt.legend()
    plt.title("$O(1)$ et $O(log N)$", fontsize="xx-large")

    plt2 = plt.subplot(1, 2, 2)
    plt2.plot(x, logarithmique, color="green", label="logarithmique")
    plt2.plot(x, lineaire, color="blue", label="linéaire")
    plt.xlabel("Taille des entrées N")
    plt.ylabel("Temps")
    plt.legend()
    plt.title("$O(\log N)$ et $O(N)$", fontsize="xx-large")

    plt.savefig(path + "fig01_cst_log_lin.png", transparent=True)

def fig02_lin_loglin_quad():
    plt.figure("Linéaire, linéarithmique, quadratique", figsize=(12.5, 5))

    plt1 = plt.subplot(1, 2, 1)
    plt1.plot(x, lineaire, color="green", label="linéaire")
    plt1.plot(x, linearithmique, color="blue", label="linéarithmique")
    plt.xlabel("Taille des entrées N")
    plt.ylabel("Temps")
    plt.legend()
    plt.title("$O(N)$ et $O(N \cdot \log N)$", fontsize="xx-large")

    plt2 = plt.subplot(1, 2, 2)
    plt2.plot(x, linearithmique, color="green", label="linéarithmique")
    plt2.plot(x, quadratique, color="blue", label="quadratique")
    plt.xlabel("Taille des entrées N")
    plt.ylabel("Temps")
    plt.legend()
    plt.title("$O(N \cdot \log N)$ et $O(N^2)$", fontsize="xx-large")

    plt.savefig(path + "fig02_lin_loglin_quad.png", transparent=True)

# Specific for exponential display
x_exp = [i for i in range(20)]
cubique_vs_exp = [(i ** 3) for i in x_exp]
exponentielle = [(2 ** i) for i in x_exp]

def fig03_quad_cub_exp():
    plt.figure("Quadratique, cubique, exponentielle", figsize=(12.5, 5))

    plt1 = plt.subplot(1, 2, 1)
    plt1.plot(x, quadratique, color="green", label="quadratique")
    plt1.plot(x, cubique, color="blue", label="cubique")
    plt.xlabel("Taille des entrées N")
    plt.ylabel("Temps")
    plt.legend()
    plt.title("$O(N^2)$ et $O(N^3)$", fontsize="xx-large")

    plt2 = plt.subplot(1, 2, 2)
    plt2.plot(x_exp, cubique_vs_exp, color="green", label="cubique")
    plt2.plot(x_exp, exponentielle, color="blue", label="exponentielle")
    plt.xlabel("Taille des entrées N")
    plt.ylabel("Temps")
    plt.legend()
    plt.title("$O(N^3)$ et $O(2^N)$", fontsize="xx-large")

    plt.savefig(path + "fig03_quad_cub_exp.png", transparent=True)


# All in one plot
all_x = [i for i in range(1, 50)]
all_logarithmique = [math.log10(i) for i in all_x]
all_lineaire = all_x
all_linearithmique = [i * math.log10(i) for i in all_x]
all_quadratique = [(i ** 2) for i in all_x]
all_cubique = [(i ** 3) for i in all_x]
all_x_exp = range(1, 20)
all_exponentielle = [(2 ** i) for i in all_x_exp]

def fig04_tous():
    plt.figure("Principales classes", figsize=(15, 5))

    plt.plot(all_x, all_logarithmique, color="green", label="logarithmique")
    plt.plot(all_x, all_lineaire, color="blue", label="linéaire")
    plt.plot(all_x, all_linearithmique, color="purple", label="linéarithmique")
    plt.plot(all_x, all_quadratique, color="yellow", label="quadratique")
    plt.plot(all_x, all_cubique, color="orange", label="cubique")
    plt.plot(all_x_exp, all_exponentielle, color="red", label="exponentielle")
    plt.xlabel("Taille des entrées N")
    plt.ylabel("Temps")
    plt.ylim(0, 2000)
    plt.legend()
    plt.title("Principales classes", fontsize="xx-large")

    plt.savefig(path + "fig04_tous.png", transparent=True)

def fig05_tous():
    plt.figure("Principales classes (zoom)", figsize=(15, 5))

    plt.plot(all_x, all_logarithmique, color="green", label="logarithmique")
    plt.plot(all_x, all_lineaire, color="blue", label="linéaire")
    plt.plot(all_x, all_linearithmique, color="purple", label="linéarithmique")
    plt.plot(all_x, all_quadratique, color="yellow", label="quadratique")
    plt.plot(all_x, all_cubique, color="orange", label="cubique")
    plt.plot(all_x_exp, all_exponentielle, color="red", label="exponentielle")
    plt.xlabel("Taille des entrées N")
    plt.ylabel("Temps")
    plt.ylim(0, 150)
    plt.legend()
    plt.title("Principales classes", fontsize="xx-large")

    plt.savefig(path + "fig05_tous.png", transparent=True)

def amdahl(s, p):
    return 1 / (1 - p + (p / s))

x_am = [(2 ** i) for i in range(12)]
amdahl_95 = [amdahl(i, 0.95) for i in x_am]
amdahl_90 = [amdahl(i, 0.90) for i in x_am]
amdahl_75 = [amdahl(i, 0.75) for i in x_am]
amdahl_50 = [amdahl(i, 0.50) for i in x_am]

def fix06_amdahl():
    plt.figure("Loi d'Amdahl", figsize=(12.5, 5))

    plt.plot(x_am, amdahl_95, color="green", label="p = 95%")
    plt.plot(x_am, amdahl_90, color="blue", label="p = 90%")
    plt.plot(x_am, amdahl_75, color="purple", label="p = 75%")
    plt.plot(x_am, amdahl_50, color="red", label="p = 50%")
    plt.xlabel("Nombre de processeurs")
    plt.ylabel("Accélération")
    plt.ylim(0, 25)
    plt.xscale("log")
    plt.legend()
    plt.title("Loi d'Amdahl", fontsize="xx-large")

    plt.savefig(path + "fix06_amdahl.png", transparent=True)


fig01_cst_log_lin()
fig02_lin_loglin_quad()
fig03_quad_cub_exp()
fig04_tous()
fig05_tous()
fix06_amdahl()