# -*- coding: utf-8 -*-
"""

@File    : ocr_util.py
@Description :
@Author  : MandyL
@Time    : 2021/6/18 17:21

"""
import sys

import pytesseract

sys.path.append('./')
sys.path.append('../')

try:
    from PIL import Image
except ImportError:
    import Image


def download_yzm():
    image_path = 'image.png'
    image_get = Image.open(image_path).resize((300, 180))
    image_grayscale = image_get.convert('L')  # 灰度处理
    image_dealed = image_thresholding_method(image_grayscale)  # 二值化处理
    result = pytesseract.image_to_string(image_dealed)
    result = result.strip()
    if not result:
        result = 'yzm'
    return result


def get_yzm_img(browser):
    browser.save_screenshot("pic.png")
    code_element = browser.find_element_by_id("authcode")
    # 图片4个点的坐标位置
    left = code_element.location['x']+225  # x点的坐标
    top = code_element.location['y']  # y点的坐标
    # left = code_element.location['x'] + 400  # x点的坐标
    # top = code_element.location['y'] + 80  # y点的坐标
    right = 80 + left
    height = code_element.size['height'] + top
    # right = 105 + left  # 上面右边点的坐标
    # height = 47 + top  # 下面右边点的坐标
    image = Image.open('pic.png')
    code_image = image.crop((left, top, right, height))
    code_image.save('image.png')


def image_thresholding_method(image):
    # 图片二值化处理，image为灰度化后的图片
    # 阈值，控制二值化程度
    threshold = 150
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    # 图片二值化
    image = image.point(table, '1')
    return image


if __name__ == '__main__':
    txt = download_yzm()
    print(txt)
