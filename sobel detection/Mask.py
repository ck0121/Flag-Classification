import cv2
import numpy as np

pathBGD = 'Resources/Background.png'
pathA = 'Resources/Typa_A.png'
pathB = 'Resources/Typa_B.png'
pathC = 'Resources/Typa_C.png'
pathD = 'Resources/Typa_D.png'
pathTest = 'Resources/Ahw0145.png'

imgTest = cv2.imread(pathTest)
imgBGD = cv2.imread(pathBGD)
imgCopy = imgTest.copy()
maskA = cv2.imread(pathA)
maskB = cv2.imread(pathB)
maskC = cv2.imread(pathC)
maskD = cv2.imread(pathD)
rows,cols,channels = maskA.shape
sumA,sumB,sumC,sumD = 0,0,0,0
absA,absB,absC,absD = 0,0,0,0
cv2.imshow("Background",imgBGD)

for i in range(rows):
    for j in range(cols):
        for k in range(channels):
            if maskA[i][j][k] == 0 or maskA[i][j][k] == 255:
                continue
            else:
                imgCopy[i,j] = maskA[i,j]
        absA = np.abs(imgCopy[i][j]-imgBGD[i][j])
        sumA = sumA + absA
cv2.imshow("Type_A",imgCopy)

imgCopy = imgTest.copy()
for i in range(rows):
    for j in range(cols):
        for k in range(channels):
            if maskB[i][j][k] == 0 or maskB[i][j][k] == 255:
                continue
            else:
                imgCopy[i,j] = maskB[i,j]
        absB = np.abs(imgCopy[i][j],imgBGD[i][j])
        sumB = sumB + absB
cv2.imshow("Type_B",imgCopy)

imgCopy = imgTest.copy()
for i in range(rows):
    for j in range(cols):
        for k in range(channels):
            if maskC[i][j][k] == 0 or maskC[i][j][k] == 255:
                continue
            else:
                imgCopy[i,j] = maskC[i,j]
        absC = np.abs(imgCopy[i][j],imgBGD[i][j])
        sumC = sumC + absC
cv2.imshow("Tpye_C",imgCopy)

imgCopy = imgTest.copy()
for i in range(rows):
    for j in range(cols):
        for k in range(channels):
            if maskD[i][j][k] == 0 or maskD[i][j][k] == 255:
                continue
            else:
                imgCopy[i,j] = maskD[i,j]
        absD = np.abs(imgCopy[i][j],imgBGD[i][j])
        sumD = sumD + absD
cv2.imshow("Type_D",imgCopy)

print(sumA,sumB,sumC,sumD)
cv2.waitKey(0)


