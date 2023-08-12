from skimage.io import imread, imsave
from skimage import img_as_float

# переводим во float для удобства (можно и с int)
# инвертируем значения поэлементно (numpy массивы так умеют), вычитывая -1 из всех чисел из диапазона [0; 1]
# избавляемся от минуса по модулю
imsave('out_img.png', abs(img_as_float(imread('img.png')) - 1))
