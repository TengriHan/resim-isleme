# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 12:04:08 2023

@author: TengriHan
"""

from PIL import Image

# Gif dosyası adı
gif_file = "pout-christian-bale.gif"

# Görüntülerin adları ve dosya yolları
image_files = ["logo.png", "logo2.png", "Dark.png"]

# Görüntüleri açın ve bir GIF dosyasına kaydedin
images = []
for file in image_files:
    with Image.open(file) as im:
        images.append(im.copy())

images[0].save(gif_file, save_all=True, append_images=images[1:], duration=1000, loop=0)
