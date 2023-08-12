from skimage.io import imread, imsave
from skimage.transform import integral_image, integrate


# пошел решать в лоб по всем блокам интегрального изображения
def box_filter(img):
    y, x = img.shape[0], img.shape[1]
    ker_size = 5
    k = ker_size // 2
    int_img = integral_image(img)

    # нахожу все 4 блока интегрального изображения для каждого значения, отступая от краев на половину ядра (чтобы не выходить за рамки)
    # для каждого определяю его нахождение относительно k
    # в зависимости от ситуации линейно работаю с блоками по отдельности
    for i in range(k, y - k):
        for j in range(k, x - k):
            a = int_img[i + k][j + k]
            b = int_img[i - k - 1][j - k - 1]
            c = int_img[i - k - 1][j + k]
            d = int_img[i + k][j - k - 1]
            if i > k and j > k:
                img[i][j] = (a + b - c - d) / ker_size ** 2
            elif i == k and j > k:
                img[i][j] = (a - d) / ker_size ** 2
            elif i > k and j == k:
                img[i][j] = (a - c) / ker_size ** 2
            elif i == j == k:
                img[i][j] = a / ker_size ** 2

    # картинка уменьшается пропорционально размеру ядра
    return img[k: y - k, k: x - k].astype('uint8')


img = box_filter(imread("img.png"))
imsave("out_img.png", img)
