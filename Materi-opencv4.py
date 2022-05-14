# Mengimpor library
import cv2
import numpy as np

'''
Menggambar lingkaran dengan klik kiri mouse
'''

# Membuat fungsi membuat lingkaran
def buat_circle(event,x,y,flags,param): # format fungsi ini ada di dokumentasi opencv
# walau kita tidak menggunakan flags dan param, kedua parameter ini tetap wajib didefinisikan
    if event == cv2.EVENT_LBUTTONDOWN: # mouse klik kiri 
        cv2.circle(canvas,center=(x,y),radius=100, color=(0,255,0), thickness=-1)

# Menyiapkan canvas kita
canvas = np.zeros((1000,1000,3))

# Memberi nama window gambar-nya
cv2.namedWindow(winname='gambarku')

# Menghubungkan mouse kita dengan fungsi buat_circle di gambarku
cv2.setMouseCallback('gambarku', buat_circle)

# while loop
while True: 
    cv2.imshow('gambarku',canvas) # perlu diingat jika menggunakan cv2.imshow maka format warnanya adalah BGR
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
# baris 18-28 harus dieksekusi sekaligus (atau otomatis jika di python script)


'''
Membuat fungsi dengan klik kiri dan klik kanan mouse
'''

# Membuat fungsi membuat lingkaran
def buat_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: # mouse klik kiri 
        cv2.circle(canvas,center=(x,y),radius=100, color=(0,255,0), thickness=-1)
    elif event == cv2.EVENT_RBUTTONDOWN: # mouse klik kanan
        cv2.circle(canvas,center=(x,y),radius=100, color=(255,0,0), thickness=-1)

# Menyiapkan canvas kita
canvas = np.zeros((1000,1000,3))

# Memberi nama window gambar-nya
cv2.namedWindow(winname='gambarku')

# Menghubungkan mouse kita dengan fungsi buat_circle di gambarku
cv2.setMouseCallback('gambarku', buat_circle)

# while loop
while True: 
    cv2.imshow('gambarku',canvas) # perlu diingat jika menggunakan cv2.imshow maka format warnanya adalah BGR
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()

'''
Membuat fungsi menggambar rectangle dengan drag mouse
'''

canvas = np.zeros((1000,1000,3))

# Membuat variabel penentu apakah kita masih menahan klik kiri atau tidak
tahan = False
ix,iy = -1,-1 # ix dan iy adalah posisi kursor mouse awal, -1,-1 artinya tidak masuk di koordinat canvas (karena dimulai dari 0,0)

# Membuat fungsi membuat rectangle
def buat_rectangle(event,x,y,flags,param):
    
    global ix,iy,tahan
    
    if event == cv2.EVENT_LBUTTONDOWN:
        tahan = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if tahan == True:
            cv2.rectangle(canvas, pt1=(ix,iy), pt2=(x,y), color=(255,0,0), thickness=-1)
    elif event == cv2.EVENT_LBUTTONUP:
        tahan = False
        cv2.rectangle(canvas, pt1=(ix,iy), pt2=(x,y), color=(255,0,0), thickness=-1)

# Memberi nama window gambar-nya
cv2.namedWindow(winname='gambarku')

# Menghubungkan mouse kita dengan fungsi buat_rectangle di gambarku
cv2.setMouseCallback('gambarku', buat_rectangle)

# while loop
while True: 
    cv2.imshow('gambarku',canvas) # perlu diingat jika menggunakan cv2.imshow maka format warnanya adalah BGR
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
