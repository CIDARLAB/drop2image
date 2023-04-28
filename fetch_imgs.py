import cv2
import glob
import math
import sys

def fetch(base_img_name):
    if base_img_name == '':
        base_img_name = "concat_image/test" # example folder
    files = glob.glob(base_img_name + '_*.png')
    image_dim = int(math.sqrt(len(files))) # for now
    img_h = [None] * image_dim

    for i in range(image_dim):
        images = [cv2.imread(file) for file in glob.glob(base_img_name + '_' + str(i) + '_*.png')]
        img_h[i] = cv2.hconcat(images)

    cv2.imwrite('test.png', cv2.vconcat(img_h))
        

if __name__ == '__main__':
    if (len(sys.argv) == 1):
        fetch('')
    else:
        fetch(sys.argv[1])
        
# some ideas
## use circle ditection library to get the droplets, determine the closest color, create pix again