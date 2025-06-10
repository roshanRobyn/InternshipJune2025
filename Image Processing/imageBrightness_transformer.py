import os
import imageio.v3 as io 
import numpy as n

def main():
    factor=1.5
    imagemat=io.imread("grayscale-v1.png")
    imageflt=imagemat.astype(n.float32)
    brightenedflt=imageflt * factor
    brightenedclipped=n.clip(brightenedflt,0,255)
    brightenedimage=brightenedclipped.astype(n.uint8)
    io.imwrite("output.png",brightenedimage)
    print("donee")

main()
