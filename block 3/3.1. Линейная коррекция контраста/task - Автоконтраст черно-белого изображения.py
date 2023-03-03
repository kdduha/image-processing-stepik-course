from skimage.io import imshow, imread, imsave
img = imread('img.png')
img_min, img_max = min(img.ravel()), max(img.ravel())
img = (img - img_min) * (255 / (img_max - img_min))
imsave('out_img.png', img.astype('uint8'))
