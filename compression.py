import cv2
import numpy as np

class Compress:
  def __init__(self, dimensions=(16, 9)):
    self.x_dim = dimensions[0]
    self.y_dim = dimensions[1]
  def compress(self, image_name=None, image_array=None, lvl=1):
    if image_name is not None:
      image = cv2.imread(image_name)
    elif image_array is not None:
      image = image_array
    return cv2.resize(image, (self.x_dim*lvl, self.y_dim*lvl), interpolation=cv2.INTER_AREA)
    
