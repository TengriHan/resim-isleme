# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 12:25:58 2023

@author: TengriHan
"""

import cv2
import numpy as np

resim = cv2.imread("logo2.png")
resim1 = cv2.imread("awa.jpg")
#Ekstra olarak "Logo2.png"'nin yanına 0 eklersek siyah beyaz olur
cv2.imshow("Furkan Logo", resim)

print(resim.size)
#Resim boyutu
print(resim.dtype)
#Resim veri tipi
print(resim.shape)
#Resimin ebatlarını ve kaç kanal kullandığını söyler.

cv2.waitKey(0)
cv2.destroyAllWindows()
