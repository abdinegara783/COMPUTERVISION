# Mengimpor library
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Membuat kanvas hitam
kosong = np.zeros(shape=(1000,2000,3))
plt.imshow(kosong)

# Menggambar persegi panjang (rectangle) dan circle
cv2.rectangle(kosong, pt1=(600,800), pt2=(950,400), 
              color=(255,0,0), thickness=-1)
cv2.rectangle(kosong, pt1=(1750,400), pt2=(1500,200), 
              color=(0,0,255), thickness=5)
cv2.rectangle(kosong, pt1=(250,800), pt2=(500,200), 
              color=(0,255,0), thickness=5)
cv2.circle(kosong, center=(1250,500), radius=50, 
           color=(255,230,140), thickness=8)
cv2.circle(kosong, center=(1500,700), radius=250, 
           color=(0,30,255), thickness=8)
plt.imshow(kosong)

# Membuat garis
cv2.line(kosong, pt1=(0,100), pt2=(2000,900), 
         color=(255,255,255), thickness=10)
plt.imshow(kosong)

# Menambahkan teks
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(kosong, text='Python', org=(1000,200), fontFace=font, fontScale=4,
            color=(255,255,255), thickness=7, lineType=cv2.LINE_AA)
plt.imshow(kosong)
