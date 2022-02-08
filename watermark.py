from PIL import Image
# import matplotlib.pyplot as plt
# import numpy as np
import os
from sys import argv

WM_TO_IM_RATIO = 7

def watermark(img_path, wm_path):
    image = Image.open(img_path)
    watermark = Image.open(wm_path)

    im_w, im_h = image.size
    wm_w, wm_h = watermark.size
    ratio = wm_w / wm_h

    if im_w > im_h:
        watermark = watermark.resize((int(im_w / WM_TO_IM_RATIO), int(im_w / (WM_TO_IM_RATIO * ratio))))
    else:
        watermark = watermark.resize((int(im_h / WM_TO_IM_RATIO), int(im_h // (WM_TO_IM_RATIO * ratio))))
    wm_h = watermark.size[1]
    offset = int(im_h * 0.02)
    image.paste(watermark, (offset, im_h - offset - wm_h), watermark)
    return image


def main():
    if len(argv) == 3:
        wm_path = argv[2]
    elif len(argv) == 2:
        wm_path = 'C:\\Users\\Administrator\\Downloads\\תמונות\\אריאל ונתאי\\framed-watermark.png'
    else:
        exit("Usage: python watermark.py <dir of images> [ <watermark path> ]")

    os.mkdir(f'{argv[1]}\\watermarked')
    for filename in os.listdir(argv[1]):
        image = watermark(f'{argv[1]}\\{filename}', wm_path)
        image.save(f'{argv[1]}\\watermarked\\{filename}')

    print('Done!')

main()