import cv2
from collections import Counter
from module import findnameoflandmark,findpostion,speak
import math

import os
from time import *


import RPi.GPIO as GPIO
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

cap = cv2.VideoCapture(0)
tip=[8,12,16,20]
tipname=[8,12,16,20]
fingers=[]
finger=[]


while True:

     ret, frame = cap.read()
     
     frame1 = cv2.resize(frame, (640, 480))

     
     a=findpostion(frame1)
     b=findnameoflandmark(frame1)
     
      
     
     if len(b and a)!=0:
        finger=[]
        if a[0][1:] < a[4][1:]: 
           finger.append(1)
           print (b[4])
           
           
          
           
                      
        else:
           finger.append(0)     
        
        
        
        fingers=[] 
        for id in range(0,4):
            if a[tip[id]][2:] < a[tip[id]-2][2:]:
               
               
               print(b[tipname[id]])
               
               if a[tip[2]] < a[tip[2]-2]:
                   kit.servo[0].angle = 50
               
                   
               
               
               fingers.append(1)
    
            else:
               fingers.append(0)
               
              
               
               
     x=fingers + finger
     c=Counter(x)
     up=c[1]
     down=c[0]
     print(up)
     print(down)
     
     
     cv2.imshow("Frame", frame1);
     key = cv2.waitKey(1) & 0xFF
    
    
    
     
    
        
      
     if up == 3:
        GPIO.output(17,GPIO.HIGH)
     
     if up == 0:
        GPIO.output(17,GPIO.LOW)
     
     
        
      
     
     
     
        
     
     if key == ord("q"):
        speak("sir you have"+str(up)+"fingers up  and"+str(down)+"fingers down") 
                    
     if key == ord("s"):
       break

