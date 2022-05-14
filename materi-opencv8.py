# Mengimpor library
import cv2
import matplotlib.pyplot as plt

# Membuka gambar
lengkap = cv2.imread('D:/Megabagusid/Python Masterclass/ayam.jpg')
plt.imshow(lengkap)
lengkap = cv2.cvtColor(lengkap, cv2.COLOR_BGR2RGB)
plt.imshow(lengkap)

# Membuka gambar
kepala = cv2.imread('D:/Megabagusid/Python Masterclass/ayam potong.jpg')
kepala = cv2.cvtColor(kepala, cv2.COLOR_BGR2RGB)
plt.imshow(kepala)

# Menyiapkan 3 objek berbeda untuk 3 nilai kepala.shape
kepala.shape
height, width, channels = kepala.shape

# Ada 6 metode yang akan digunakan (gunakan fungsi eval() untuk merubah string menjadi function)
teknik = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,cv2.TM_CCORR_NORMED, 
          cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
teknik_str = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 
              'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

# Mulai melakukan template matching
lengkap_copy = lengkap.copy()

hasil = cv2.matchTemplate(lengkap_copy, kepala, cv2.TM_CCOEFF)
plt.imshow(hasil)

# Menyiapkan 4 objek untuk menampung hasil minMaxLoc
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(hasil)

# Menentukan lokasi titik awal (pt1) dan titik akhir (pt2)
pt1 = max_loc
pt2 = (pt1[0]+width, pt1[1]+height)

# Menggambar rectangle
cv2.rectangle(lengkap_copy, pt1, pt2, (0,255,0), 20)

plt.figure()
plt.subplot(1,2,1)
plt.imshow(hasil)
plt.title('hasil template matching')

plt.subplot(1,2,2)
plt.imshow(lengkap_copy)
plt.title('Lokasi terdeteksi')
plt.suptitle('Teknik = '+teknik_str[0])

# For loop untuk semua teknik template matching
for i in teknik:
    
    # Membuat duplikasi objek lengkap
    lengkap_copy = lengkap.copy()
    
    # Mengaplikasikan template matching
    hasil = cv2.matchTemplate(lengkap_copy, kepala, i)
    
    # Menyiapkan 4 objek untuk menampung hasil minMaxLoc
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(hasil)
    
    # Khusus untuk 2 algoritma yang ada SQ, kita gunakan nilai min
    if i in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        pt1 = min_loc
    else:
        pt1 = max_loc
    
    # Menentukan pt2
    pt2 = (pt1[0]+width, pt1[1]+height)
    
    # Menggambar rectangle
    cv2.rectangle(lengkap_copy, pt1, pt2, (0,255,0), 20)
    
    plt.figure()
    plt.subplot(1,2,1)
    plt.imshow(hasil)
    plt.title('hasil template matching')

    plt.subplot(1,2,2)
    plt.imshow(lengkap_copy)
    plt.title('Lokasi terdeteksi')
    plt.suptitle('Teknik = '+teknik_str[teknik[i]])