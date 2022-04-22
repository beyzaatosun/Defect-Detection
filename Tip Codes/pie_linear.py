# -*- coding: utf-8 -*-
"""
@author: User
"""

import cv2
import numpy as np
  
# Function to map each intensity level to output intensity level.
def pixelVal(pix, r1, s1, r2, s2):
    if (0 <= pix and pix <= r1):
        return (s1 / r1)*pix
    elif (r1 < pix and pix <= r2):
        return ((s2 - s1)/(r2 - r1)) * (pix - r1) + s1
    else:
        return ((255 - s2)/(255 - r2)) * (pix - r2) + s2
  
# Open the image.
img = cv2.imread('Sc_1.jpg')
  
# Define parameters.
r1 = 50
s1 = 0
r2 = 140
s2 = 100
  
# Vectorize the function to apply it to each value in the Numpy array.
pixelVal_vec = np.vectorize(pixelVal)
  
# Apply contrast stretching.
contrast_stretched = pixelVal_vec(img, r1, s1, r2, s2)
  
# Save edited image.
cv2.imwrite('Sc_1.jpg', contrast_stretched)