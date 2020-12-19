import cv2



def peekImg(img):
  cntRow, cntCol, cntCha = img.shape
  print(f'cnt:  row={cntRow}  col={cntCol}  channel={cntCha}')
  print('display the pixel values in the RGBA order:')
  for y in range(cntRow):
    for x in range(cntCol):
      pix = img[y, x]
      b, g, r, a = pix[0], pix[1], pix[2], pix[3]
      print(f'[{r:3d} {g:3d} {b:3d} {a:3d}]',  end='  ')
    print()



tiny = cv2.imread('Resources/tiny.png', cv2.IMREAD_UNCHANGED)


peekImg(tiny)


cv2.waitKey(0)



