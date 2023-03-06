import cv2
import numpy as np

resim = cv2.imread("joker.jpg")

resim[50,30] = [255,255,255] 
#Resmin soldan başlayarak 50 aşağısı 30 sağ pikselini istediğimiz renge çevirme

for i in range(100):
    resim[70,i] = [255,255,255]
#for döngüsüyle düz çizgi çizdirebiliriz.    
    

cv2.imshow("Joker", resim)



cv2.waitKey(0)
cv2.destroyAllWindows()