from skimage.io import imread, imsave

img = imread('img.png')
# находим стобец и колонку центра
row, col = img.shape[0]//2, img.shape[1]//2
# отступаем от центра на некоторый диапазон и берем срезы
img[row-3:row+4, col-7:col+8] = [255, 192, 203]
imsave('out_img.png', img)
