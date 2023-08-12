from skimage.io import imread, imsave
from skimage import img_as_float, img_as_ubyte
import numpy as np

img = img_as_float(imread('img.png'))
r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]    # пункты 1-2

y = 0.2126*r + 0.7152*g + 0.0722*b
u = -0.0999*r - 0.3360*g + 0.4360*b
v = 0.6150*r - 0.5586*g - 0.0563*b   

# вспомогательное k-значение для отбрасывания 5% всех пикселей
# значения отбрасываю от одномерного отсортированного списка всех значений канала
k, y_list = round(y.size * 0.05), sorted(y.ravel())   # пункт 3
y_min, y_max = y_list[k], y_list[-k-1]

y = np.clip((y - y_min)/(y_max - y_min), 0., 1.)      # пункт 4 (линейное растяжение) и сразу 5
r = y + 1.2803*v                                      # перевод каналов опять - пункт 6
g = y - 0.2148*u - 0.3805*v
b = y + 2.1279*u
img = np.clip(np.dstack((r, g, b)), 0., 1.)           # собираем каналы и обрезаем - пункт 7

imsave('out_img.png', img_as_ubyte(img))              # сохранение и возвращение к ubyte - пункт 8
