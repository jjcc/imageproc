# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import cv2
import numpy as np

#myimg = np
def paint_block(rgb):
    #img = np.zeros([50,50,3])
    img = np.ones([50,50,3])
    # t0 = t.time()
    # np_rgb[:,:,0] = image[:,:,2]
    # np_rgb[:,:,1] = image[:,:,1]
    # np_rgb[:,:,2] = image[:,:,0]
    img[:,:,0] = rgb[0]/255.0
    img[:,:,1] = rgb[1]/255.0
    img[:,:,2] = rgb[2]/255.0
    return img


def draw_colorblocks():
    plt.figure(figsize=(2, 2))
    colors = [0xADFF2F, 0xFFFF00, 0x93D2D4, 0xD2691E, 0x967EC7, 0xFFFFFF, 0x000000, 0xFFB7AF, 0xE24060, 0xFF98E65]
    temp = paint_block([0xff, 0, 0])
    for c in colors:
        color = c
        r = color >> 16
        color = c
        g = (color & 0xff00) >> 8
        color = c
        b = color & 0xff
        rgb = [r, g, b]
        # print("color->r,g,b:%x -> %x,%x,%x"%(color,r,g,b))
        img = paint_block(rgb)

        merged = cv2.hconcat((temp, img))
        temp = merged
    temp = cv2.convertScaleAbs(temp, alpha=(255.0))
    imgsave = cv2.cvtColor(temp, cv2.COLOR_BGR2RGB)
    cv2.imwrite('merged.png', imgsave)
    plt.figure(figsize=(5, 5))
    color2 = [0xFF, 0, 0]
    img2 = paint_block(color2)
    # plt.subplot(2,5,3)
    plt.imshow(temp)
    # plt.title('my picture')
    plt.show()





def main():
    draw_colorblocks()

if __name__ == "__main__":
    # arguments = parse_arguments()

    main(sys.argv[1:])
    # test_harvest()