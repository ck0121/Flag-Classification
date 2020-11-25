import pygame
import numpy as np

C_white     = (255, 255, 255)
C_black     = (0, 0, 0)
C_gray      = (128, 128, 128)
C_red       = (200, 0, 0)
C_green     = (0, 200, 0)
C_b_red     = (255, 0, 0)
C_b_green   = (0, 255, 0)
C_blue      = (0, 0, 255)

# https://stackoverflow.com/questions/64183409/how-do-i-convert-an-opencv-cv2-image-bgr-and-bgra-to-a-pygame-surface-object
def cvImageToSurface(cvImage):
  if cvImage.dtype.name == 'uint16':
    cvImage = (cvImage / 256).astype('uint8')
  size = cvImage.shape[1::-1]
  if len(cvImage.shape) == 2:
    cvImage = np.repeat(cvImage.reshape(size[1], size[0], 1), 3, axis=2)
    format = 'RGB'
  else:
    format = 'RGBA' if cvImage.shape[2] == 4 else 'RGB'
    cvImage[:, :, [0, 2]] = cvImage[:, :, [2, 0]]
  surface = pygame.image.frombuffer(cvImage.flatten(), size, format)
  return surface.convert_alpha() if format == 'RGBA' else surface.convert()


