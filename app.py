import cv2
from PyLivestream import PyLivestream

print(cv2.__version__)


rtmp_url = "rtmp://210.99.70.120/live/cctv045.stream"

stream = PyLivestream()
stream.open(rtmp_url)

while True:
    frame = stream.get_frame()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

stream.close()
cv2.destroyAllWindows()