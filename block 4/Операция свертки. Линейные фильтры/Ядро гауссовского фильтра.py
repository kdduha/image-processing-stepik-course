import numpy as np

# функция Гаусса
def gauss(simga, x, y):
    return 1 / (2 * np.pi * sigma**2) * np.exp((-x**2 -y**2) / (2 * sigma**2))

# ядро
def kernel(sigma):
    # ОЧЕНЬ ВАЖЕН ТАКОЙ ПОРЯДОК СЧЕТА K 
    # (при других комбинациях операции и округления на граничных и четных значения sigma ядро ломаться по размерности)
    k = round(3 * sigma) * 2 + 1
    kernel = np.zeros((k, k))
    center = k // 2

    # заполняю ядро гауссовскими значениями
    for x in range(-center, center + 1):
        for y in range(-center, center + 1):
            kernel[x + center][y + center] = gauss(sigma, x, y)
    
    kernel /= np.sum(kernel)
    return kernel

sigma = float(input())
kernel = kernel(sigma)

for row in kernel:
    for el in row:
        # красивый вывод float по 5 знаков
        print('{:.5f}'.format(el), end=' ')
    print()
