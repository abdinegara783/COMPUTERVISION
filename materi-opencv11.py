# Mengimpor library
import cv2
import matplotlib.pyplot as plt

# Menyiapkan gambar
lincoln = cv2.imread('D:/Megabagusid/Python Masterclass/abraham_lincoln.jpeg')
plt.imshow(lincoln)
yani = cv2.imread('D:/Megabagusid/Python Masterclass/ahmad_yani.jpeg')
plt.imshow(yani)
banyak = cv2.imread('D:/Megabagusid/Python Masterclass/banyak_wajah.jpg')
plt.imshow(banyak)

# 6000 features dari haarcascade
wajah_cascade = cv2.CascadeClassifier('D:/Megabagusid/Python Masterclass/haarcascades/haarcascade_frontalface_default.xml')

def deteksi_wajah(gambar):
    gambar_wajah = gambar.copy()
    
    kotak_wajah = wajah_cascade.detectMultiScale(gambar_wajah)
    
    for (x,y,l,t) in kotak_wajah:
        cv2.rectangle(gambar_wajah,(x,y),(x+l,y+t), (255,255,255),10)
    
    return gambar_wajah

# Mencoba mendeteksi wajah 3 foto di awal
hasil = deteksi_wajah(lincoln)
plt.imshow(hasil)
hasil2 = deteksi_wajah(yani)
plt.imshow(hasil2)
hasil3 = deteksi_wajah(banyak)
plt.imshow(hasil3)

# Improve algoritma
def deteksi_wajah_v2(gambar):
    gambar_wajah = gambar.copy()
    
    kotak_wajah = wajah_cascade.detectMultiScale(gambar_wajah,
                                                 scaleFactor=1.2,
                                                 minNeighbors=5)
    
    for (x,y,l,t) in kotak_wajah:
        cv2.rectangle(gambar_wajah,(x,y),(x+l,y+t), (255,255,255),10)
    
    return gambar_wajah

hasil3_v2 = deteksi_wajah_v2(banyak)
plt.imshow(hasil3_v2)

# Kita coba deteksi mata dengan haarcascade
mata_cascade = cv2.CascadeClassifier('D:/Megabagusid/Python Masterclass/haarcascades/haarcascade_eye.xml')

# Fungsi mendeteksi mata
def deteksi_mata(gambar):
    gambar_wajah = gambar.copy()
    
    kotak_mata = mata_cascade.detectMultiScale(gambar_wajah,
                                                 scaleFactor=1.2,
                                                 minNeighbors=5)
    
    for (x,y,l,t) in kotak_mata:
        cv2.rectangle(gambar_wajah,(x,y),(x+l,y+t), (255,255,255),10)
    
    return gambar_wajah

# Mendeteksi mata lincoln
hasil4 = deteksi_mata(lincoln)
plt.imshow(hasil4)

# Fungsi deteksi wajah dan mata
def deteksi_semua(gambar):
    gambar_wajah = gambar.copy()
    
    kotak_wajah = wajah_cascade.detectMultiScale(gambar_wajah,
                                                 scaleFactor=1.2,
                                                 minNeighbors=5)
    
    kotak_mata = mata_cascade.detectMultiScale(gambar_wajah,
                                                 scaleFactor=1.2,
                                                 minNeighbors=5)
    
    for (x,y,l,t) in kotak_wajah:
        cv2.rectangle(gambar_wajah,(x,y),(x+l,y+t), (255,255,255),4)
    
    for (x,y,l,t) in kotak_mata:
        cv2.rectangle(gambar_wajah,(x,y),(x+l,y+t), (0,255,0),2)
    
    return gambar_wajah

# Mendeteksi wajah dan mata lincoln
hasil5 = deteksi_semua(lincoln)
plt.imshow(hasil5)


# Dengan video
import cv2
import matplotlib.pyplot as plt

wajah_cascade = cv2.CascadeClassifier('D:/Megabagusid/Python Masterclass/haarcascades/haarcascade_frontalface_default.xml')
mata_cascade = cv2.CascadeClassifier('D:/Megabagusid/Python Masterclass/haarcascades/haarcascade_eye.xml')

def deteksi_semua(gambar):
    gambar_wajah = gambar.copy()
    
    kotak_wajah = wajah_cascade.detectMultiScale(gambar_wajah, scaleFactor=1.2, minNeighbors=5)
    kotak_mata = mata_cascade.detectMultiScale(gambar_wajah, scaleFactor=1.2, minNeighbors=5)
    
    for (x,y,l,t) in kotak_wajah:
        cv2.rectangle(gambar_wajah,(x,y),(x+l,y+t), 
                      (255,255,255),4)
    
    for (x,y,l,t) in kotak_mata:
        cv2.rectangle(gambar_wajah,(x,y),(x+l,y+t), 
                      (0,255,0),2)
    
    return gambar_wajah

cap = cv2.VideoCapture(2, cv2.CAP_DSHOW) # cv2.CAP_DSHOW agar tidak error
while True:
    
    ret, frame = cap.read()
    frame = deteksi_semua(frame)
    cv2.imshow('Video Deteksi Wajah dan mata', frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()