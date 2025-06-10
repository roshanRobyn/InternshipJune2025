import os
import numpy as n
import imageio.v3 as io

def main():
    factor1=1.5
    factor2=0.5
    imageArray=io.imread("grayscale-v1.png")
    imageflt=imageArray.astype(n.float32)
    modarray=imageflt.copy()
    height,width,length=modarray.shape
    mid=256/2
    for row in range(height):
        for col in range(width):
            for col2 in range(length):
                currentpix=modarray[row][col][col2]
                if currentpix>mid:
                    modarray[row][col][col2]=modarray[row][col][col2]*factor1
                else:
                    modarray[row][col][col2]=modarray[row][col][col2]*factor2
    imageClipped=n.clip(modarray,0,255)
    imageUint=imageClipped.astype(n.uint8)
    io.imwrite("outputContrast.png",imageUint)


main()
