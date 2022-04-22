# -*- coding: utf-8 -*-
"""
@author: User
"""
import cv2
import numpy as np
import os
from PIL import Image
from PIL import ImageEnhance

#SINGLE IMAGES
# Open the image.
# img = cv2.imread(r"")
  
# Trying 4 gamma values.
# for gamma in [0.1, 0.5, 1.4, 2.2]:
      
#     # Apply gamma correction.
#     gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8')
  
#     # Save edited images.
#     cv2.imwrite('2gamma_transformed'+str(gamma)+'.jpg', gamma_corrected)

#IN FILE ALL IMAGES
gamma = .7
f = r''
for file in os.listdir(f):
    if file.endswith('.jpg'):
        f_img = f+"/"+file
        img = cv2.imread(f_img)  
        gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8')
        cv2.imwrite(file, gamma_corrected)