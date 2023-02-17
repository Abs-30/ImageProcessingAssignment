import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

im = cv.imread('images/jeniffer.jpg', cv.IMREAD_GRAYSCALE)
assert im is not None

cv.imshow(im)