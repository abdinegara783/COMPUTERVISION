# Download file gambar ayam: shorturl.at/cdnDN

# Mengimpor library
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image # library pillow

# Menyiapkan gambar
gambar = Image.open('D:/Megabagusid/Python Masterclass/ayam.jpg') # Sesuaikan path dengan direktori foto ayam
type(gambar)

# Merubah gambar menjadi array
gambar_ar = np.asarray(gambar)
type(gambar_ar)

# Memunculkan gambar
plt.imshow(gambar_ar)

# Memunculkan gambar 1 channel
# RGB - Red, Green, Blue
plt.imshow(gambar_ar[:,:,0])
gambar_ar[:,:,0].shape
gambar_ar.shape
plt.imshow(gambar_ar[:,:,0], cmap='viridis')
plt.imshow(gambar_ar[:,:,0], cmap=None)
plt.imshow(gambar_ar[:,:,0], cmap='gray')
plt.imshow(gambar_ar[:,:,0]) # Red
plt.imshow(gambar_ar[:,:,1]) # Green
plt.imshow(gambar_ar[:,:,2]) # Blue
plt.imshow(gambar_ar)

# Menyisakan channel Green
gambar_hijau = gambar_ar.copy()
gambar_hijau[:,:,0] = 0
gambar_hijau[:,:,2] = 0
plt.imshow(gambar_hijau)

# Memulai OpenCV --> bahasa C++
import cv2

# Membuka file dengan OpenCV
ayam = cv2.imread('D:/Megabagusid/Python Masterclass/ayam.jpg')
plt.imshow(ayam)
# Pillow RGB - Red Green Blue
# OpenCV BGR - Blue Green Red
type(ayam)

# Konversi ke RGB
ayam_rgb = cv2.cvtColor(ayam, cv2.COLOR_BGR2RGB)
plt.imshow(ayam_rgb)

# Melihat apakah gambar array pillow identik dengan OpenCV rgb
ayam_rgb == gambar_ar
