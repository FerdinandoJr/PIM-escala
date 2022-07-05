import numpy as np
import matplotlib.pyplot as plt
import imutils 
import cv2  
from matplotlib import pyplot as plt
import matplotlib.image as img 
from skimage.io import imread, imshow
from skimage.color import rgb2hsv, rgb2gray, rgb2yuv
from skimage import color, exposure, transform
from skimage.exposure import equalize_hist
import numpy as npy 
import math

path = '/content/drive/MyDrive/PIM/'
image = img.imread(path+"verticalBars.png")  

def scale(im, nR, nC=0):
    if(nC==0):
      nC=nR
    number_rows = len(im)     # source number of rows 
    number_columns = len(im[0])  # source number of columns 
    return [[ im[int(number_rows * r / nR)][int(number_columns * c / nC)]  
                 for c in range(nC)] for r in range(nR)]

def scale2(image, scale=1):
    w, h = image.shape[:2]; 
    xNew = int(w * scale); 
    yNew = int(h * scale); 
    xScale = xNew/(w-1); 
    yScale = yNew/(h-1); 
      
    newImage = npy.zeros([xNew, yNew, 4]); 
      
    for i in range(xNew-1): 
      for j in range(yNew-1): 
          newImage[i + 1, j + 1]= image[1 + int(i / xScale), 
                                    1 + int(j / yScale)] 
    img.imsave(f"/content/drive/MyDrive/PIM/scaled_{round(scale, 2)}.png", newImage); 


#im = plt.imread('filename.jpeg')

plt.imshow(image)
plt.show()

s = 1.2
for i in range(6):
  scale2(image,s)
  s += 0.2
