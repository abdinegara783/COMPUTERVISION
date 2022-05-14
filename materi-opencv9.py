# Mengimpor library
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load gambar
gambar = cv2.imread('D:/Megabagusid/Python Masterclass/papan_catur.png')
gambar = cv2.cvtColor(gambar,cv2.COLOR_BGR2RGB)
plt.imshow(gambar)

# ubah ke abu-abu
gambar_abu = cv2.cvtColor(gambar, cv2.COLOR_RGB2GRAY)
plt.imshow(gambar_abu, cmap='gray')

# load papan catur asli
gambar_asli = cv2.imread('D:/Megabagusid/Python Masterclass/papan_catur_asli.jpg')
gambar_asli = cv2.cvtColor(gambar_asli,cv2.COLOR_BGR2RGB)
plt.imshow(gambar_asli)

gambar_asli_abu = cv2.cvtColor(gambar_asli, cv2.COLOR_RGB2GRAY)
plt.imshow(gambar_asli_abu, cmap='gray')



# Menggunakan Harris corner detection
# Merubah menjadi numpy float (syarat algoritmanya)
abu = np.float32(gambar_abu)
sudut = cv2.cornerHarris(src=abu, blockSize=2, 
                         ksize=3, k=0.04)
sudut = cv2.dilate(sudut, None)
# dilate merupakan teknik morphological transformations untuk keperluan plotting
# di mana ia digunakan untuk memperjelas gambarnya
gambar[sudut>0.01*sudut.max()] = [255,0,0]
plt.imshow(gambar)

# Menggunakan papan catur asli
abu2 = np.float32(gambar_asli_abu)
sudut2 = cv2.cornerHarris(src=abu2, blockSize=2, 
                         ksize=3, k=0.04)
sudut2 = cv2.dilate(sudut2, None)
gambar_asli[sudut2>0.01*sudut2.max()] = [255,0,0]
plt.imshow(gambar_asli)



# Menggunakan Shi-Tomasi Detection
# reload gambar
gambar = cv2.imread('D:/Megabagusid/Python Masterclass/papan_catur.png')
gambar = cv2.cvtColor(gambar,cv2.COLOR_BGR2RGB)
gambar_abu = cv2.cvtColor(gambar, cv2.COLOR_RGB2GRAY)

gambar_asli = cv2.imread('D:/Megabagusid/Python Masterclass/papan_catur_asli.jpg')
gambar_asli = cv2.cvtColor(gambar_asli,cv2.COLOR_BGR2RGB)
gambar_asli_abu = cv2.cvtColor(gambar_asli, cv2.COLOR_RGB2GRAY)

# Deteksi gambar hitam putih dengan Shi-tomasi
sudut = cv2.goodFeaturesToTrack(image=gambar_abu, 
                                maxCorners=20, 
                                qualityLevel=0.01, 
                                minDistance=10)
# Jika ingin benar-benar mendeteksi angka sudut maks, 
# maxCorners = -1
# Shi-tomasi tidak langsung memberikan visualisasi sudut, maka harus
# kita modifikasi dengan menggambar manual
sudut = np.int0(sudut)
for i in sudut:
    x,y = i.ravel() # meratakan (flattening) array (menjadi 1 dimensi)
    cv2.circle(gambar, (x,y), 3, (255,0,0), -1)
plt.imshow(gambar)

# Deteksi gambar asli dengan Shi-tomasi
sudut2 = cv2.goodFeaturesToTrack(image=gambar_asli_abu, 
                                maxCorners=80, 
                                qualityLevel=0.01, 
                                minDistance=10)
sudut2 = np.int0(sudut2)
for i in sudut2:
    x,y = i.ravel() # meratakan (flattening) array (menjadi 1 dimensi)
    cv2.circle(gambar_asli, (x,y), 3, (255,0,0), -1)
plt.imshow(gambar_asli) 