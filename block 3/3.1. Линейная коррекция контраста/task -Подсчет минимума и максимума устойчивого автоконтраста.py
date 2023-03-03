from skimage.io import imread

pixels = sorted(imread('img.png').ravel())
k = round(len(pixels) * 0.05)
print(pixels[k], pixels[-k-1])
