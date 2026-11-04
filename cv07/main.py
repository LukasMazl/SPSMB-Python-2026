from matrix import convolution
from view import load, numpy_to_list, list_to_numpy, show

if __name__ == "__main__":
    kernel = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    image = load("C:\\Users\\mazl\\Desktop\\SPSMB-Python-2026\\cv07\\image.png")
 
    img = numpy_to_list(image)
    new_img = convolution(img, kernel)
    np_img = list_to_numpy(new_img)
    show(np_img)

