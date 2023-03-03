from skimage.io import imread, imsave

img = imread('img.png')
img[img.shape[0]//2-3:img.shape[0]//2+4, img.shape[1]//2-7:img.shape[1]//2+8] = [255, 192, 203]
imsave('out_img.png', img)
