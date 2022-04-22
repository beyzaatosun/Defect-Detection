# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 01:29:05 2021

@author: Berke
"""

import os


f = r'' #images file path
for file in os.listdir(f):
    if file.endswith('.jpg'):
        f_img = f+"/"+file
        os.rename(r"yolov4\test\000.jpg",
              r"yolov4\test\Class6_.jpg")
