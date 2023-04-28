import eel
import cv2
import glob
import math

eel.init('web')

@eel.expose
def save_pix(pix_list):
    print("Hello World!")

@eel.expose
def fetch():
    base_img_name = "../concat_image/test"
    files = glob.glob(base_img_name + '_*.png')
    image_dim = int(math.sqrt(len(files))) # for now
    img_h = [None] * image_dim
    for i in range(image_dim):
        images = [cv2.imread(file) for file in glob.glob(base_img_name + '_' + str(i) + '_*.png')]
        img_h[i] = cv2.hconcat(images)
    cv2.imwrite('test.png', cv2.vconcat(img_h))
    print("fetched")

eel.start('index.html')