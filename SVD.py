# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#def print_lyrics():
#    print("Im a lumberjack, and Im okay.")
#    print("I sleep all night and I work all day.")
#
#def addTwoNum(a, b):
#    print(a + b)
#    return a + b
#
#
#print(addTwoNum())
#print(addTwoNum(10, 15))
#print_lyrics()

#if 54 in [2, 54, 3, 76, 5]:
#    print('Found', 3)
#else:
#    print('Not Found!')

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

plt.style.use('classic')
img = Image.open('GradDayPic02_07_2016 - Copy.JPG')
# convert image to grayscale
imggray = img.convert('LA')
# convert to numpy array
imgmat = np.array(list(imggray.getdata(band=0)), float)
# Reshape according to orginal image dimensions
imgmat.shape = (imggray.size[1], imggray.size[0])

plt.figure(figsize=(9, 6))
plt.imshow(imgmat, cmap='gray')
plt.show()

U, D, V = np.linalg.svd(imgmat)
imgmat.shape
U.shape
D.shape
V.shape

reconstimg = np.matrix(U[:, :2]) * np.diag(D[:2]) * np.matrix(V[:2, :])
plt.imshow(reconstimg, cmap='gray')
plt.show()
#
#
for i in [5, 10, 15, 20, 30, 50, 100]:
    reconstimg = np.matrix(U[:, :i]) * np.diag(D[:i]) * np.matrix(V[:i, :])
    plt.imshow(reconstimg, cmap='gray')
    title = "n = %s" % i
    plt.title(title)
    plt.show()