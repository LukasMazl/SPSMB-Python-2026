from matrix import convolution, plus
from view import load, numpy_to_list, list_to_numpy, show

if __name__ == "__main__":
    kernel_1 = [
        [1, 0, -1],
        [1, 0, -1],
        [1, 0, -1]
    ]

    kernel_2 = [
        [1, 1, 1],
        [0, 0, 0],
        [-1, -1, -1]
    ]

    bluer_kernel = [
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9]
    ]

    sharpening_kernel = [
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ]

    emboss_kernel = [
    [-2, -1,  0,  1,  2],
    [-1, -1,  0,  1,  1],
    [ 0,  0,  1,  0,  0],
    [ 1,  1,  0, -1, -1],
    [ 2,  1,  0, -1, -2]
]
    laplacian_kernel = [
    [ 0,  0, -1,  0,  0],
    [ 0, -1, -2, -1,  0],
    [-1, -2, 12, -2, -1],
    [ 0, -1, -2, -1,  0],
    [ 0,  0, -1,  0,  0]
]
    
    gaussian_kernel = [
    [1,  4,  6,  4,  1],
    [4, 16, 24, 16,  4],
    [6, 24, 36, 24,  6],
    [4, 16, 24, 16,  4],
    [1,  4,  6,  4,  1]
]

    image = load("C:\\Users\\mazl\\Desktop\\SPSMB-Python-2026\\cv07\\image.png")
 
    img = numpy_to_list(image)
    #new_img = convolution(img, sharpening_kernel)
    #new_img_2 = convolution(img, kernel_2)
    #new_img_3 = convolution(img, kernel_1)
    #result = plus(new_img, new_img_2)
    #result = plus(result, new_img_3)
    result = convolution(img, laplacian_kernel)
    np_img = list_to_numpy(result)
    show(np_img)

