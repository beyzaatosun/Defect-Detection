# -*- coding: utf-8 -*-
"""
Created on Mon May 17 02:58:23 2021

@author: User
"""

import os
import os.path
from PIL import Image
from PIL import ImageEnhance

#SINGLE IMAGE
# img=Image.open(r"")    # Opening Image Path
# img_shr_obj=ImageEnhance.Sharpness(img)
# factor=1.7    # Specified Factor for Enhancing Sharpness
# e_i=img_shr_obj.enhance(factor)    #Enhances Image
# e_i.save("sharpness.jpg")   # Shows Enhanced Image

#IN FILE ALL IMAGES
f = r'' #Images file path
for file in os.listdir(f):
    if file.endswith('.jpg'):
        f_img = f+"/"+file
        img = Image.open(f_img)
        img=ImageEnhance.Sharpness(img)
        img=img.enhance(1.7)
        img.save(f_img)
