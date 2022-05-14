# mengimpor library
import cv2

# Mengambil gambar dari kamera (webcam)
cap = cv2.VideoCapture(1) 
# angka yang dimasukkkan:
# 0 -> default
# 1 -> eksternal
# 2 -> untuk yang lain, dst

while True:
    ret, frame = cap.read()
    # ret menyatakan nilai Boolean True jika berhasil menangkap frame
    # frame adalah nilai array frame itu sendiri sesuai settingan kamera
    
    cv2.imshow('video', frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release() # perintah cap.release() digunakan untuk menghentikan proses rekaman
cv2.destroyAllWindows()

'''
Bagaimana menyimpan hasil rekaman
'''

# mengimpor library
import cv2

# Mengambil gambar dari kamera (webcam)
cap = cv2.VideoCapture(1) 
# angka yang dimasukkkan:
# 0 -> default
# 1 -> eksternal
# 2 -> untuk yang lain, dst

# Mengambil ukuran default dari webcam/kamera
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Menyimpan streaming video ke sebuah file
# Windows --> *'DIVX'
# MACOS/Linux --> *'XVID'
writer = cv2.VideoWriter('videoku.mp4', cv2.VideoWriter_fourcc(*'DIVX'),
                         20, (width, height))

while True:
    ret, frame = cap.read()
    # ret menyatakan nilai Boolean True jika berhasil menangkap frame
    # frame adalah nilai array frame itu sendiri sesuai settingan kamera
    
    # Menulis script untuk menhimpan video
    writer.write(frame)
    
    cv2.imshow('video', frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
writer.release()
cv2.destroyAllWindows()

'''
Membuka video dengan OpenCV
'''

import cv2
import time

cap = cv2.VideoCapture('videoku.mp4') 

if cap.isOpened() == False:
    print('Error karena filenya tidak ada atau salah Codec')

while cap.isOpened():
    ret, frame = cap.read()    
    if ret == True:
        time.sleep(1/30)    # agar tidak terlalu cepat
        cv2.imshow('video', frame)        
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()











