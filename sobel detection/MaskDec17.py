import cv2

def score(pic, bkg, mas):
  # assumption:  pic, bkg and mask all have the same size
  cntRow, cntCol, cntCha = pic.shape
  error = 0
  for y in range(cntRow):
    for x in range(cntCol):
      mas_pix = mas[y, x] # pixel of mask
      mas_a = mas_pix[3]  # alpha of mask
      if (mas_a > 20):
        continue
      # we are now looking at a transparent mask pixel
      pic_pix = pic[y, x] # pixel of picture
      bkg_pix = bkg[y, x] # pixel of background
      pic_b, pic_g, pic_r = pic_pix[0], pic_pix[1], pic_pix[2]
      bkg_b, bkg_g, bkg_r = bkg_pix[0], bkg_pix[1], bkg_pix[2]
      err = abs(int(pic_r)-int(bkg_r)) + abs(int(pic_g)-int(bkg_g)) + abs(int(pic_b)-int(bkg_b))
      error += err
  return error


def findType(pic, bkg, maskTypes, masks):
  errors = []
  minErr = 99999999
  minMaskTypI = -1
  i = 0
  for m in masks:
    err = score(pic, bkg, m)
    if err < minErr:
      minErr = err
      minMaskTypI = i
    i += 1
    errors.append(err)
  print(f'The errors are:  {str(errors)},   minMaskTyp={maskTypes[minMaskTypI]}')
  return minMaskTypI


def findTypes(picNames, bkg, maskTypes, masks):
  for pn in picNames:
    pic = cv2.imread('Resources/'+pn+'.png')
    cv2.imshow(pn, pic)
    picTyp = findType(pic, bkg, maskTypes, masks)
    print(f'The type of pic {pn} is:  {str(maskTypes[picTyp])}')


bkg = cv2.imread('Resources/Background.png')
maskTypes = ['A', 'B', 'C', 'D']
masks = [cv2.imread('Resources/Mask_' + s + '.png', cv2.IMREAD_UNCHANGED) for s in maskTypes]


picNames = ['Ahw0001', 'Ahw0042', 'Ahw0099', 'Ahw0145', 'Ahw0148', 'Ahw0155', 'Ahw0238', 'Ahw0247']

findTypes(picNames, bkg, maskTypes, masks)


cv2.waitKey(0)

