# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 00:31:33 2021

@author: User
"""

import PIL
import os
import os.path
from PIL import Image

f = r'' #images file path
for file in os.listdir(f):
    if file.endswith('.jpg'):
        f_img = f+"/"+file
        img = Image.open(f_img)
        img = img.resize((416,416))
        img.save(f_img)
