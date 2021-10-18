import cv2 as cv

img = cv.imread('../data/lena_std.tif')
cv.imshow('image',img)
k = cv.waitKey()

if k==ord('s'):
    cv.imwrite('saved_img.tif', img)
