# Mengimpor library
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Live webcam
def harris_corner(gambar):
    
    # Merubah gambar ke grayscale
    gambar_abu = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)
    
    # Merubah menjadi numpy float (syarat algoritma)
    gambar_abu = np.float32(gambar_abu)
    
    # Mendeteksi dengan algoritma Harris
    sudut = cv2.cornerHarris(src=gambar_abu, 
                             blockSize=3, 
                             ksize=3, 
                             k=0.04)
    gambar_hitam = np.zeros((gambar.shape[0],gambar.shape[1],3),
                            np.uint8)
    
    # Menandai sudut dengan warna kuning
    gambar_hitam[sudut>0.005*sudut.max()] = [0,255,255] #BGR
    
    return gambar_hitam


def shi_tomasi(gambar):
    
    # Merubah gambar ke grayscale
    gambar_abu = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY) 
    
    # Mendeteksi sudut
    sudut = cv2.goodFeaturesToTrack(image=gambar_abu, 
                                    maxCorners=100, 
                                    qualityLevel=0.01, 
                                    minDistance=10)
    gambar_hitam = np.zeros((gambar.shape[0],gambar.shape[1],3),
                            np.uint8)
    sudut = np.int0(sudut)
    
    for titik in sudut:
        x,y = titik.ravel()
        #cv2.circle(gambar,(x,y),3,[0,255,255],-1)
        cv2.circle(gambar_hitam,(x,y),3,[0,255,255],-1)
    
    return gambar_hitam
    

# Deteksi sudut live dengan webcam
cap = cv2.VideoCapture(2, cv2.CAP_DSHOW) # cv2.CAP_DSHOW agar tidak error
while True:
    
    ret, frame = cap.read()
    frame = shi_tomasi(frame)
    cv2.imshow('Video Deteksi Sudut', frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
cap.release()
cv2.destroyAllWindows()