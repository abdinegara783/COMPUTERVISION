# Mengimpor library
import cv2
import matplotlib.pyplot as plt

# Membuka file dengan OpenCV
gambar = cv2.imread('D:/Megabagusid/Python Masterclass/ayam.jpg')
type(gambar)
# Membuka file yang salah
gambar2 = cv2.imread('asdasdasd.jpg')
type(gambar2)

# Mengeluarkan gambar
plt.imshow(gambar)
plt.imshow(gambar2) # akan error

# Konversi ke RGB
gambar_rgb = cv2.cvtColor(gambar, cv2.COLOR_BGR2RGB)
plt.imshow(gambar_rgb)

# Merubah gambar ke grayscale
gambar_gray = cv2.imread('D:/Megabagusid/Python Masterclass/ayam.jpg', cv2.IMREAD_GRAYSCALE)
plt.imshow(gambar_gray) # default cmap viridis
plt.imshow(gambar_gray, cmap='gray')

# Mengecilkan gambar dengan ukuran yang jelas
gambar_baru = cv2.resize(gambar_rgb,(500,700)) # format resize adalah (sumbu x, sumbu y) --> (kolom,baris)
plt.imshow(gambar_baru)

# Mengecilkan gambar berdasarkan rasio
rasio_baris = 0.5 # baris adalah sumbu y di plt.imshow()
rasio_kolom = 0.5 # kolom adalah sumbu x di plt.imshow()
gambar_baru2 = cv2.resize(gambar_rgb, (0,0), gambar_rgb, rasio_kolom, rasio_baris)
plt.imshow(gambar_baru2)
rasio_baris2 = 0.76
rasio_kolom2 = 0.86
gambar_baru3 = cv2.resize(gambar_rgb, (0,0), gambar_rgb, rasio_kolom2, rasio_baris2) # 0.76*1280 dan 0.86*1920
plt.imshow(gambar_baru3)

# Membalik gambar
gambar_terbalik = cv2.flip(gambar_rgb,0) # nilai 0 membalik gambar sesuai sumbu x
plt.imshow(gambar_terbalik)
gambar_terbalik2 = cv2.flip(gambar_rgb,1) # nilai 1 membalik gambar sesuai sumbu y
plt.imshow(gambar_terbalik2)
gambar_terbalik3 = cv2.flip(gambar_rgb,-1) # nilai -1 membalik gambar sesuai sumbu x dan y sekaligus
plt.imshow(gambar_terbalik3)
# parameter flip sangat penting dalam pembahasan deep learning selanjutnya

# Merubah tipe file
type(gambar_rgb)
cv2.imwrite('gambar_baru_bro.jpg', gambar_rgb) # akan menjadi BGR
cv2.imwrite('gambar_baru_bro2.jpg', gambar) # jadi save file yang aslinya adalah BGR, otomatis imwrite akan merubahnya ke RGB

# memunculkan gambar langsung dari OpenCV
cv2.imshow('Ayam', gambar) # akan memunculkan sesuai resolusi aslinya
cv2.waitKey() # menunggu sampai kita menekan sesuai di keyboard