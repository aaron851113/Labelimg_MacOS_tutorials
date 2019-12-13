# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 17:39:19 2018

@author: user
"""
import numpy as np
import cv2
import time 

video_path='114_TidingBlvd1-Gangqian-PSh_20191025_0700-1000_0013_0752-1252.avi'

interval=15 
video_capture = cv2.VideoCapture('video/'+video_path)
sucess=1
c=0

while(sucess):
    sucess, frame = video_capture.read()
    if (c%interval==0):
        savefigure_name = 'video_to_picture/'+str(c) + '.jpg'
        cv2.imwrite(savefigure_name, frame)
    c+=1
  
video_capture.release()



