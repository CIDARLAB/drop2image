import sys
from PIL import Image
from PIL import ImageColor
import numpy as np
import cv2

def resize_image(filename, size):
    # can i assume that the aspect ratio of input image file and user specified size are the same?
    # ok
    im = Image.open(filename, 'r')
    r_im = im.resize(size)
    #r_im.save(filename)
    return r_im


def get_closest_color(pix, color):
    # in what form color input will be given?
    # hex, rgb, anything
    closest_color = None
    min_diff = 100000
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
            b,g,r = im[i,j]
            c_r, c_g, c_b = get_closest_color((r,g,b), color_set_rgb)
            im_out[i,j,:] = (c_b, c_g, c_r)
            # fixing the order of rgb

    return im_out

def convert_jpeg_to_pix(filename, color_set):
    im = Image.open(filename, 'r')
    w, h = im.size
    im = im.convert('RGB')
    color_set_rgb = [ImageColor.getrgb(color) for color in color_set]
    print(color_set_rgb)
    pix_list = []
    if w%2==0:
        for i in range(h):
            for j in range(w):
                if i%2==0:
                    pix = color_set_rgb.index(im.getpixel((j,i)))
                else:
                    pix = color_set_rgb.index(im.getpixel((w-1-j,i)))
                pix_list.append(pix)
    else:
        for i in range(h):
            for j in range(w):
                if i%2==0:
                    pix = color_set_rgb.index(im.getpixel((w-1-j,i)))
                else:
                    pix = color_set_rgb.index(im.getpixel((j,i)))
                pix_list.append((pix))

    return pix_list

def output_format(filename, pix):
    txt = open(filename, 'a')
    np.savetxt(filename, pix, fmt='%d', delimiter=" ")
    txt.close()
    return

# example function
image = resize_image('test_image/image.jpeg', (10, 10))
image.save('test_image/newest_image.jpeg')
color_set = ['#FFFFFF', '#000000'] # user input
im_out = get_closest_image('test_image/image.jpeg', color_set)
cv2.imwrite('test_image/closest_image.jpeg', im_out)

im_resized_out = get_closest_image('test_image/newest_image.jpeg', color_set)
cv2.imwrite('test_image/closest_resized_image.jpeg', im_resized_out)
#closest_resized_pix = convert_jpeg_to_pix('test_image/closest_resized_image.jpeg', color_set)
#output_format('test_image/closest_resized_pix.txt', closest_resized_pix)


# test with emoji with even number of pixels
resized_test = resize_image("emoji_test/test.png", (10, 10))
resized_test.save('emoji_test/resized_test.png')
color_set_even = ['#FF0000', '#FFFFFF', '#000000']
im_out = get_closest_image('emoji_test/resized_test.png', color_set_even)
cv2.imwrite('emoji_test/closest_test.png', im_out)

closest_resized_pix = convert_jpeg_to_pix('emoji_test/closest_test.png', color_set_even)
output_format('emoji_test/test.txt', closest_resized_pix)

# test with emoji with odd number of pixels
resized_odd = resize_image("emoji_test/test_odd.png", (15, 15))
resized_odd.save("emoji_test/resized_odd.png")
color_set_odd = ['#FFFF00', '#FFFFFF', '#000000']
im_out_odd = get_closest_image('emoji_test/resized_odd.png', color_set_odd)
cv2.imwrite('emoji_test/closest_odd.png', im_out_odd)

closest_resized_odd_pix = convert_jpeg_to_pix('emoji_test/closest_odd.png', color_set_odd)
output_format('emoji_test/test_odd.txt', closest_resized_odd_pix)



# QR code 100*100?

# output file to be index of color set -> done
# being order top left to bottom left -> done

