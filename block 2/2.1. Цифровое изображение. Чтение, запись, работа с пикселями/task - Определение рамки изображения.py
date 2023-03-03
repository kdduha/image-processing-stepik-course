import numpy as np
from skimage.io import imread

def borders(img, n, el=True, ind=1):                # 1: rows, 0: columns
    slices = img[n, :] if el else img[:, n]         # making slices depended on rows/columns   
    while np.all(slices == img[0, 0]):              # comparing slices' color with the 1-st pixel
        n += ind
        slices = img[n, :] if el else img[:, n]    # updating slices with new N
    return n

img = imread('img.png')
print(borders(img, 0, el=False), 
      borders(img, 0), 
      img.shape[1]-1 - borders(img, img.shape[1]-1, el=False, ind=-1), 
      img.shape[0]-1 - borders(img, img.shape[0]-1, ind=-1))
