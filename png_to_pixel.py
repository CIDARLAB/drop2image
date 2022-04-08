import sys
from PIL import Image
from PIL import ImageColor
import numpy as np
import os
import PIL
import glob
import cv2

def resize_image(filename, size):
    # can i assume that the aspect ratio of input image file and user specified size are the same?
    im = Image.open(filename, 'r')
    r_im = im.resize(size)
    #r_im.save(filename)
    return r_im


def get_closest_color(pix, color):
    # in what form color input will be given?
    closest_color = None
    min_diff = sys.maxsize
    pix = np.array(pix)
    for clr in color:
        clr = np.array(clr)
        diff = np.sum((clr-pix)**2)
        if diff < min_diff:
            min_diff = diff
            closest_color = clr
    return closest_color


def get_closest_image(filename, color_set):
    #im = Image.open(filename, 'r')
    im = cv2.imread(filename)
    color_set_rgb = [ImageColor.getrgb(color) for color in color_set]

    h, w, c = im.shape
    im_out = np.zeros((h,w,c))

    for i in range(h):
        for j in range(w):
            closest_color = get_closest_color(im[i,j], color_set_rgb)
            im_out[i,j,:] = closest_color

    return im_out

def convert_jpeg_to_pix(filename):
    im = Image.open(filename, 'r')
    w, h = im.size
    im = im.convert('RGB')
    pix_list = []
    for i in range(w):
        for j in range(h):
            pix = image.getpixel((i,j))
            pix_list.append(tuple(pix))

    return pix_list

def output_format(filename, pix):
    txt = open(filename, 'a')
    np.savetxt(filename, pix, fmt='%d', delimiter=" ")
    return

# example function
image = resize_image('image.jpeg', (10,10))
image.save('newest_image.jpeg')

color_set = []
im_out = get_closest_image('image.jpeg', color_set)

#im_out.save('closest_image.jpeg')
cv2.imwrite('closest_image.jpeg', im_out)

im_resized_out = get_closest_image('newest_image.jpeg', color_set)
cv2.imwrite('closest_resized_image.jpeg', im_resized_out)
closest_resized_pix = convert_jpeg_to_pix('closest_resized_image.jpeg')
output_format('closest_resized_pix.txt', closest_resized_pix)


# txt = open('image_pix.txt', 'a')
#
# width, height = image.size
# print(image.size)
#
# #pix = list(image.getdata())
# #pix = [pix[i * width:(i + 1) * width] for i in range(height)]
# #pix = np.array(pix).reshape((width, height))
# #print(pix)
# #image.save('new_image.jpeg')
# #pix = image.load()
#
# image = image.convert('RGB')
#
# pix_list = []
#
# for i in range(image.width):
#     for j in range(image.height):
#         pix = image.getpixel((i, j))
#         pix_list.append(tuple(pix))
#         #print(pix)
#
# np.savetxt("image_pix.txt", pix_list, fmt='%d', delimiter=" ")
# txt.close()
