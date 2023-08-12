from skimage.io import imread, imshow, imsave

img = imread('img.png')
# выводим кол-во колонок матрицы (второй элемент кортежа shape=(n-строк, m-столбцов)
print(img.shape[1])
