from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from matrix import format as frmt


def load(path):
    img = Image.open(path).convert("L")
    matrix = np.array(img)
    return matrix


def show(matrix):
    plt.imshow(matrix, cmap="gray")
    plt.colorbar()
    plt.show()


# Převod NumPy -> obyčejný Python list int
def numpy_to_list(matrix):
    return matrix.astype(int).tolist()


# Převod Python list -> NumPy
def list_to_numpy(my_list):
    return np.array(my_list, dtype=int)


# Hlavní program
matrix = load("C:\\Users\\mazl\\Desktop\\SPSMB-Python-2026\\cv07\\image.png")


my_list = numpy_to_list(matrix)

frmt(my_list)
