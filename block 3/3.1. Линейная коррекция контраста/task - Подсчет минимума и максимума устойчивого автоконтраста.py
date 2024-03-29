from skimage.io import imread

# чтобы отбросить 5% всех значений, вытягиваю в одномерный массив всю матрицу изображения и сортирую
pixels = sorted(imread('img.png').ravel())

# получаем число отбрасываемых пикселей
k = round(len(pixels) * 0.05)

# min и max для ответа будут границы последовательности значений изображения 
# с поправкой на обратную сторону (верхний предел) и невключение элемента
# т.к. отриц.индексы начиинаются с -1, а не с 0
print(pixels[k], pixels[-k-1])
