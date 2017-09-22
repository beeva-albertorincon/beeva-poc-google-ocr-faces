# encoding:utf8
import numpy as np
import cv2
import base64
import beesion

import time

import logging
logging.basicConfig(format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

frame_processing_ratio = 4
cap = cv2.VideoCapture(0)
#cap2 = cv2.VideoCapture(1)
while(True):
    _, frame = cap.read()
    #_, frame2 = cap2.read()
    if n%frame_processing_ratio:
        frame = cv2.resize(frame, (0,0), fx=0.33, fy=0.33)
        if cv2.waitKey(1) & 0xFF == ord('c'):
            _, img_png = cv2.imencode('.png', frame)
            beesion.detect_text_front(img_png.tobytes())
        _, img_png = cv2.imencode('.png', frame)
        #faces = beesion.detect_faces(img_jpg.tobytes()) #google's
        faces = beesion.detect_faces_offline(frame)# offline
        if len(faces) == 2:
            cv2.imshow('frame',frame)
            croped_faces = list()
            for face in faces:
                y,x,h,w = face
                frame = cv2.rectangle(frame, (x,y),(w,h),(0,255,0),2)
                croped_faces.append(frame[y:h, w:x])
                #cv2.imshow('Face detected', frame[y:h, w:x])
                # x,y,h,w = face #google's method
                # frame = cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                # croped_faces.append(frame[y:y+h, x:x+h])
                #cv2.imshow('Face detected', frame[y:y+h, x:x+h])
            verification_result = beesion.verify_face(croped_faces[0], croped_faces[1])
            logging.info(verification_result)
            if verification_result and verification_result[0] == True:
                frame = cv2.putText(frame, 'Acceso permitido', (20,200),cv2.FONT_HERSHEY_SIMPLEX, 4, (0,255,0), 4)
                while(cv2.waitKey(1) & 0xFF != ord('q')):
                    cv2.imshow('frame',frame)
            elif verification_result and verification_result[0] == False:
                frame = cv2.putText(frame, "Acceso denegado", (20,200),cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 2)
            else:
                frame = cv2.putText(frame, "Por favor, no se mueva", (20,200),cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 2)
        cv2.imshow('frame',frame)
        # cv2.imshow('frame2',frame2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break
    n+=1
    if n>4:
        n = 0 # avoid inifinite number
# When everything done, release the capture
