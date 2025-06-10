import os
import numpy as n
import imageio.v3 as io

def main():
    image_array=io.imread("grayscale-v1.png")
    moddedflt=image_array.astype(n.float32)
    length,width,height=moddedflt.shape
    for i in range(length):
        for j in range(width):
            for k in range(height):
                moddedflt[i][j][k]=255-moddedflt[i][j][k]
    imageUint=moddedflt.astype(n.uint8)
    io.imwrite("outputINVERTED.png",imageUint)

main()

