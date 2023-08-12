from skimage.io import imshow, imread, imsave

img = imread('img.png')

# вычленяю мин. и макс. значение из одномерного массива = матрица изображения, расстянутая в один ряд
# хотя можно все сделать и с помощью np.min/np.max
img_min, img_max = min(img.ravel()), max(img.ravel())

# подставляю в формулу
img = (img - img_min) * (255 / (img_max - img_min))
imsave('out_img.png', img.astype('uint8'))
