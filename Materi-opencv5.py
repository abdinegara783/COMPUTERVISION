# Mengimpor library
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Menyiapkan gambar
gambar = cv2.imread('D:/Megabagusid/Python Masterclass/ayam.jpg')
plt.imshow(gambar)
# jika menggunakan cv2.imshow() --> cv2.imshow('ayam',gambar)

# Merubah ke RGB
gambar_rgb = cv2.cvtColor(gambar, cv2.COLOR_BGR2RGB)
plt.imshow(gambar_rgb)

# Merubah dari BGR ke HSV
gambar_hsv = cv2.cvtColor(gambar, cv2.COLOR_BGR2HSV)
plt.imshow(gambar_hsv)

# Merubah dari RGB ke HSV
gambar_hsv2 = cv2.cvtColor(gambar_rgb, cv2.COLOR_RGB2HSV)
plt.imshow(gambar_hsv2)

# Jika salah konversi (seharusnya BGR tapi RGB ke HSV)
gambar_hsv3 = cv2.cvtColor(gambar, cv2.COLOR_RGB2HSV)
plt.imshow(gambar_hsv3)
# ternyata hasilnya berbeda


'''
Menggabungkan (blending) beberapa gambar

Formula:
blending = α⋅gb1+(1-α)⋅gb2+γ
blending = α⋅gb1+β⋅gb2+γ
'''

gb1 = cv2.imread('D:/Megabagusid/Python Masterclass/ayam.jpg')
gb1 = cv2.cvtColor(gb1, cv2.COLOR_BGR2RGB)
plt.imshow(gb1)
gb2 = cv2.imread('D:/Megabagusid/Python Masterclass/watermark.png')
gb2 = cv2.cvtColor(gb2, cv2.COLOR_BGR2RGB)
plt.imshow(gb2)

# Menggabungkan gambar dengan ukuran yang sama
gb1_baru = cv2.resize(gb1,(1200,1200))
gb2_baru = cv2.resize(gb2,(1200,1200))
plt.imshow(gb1_baru)
plt.imshow(gb2_baru)
gabung = cv2.addWeighted(src1=gb1_baru, alpha=0.5,
                         src2=gb2_baru, beta=0.5,
                         gamma=0)
plt.imshow(gabung)
# Membuat gambar 1 lebih menonjol
gabung2 = cv2.addWeighted(src1=gb1_baru, alpha=0.8,
                         src2=gb2_baru, beta=0.2 ,
                         gamma=0)
plt.imshow(gabung2)
# Perintah addWeighted hanya bisa untuk penggabungan gambar yg ukurannya sama


'''
Melakukan proses overlay (menumpuk gambar - tanpa blending)
'''

gb2_kecil = cv2.resize(gb2,(600,700))
plt.imshow(gb2_kecil)
plt.imshow(gb1)

# Menentukan koordinat awal dan akhir (untuk mempermudah)
y_awal = 0
y_akhir = y_awal + gb2_kecil.shape[0]
x_awal = 0
x_akhir = x_awal + gb2_kecil.shape[1]

# Kita akan memasang gb2_kecil di atas gb1
tempel = gb1.copy()
tempel[y_awal:y_akhir, x_awal:x_akhir] = gb2_kecil 
# tempel[0:+ gb2_kecil.shape[0], 0:0+gb2_kecil.shape[1]] = gb2_kecil 
plt.imshow(tempel)
plt.imshow(gb1) # pentingnya menggunakan copy()


'''
Melakukan masking
'''

# ROI = Region of Interest
y_awal = gb1.shape[0] - 700
y_akhir = y_awal + gb2_kecil.shape[0] # atau cukup gb1.shape[0]
x_awal = gb1.shape[1] - 600
x_akhir = x_awal + gb2_kecil.shape[1] # atau cukup gb1.shape[1]
roi = gb1[y_awal:y_akhir, x_awal:x_akhir]
plt.imshow(roi)

# Membuat mask-nya
gb2_gray = cv2.cvtColor(gb2_kecil, cv2.COLOR_RGB2GRAY)
plt.imshow(gb2_gray)
plt.imshow(gb2_gray, cmap='gray')

# Membuat inverse (pixel hitam jadi putih, dan sebaliknya)
gb2_inv = cv2.bitwise_not(gb2_gray)
plt.imshow(gb2_inv)
plt.imshow(gb2_inv, cmap='gray')
# perhatikan bahwa sekarang gb2_inv hanya 3 dimensi shape nya

# menambah background (menambah channel) ke gb2_inv
bg_putih = np.full(gb2_kecil.shape,255)
plt.imshow(bg_putih)

# menggabungkan bg_putih dengan gb2_inv --> sebuah ilustrasi penggabungan gambar dengan masking
gb2_potong = cv2.bitwise_or(bg_putih, bg_putih, mask=gb2_inv)
# cara bacanya= gabungkan bg_putih dengan bg_putih lalu untuk ketiga channelnya
# ditumpuk (masking) dengan gb2_inv
plt.imshow(gb2_potong)

# Memotong gb2_kecil berdasarkan gb2_final
gb2_final = cv2.bitwise_or(gb2_kecil, gb2_kecil, mask=gb2_inv)
plt.imshow(gb2_final)

# tahap akhir untuk roi
roi_final = cv2.bitwise_or(roi,gb2_final)
plt.imshow(roi_final)

# tahap akhir masking
gb_final = gb1.copy()
plt.imshow(gb_final)
gb_final[y_awal:y_akhir, x_awal:x_akhir] = roi_final
plt.imshow(gb_final)
