# -*- coding: utf-8 -*-
"""

@File    : ocr_util.py
@Description :
@Author  : ljw
@Time    : 2021/6/18 17:21

"""
import requests
from PIL.Image import Image


def download_yzm():
    IMAGE_URL = 'http://ids2.just.edu.cn//cas/captcha.jpg'
    r = requests.get(IMAGE_URL)
    with open('img.png', 'wb') as f:
        f.write(r.content)
