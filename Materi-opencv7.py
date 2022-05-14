# Mengimpor library
import cv2

# Menyiapkan webcam
cap = cv2.VideoCapture(0)

# Menyiapkan lebar dan tinggi
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Titik awal pilih di pusat
x = width // 2 # agar menjadi integer
y = height // 2

# Width dan height untuk rectangle
w = width // 4
h = height // 4

while True:
    
    ret, frame = cap.read()
    cv2.rectangle(frame, (x,y), (x+w, y+h), color=(0,255,0), thickness=4)
    cv2.imshow('video', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

'''
Membuat rectangle dengan 2x mouse clicks
'''

import cv2

# Fungsi mouse (callback) --> review di materi computer vision #4
def buat_rectangle(event,x,y,flags,param):
     
    global pt1, pt2, click1, click2
    
    if event == cv2.EVENT_LBUTTONDOWN:
        
        # Mereset rectangle-nya
        if click1 and click2:
            pt1 = (0,0)
            pt2 = (0,0)
            click1 = False
            click2 = False
        
        if click1 == False:
            pt1 = x,y
            click1 = True
        
        elif click2 == False:
            pt2 = x,y
            click2 = True
        

# Parameter global
pt1 = (0,0)
pt2 = (0,0)
click1 = False
click2 = False

# Mensetting webcam
cap = cv2.VideoCapture(0)

# Memberi nama window
cv2.namedWindow('video')

# Menghubungkan mouse kita dengan fungsi callback opencv sekaligus buat_rectangle
cv2.setMouseCallback('video', buat_rectangle)

while True:
    ret, frame = cap.read()
    
    if click1:
        cv2.circle(frame, center=pt1, radius=3, color=(0,255,0), thickness=-1)
    
    if click1 & click2:
        cv2.rectangle(frame, pt1, pt2, (0,255,0), 3)
    
    cv2.imshow('video', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()




