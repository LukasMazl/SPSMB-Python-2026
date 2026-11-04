from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def load(path):
    img = Image.open(path).convert("L")
    matrix = np.array(img)
    return matrix


def show(matrix):
    plt.imshow(matrix, cmap="gray")
    plt.colorbar()
    plt.show()


# Hlavní program
matrix = load("C:\\Users\\mazl\\Desktop\\SPSMB-Python-2026\\cv07\\image.png")
print(matrix)
show(matrix)