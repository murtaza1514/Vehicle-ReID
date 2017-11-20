import numpy as np
import cv2
import threading

class CamThread (threading.Thread):
    def __init__(self, camName, camPath):
        threading.Thread.__init__(self)
        self.camPath = camPath
        self.camName = camName
    def run(self):
        cap = cv2.VideoCapture(self.camPath)
        while (True):
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            cv2.imshow(self.camName, gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cap.release()
                break



if __name__ == '__main__':
    cams = []
    while(True):
        address = input("Enter address to add new cam:")
        cam = CamThread("cam" + str(len(cams)), 0)
        cams.append(cam)
        cam.start()







'''
import numpy as np
import cv2

cap = cv2.VideoCapture("http://24.147.70.250:8081/mjpg/video.mjpg")

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
'''