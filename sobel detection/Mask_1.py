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

def compare_img_hist(img1, img2):
    img1_hist = cv2.calcHist([img1], [1], None, [256], [0,256])
    img1_hist = cv2.normalize(img1_hist, img1_hist, 0, 1, cv2.NORM_MINMAX, -1)

    img2_hist = cv2.calcHist([img2], [1], None, [256], [0,256])
    img2_hist = cv2.normalize(img2_hist, img2_hist, 0, 1, cv2.NORM_MINMAX, -1)

    similarity = cv2.compareHist(img1_hist, img2_hist, 0)
    print(similarity)

    return similarity


for i in range(rows):
    for j in range(cols):
        for k in range(channels):
            if maskA[i][j][k] == 0 or maskA[i][j][k] == 255:
                continue
            else:
                imgCopy[i,j] = maskA[i,j]
        absA = np.abs(imgCopy[i][j],imgBGD[i][j])
        sumA = sumA + absA
new_img = imgCopy
cv2.imshow("Type_A",new_img)
compare_img_hist(imgBGD, new_img)

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
new_img2 = imgCopy
cv2.imshow("Type_C",new_img2)
compare_img_hist(imgBGD, new_img2)

print(sumA,sumB,sumC,sumD)
cv2.waitKey(0)
