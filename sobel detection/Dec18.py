import cv2


# find the number of different pixels between pic1 and pic2 outside the mask
# def outsideDiffArea(pic1, pic2, mask):
#   thold_alpha = 20  # threshold for mask boundary
#   thold_diff  = 30  # threshold for pixel difference between pic1 and pic2
#   cntRow, cntCol, cntCha = pic1.shape  # assumption:  pic1, pic2 and mask all have the same width and height
#   diffArea = 0 # number of different pixels between pic1 and pic2
#   for y in range(cntRow):
#     for x in range(cntCol):
#       if (mask[y, x][3] > thold_alpha): # alpha of mask pixel
#         continue
#       # we are now looking at a transparent mask pixel (outside the mask)
#       pic1_pix = pic1[y, x] # pixel of picture1
#       pic2_pix = pic2[y, x] # pixel of picture2
#       b1, g1, r1 = pic1_pix[0], pic1_pix[1], pic1_pix[2]
#       b2, g2, r2 = pic2_pix[0], pic2_pix[1], pic2_pix[2]
#       diff = abs(int(r2)-int(r1)) + abs(int(g2)-int(g1)) + abs(int(b2)-int(b1))
#       if diff > thold_diff:
#         diffArea += 1
#   return diffArea

def error(pic1, pic2, mask):
  thold_alpha = 20  # threshold for mask boundary
  thold_diff  = 30  # threshold for pixel difference between pic1 and pic2
  cntRow, cntCol, cntCha = pic1.shape  # assumption:  pic1, pic2 and mask all have the same width and height
  diffArea = 0 # number of different pixels between pic1 and pic2
  areaDiffOut = 0
  areaSameIn  = 0
  for y in range(cntRow):
    for x in range(cntCol):
      if(mask[y, x][3] < thold_alpha):
        pic1_pix = pic1[y, x]  # pixel of picture1
        pic2_pix = pic2[y, x]  # pixel of picture2
        b1, g1, r1 = pic1_pix[0], pic1_pix[1], pic1_pix[2]
        b2, g2, r2 = pic2_pix[0], pic2_pix[1], pic2_pix[2]
        diff = abs(int(r2) - int(r1)) + abs(int(g2) - int(g1)) + abs(int(b2) - int(b1))
        if diff > thold_diff:
          areaSameIn += 1
      else:
        pic1_pix = pic1[y, x]  # pixel of picture1
        pic2_pix = pic2[y, x]  # pixel of picture2
        b1, g1, r1 = pic1_pix[0], pic1_pix[1], pic1_pix[2]
        b2, g2, r2 = pic2_pix[0], pic2_pix[1], pic2_pix[2]
        diff = abs(int(r2) - int(r1)) + abs(int(g2) - int(g1)) + abs(int(b2) - int(b1))
        if diff > thold_diff:
          areaDiffOut += 1
  return areaDiffOut + areaSameIn





def findType(picName, pic, bkg, maskTypes, masks):
  areas = [0] * len(masks)  # not used here yet, may be useful later
  minArea = 0
  minAreaI = 0
  areasStr = ''
  for i in range(len(masks)):
    areas[i] = area = error(pic, bkg, masks[i])
    if i == 0:
      minArea = area
    elif area < minArea:
      minArea = area
      minAreaI = i
    areasStr += f'{area:6d}'
  # area = number of different pixels between pic and bkg outside the masks
  print(f'{picName}   areas=[{areasStr} ]   typ={maskTypes[minAreaI]}')
  return minAreaI



def findTypes(picNames, bkg, maskTypes, masks):
  for pn in picNames:
    pic = cv2.imread('Resources/'+pn+'.png')
    cv2.imshow(pn, pic)
    findType(pn, pic, bkg, maskTypes, masks)


bkg = cv2.imread('Resources/Background.png')
maskTypes = ['A', 'B', 'C', 'D']
masks = [cv2.imread('Resources/Mask_' + s + '.png', cv2.IMREAD_UNCHANGED) for s in maskTypes]
picNames = ['Ahw0001', 'Ahw0042', 'Ahw0099', 'Ahw0145', 'Ahw0148', 'Ahw0155', 'Ahw0238', 'Ahw0247']


findTypes(picNames, bkg, maskTypes, masks)

cv2.waitKey(0)