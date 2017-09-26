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
frame_count = 0
cap = cv2.VideoCapture(0)
#cap2 = cv2.VideoCapture(1)
while(True):
    _, frame = cap.read()
    #_, frame2 = cap2.read()
    if frame_count%frame_processing_ratio:
        frame = cv2.resize(frame, (0,0), fx=0.33, fy=0.33)
        faces = beesion.detect_faces_offline(frame)# offline
        if len(faces) == 1:
            cv2.imshow('frame',frame)
            _, img_png = cv2.imencode('.png', frame)
            croped_faces = list()
            face = faces[0]
            y,x,h,w = face
            frame2 = cv2.rectangle(frame, (x,y),(w,h),(0,255,0),2)
            if cv2.waitKey(1) & 0xFF == ord('c'):
                #faces = beesion.detect_faces(img_jpg.tobytes()) #google's
                try:
                    res = beesion.save_face_to_encodings(frame[y:h, w:x])
                    if res:
                        frame = cv2.putText(frame2, 'Imagen guardada', (20,200),cv2.FONT_HERSHEY_SIMPLEX, 4, (0,255,0), 4)
                    else:
                        frame = cv2.putText(frame2, "Por favor, no se mueva", (20,200),cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 2)
                except Exception as e:
                    logging.error(e)
                    frame = cv2.putText(frame2, "Por favor, no se mueva", (20,200),cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 2)
        cv2.imshow('frame',frame)
        # cv2.imshow('frame2',frame2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break
    frame_count+=1
    if frame_count>4:
        frame_count = 0 # avoid inifinite number
