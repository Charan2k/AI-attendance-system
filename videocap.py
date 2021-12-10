import cv2 as cv
import numpy as np
import os
def camon():
    framep=[]
    casc = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

    frame = cv.VideoCapture(0)
    try:
      

        if not os.path.exists('data'):
            os.makedirs('data')
  
    
    except OSError:
        print ('Error: Creating directory of data')
  
#frames
    currentframe = 0
    while frame:
        ret, frame1 = frame.read()
        grey = cv.cvtColor(frame1,cv.COLOR_BGR2GRAY)
        
        faces = casc.detectMultiScale(grey, 1.1,4)
        
        for (a,b,c,d) in faces:
            
            # cv.rectangle(frame1,(a,b),(a+c, b+d),(255,0,0),2)
            framep.append(frame1[b:b+d, a:a+c])


        cv.imshow('video',frame1)
        for i in framep:
            cv.imshow('cutfrm',i)
            if ret:
        
                name = './data/frame' + str(currentframe) + '.jpg'
                print ('Create' + name)
        
                
                cv.imwrite(name, i)
                # print(faces)
                currentframe +=1
            
            if currentframe == 100:
                break
            
            
        if cv.waitKey(1) & 0xFF == ord('c'):
            break

        
    frame.release()
    cv.destroyAllWindows() 
camon()
    
