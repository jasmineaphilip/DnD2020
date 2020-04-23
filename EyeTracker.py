import cv2
from time import time
from gaze_tracking import GazeTracking
# import winsound
import os

TIMEOUT = 3
RECORD = False
start = time()

eye = GazeTracking()
cap = cv2.VideoCapture(0)
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 20, (int(cap.get(3)),int(cap.get(4))))

while True:
	# We get a new frame from the cap
    _, frame = cap.read()

    # We send this frame to GazeTracking to analyze it
    eye.refresh(frame)
    frame = eye.annotated_frame()

    if(eye.pupil_left_coords() is None):
    	cv2.putText(frame, "WARNING: EYES are CLOSED", (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)
    	cv2.putText(frame, "Time: " + "%.3f" %(time()-start), (90, 95), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)
    else:
    	start = time()

    if (int(time()) - int(start)) >= TIMEOUT:
    	print("WARNING ASLEEP WARNING ASLEEP")
    	# os.system('start scream.wav')
    	# winsound.PlaySound('scream.wav', winsound.SND_FILENAME)

    cv2.imshow("Eye Tracking", frame)
    if RECORD:
        out.write(frame)

    value = cv2.waitKey(1)
    if value == 27:
        break
    elif value == ord('r'):
        RECORD = not RECORD
        if RECORD:
            print("Recording Begins")
        else:
            print("Recording Ended")

cap.release()
out.release()
cv2.destroyAllWindows()
exit()
