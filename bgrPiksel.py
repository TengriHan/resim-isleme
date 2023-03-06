import cv2
import numpy as np

KediResim = cv2.imread("kedi.jpg")

cv2.imshow("Kedi Resmi", KediResim)


print(KediResim[(230,80)])

print("Resmin Boyutu: " +str(KediResim.size))
print("Resmin Özellikleri: " + str(KediResim.shape))
print("Resmin Veri Tipi: " +str(KediResim.dtype))



cv2.waitKey(0)
cv2.destroyAllWindows()