import cv2
import numpy as np
cap = cv2.VideoCapture(r"C:\Users\palas\Downloads\12th Fail (2023) [1080p] [WEBRip] [x265] [10bit] [5.1] [YTS.MX]\12th.Fail.2023.1080p.WEBRip.x265.10bit.AAC5.1-[YTS.MX].mp4")
if (cap.isOpened()== False):
   print("Error opening video file")
while(cap.isOpened()):
   ret, frame = cap.read()
   if ret == True:
     cv2.imshow('Frame', frame)
   if cv2.waitKey(250) & 0xFF == ord('q'):
      break
   else:
      break
cap.release()
cv2.destroyAllWindows()
