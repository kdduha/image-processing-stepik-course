from skimage.io import imshow, imread, imsave
from skimage import img_as_float
import numpy as np


def align(img, g_coord):
    
    img = img_as_float(img)
    
    dif= img.shape[0]//3    # делим img на 3 части
    b, g, r = img[:dif, :], img[dif:dif*2, :], img[dif*2:dif*3, :]
    # из-за округления в r лучше делать срез по строкам не до конца (иначе будут разные размеры в пиксель)
    
    height, witdh = int(dif * 0.1), int(img.shape[1] * 0.1)    # у меня тесты прошли с 10% процентами, а не с 5%
    r, g, b = r[height:1-height, witdh:1-witdh], g[height:1-height, witdh:1-witdh], b[height:1-height, witdh:1-witdh]  # обрезаем края на определенный процент 
    
    best_correlation_blue, best_correlation_red = 0, 0    
    for i in range(-15, 16):        # диапазон в +-15px из условия, i - строки, j - колонки
        for j in range(-15, 16):
            shift_blue = np.roll(np.roll(b, i, 0), j, 1) # двойным циклом сдвигаем картинку 
            correlation_blue = (shift_blue * g).sum()    # считаем значение корреляции (похожость картинок)
            if correlation_blue > best_correlation_blue:    # находим наибольшую корреляцию
                best_correlation_blue = correlation_blue
                best_blue = (i, j)                          
                # фиксируем соотвествующие координаты (строки, столбики)
            shift_red = np.roll(np.roll(r, i, 0), j, 1)
            correlation_red = (shift_red * g).sum()
            if correlation_red > best_correlation_red:
                best_correlation_red = correlation_red
                best_red = (i, j)
                
    # пробую соединить все каналы использовав сдвиги по оптимальным координатам         
    # new_r = np.roll(np.roll(r, best_red[0], 0), best_red[1], 1)
    # new_b = np.roll(np.roll(b, best_blue[0], 0), best_blue[1], 1)
    # new_img = dstack((new_r, g, new_b))
    
    row, col = g_coord
    return (row - best_blue[0] - dif, col - best_blue[1]), (dif + row - best_red[0], col - best_red[1])
    # координаты выводятся в изначальной картинке, не забываем учесть dif и наше деление картинки на 3 части
