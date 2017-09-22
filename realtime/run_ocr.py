# encode:utf8
import numpy as np
import cv2
import base64
import beesion


cap = cv2.VideoCapture(0)
n = 0
while(True):
    # Capture frame-by-frame
    _, frame = cap.read()
    # Our operations on the frame come here
    if cv2.waitKey(1) & 0xFF == ord('c'):
        _, img_png = cv2.imencode('.png', frame)
        try:
            text = beesion.detect_text_front(img_png.tobytes())
            text = ','.join(text)
            frame = cv2.putText(frame, "%s" %(text), (10,200),cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 4)
            while(cv2.waitKey(1) & 0xFF != ord('q')):
                cv2.imshow('frame',frame)
            with open('people.csv', 'a') as f:
                f.write(text+'\n')
        except Exception as e:
            print(e)
            frame = cv2.putText(frame, "Failed!", (10,200),cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 4)
            while(cv2.waitKey(1) & 0xFF != ord('q')):
                cv2.imshow('frame',frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    n+=1
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
