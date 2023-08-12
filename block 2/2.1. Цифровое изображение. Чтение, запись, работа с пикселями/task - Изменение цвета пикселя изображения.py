from skimage.io import imread, imshow, imsave

img = imread('img.png')
# центр находим за счет целочисленного деления пополам n-ой строки и m-ого столбца
img[img.shape[0]//2, img.shape[1]//2] = [102, 204, 102]
imsave('out_img.png', img)
