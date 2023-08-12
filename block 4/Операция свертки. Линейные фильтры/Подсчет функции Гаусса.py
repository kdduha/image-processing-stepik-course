import numpy as np

# просто иду по формуле
def gaussa(simga, x, y):
    return 1 / (2 * np.pi * sigma**2) * np.exp((-x**2 -y**2) / (2 * sigma**2))

sigma, x, y = map(int, input().split())
print(gaussa(sigma, x, y))
