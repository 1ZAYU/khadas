import cv2
import time

cv2.namedWindow("Camera Feed")
face_cascade = cv2.CascadeClassifier('/home/khadas/Desktop/testxml.xml')
print("input the camaer num")
t = int(input())
cap = cv2.VideoCapture(t)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
cap.set(cv2.CAP_PROP_FOURCC, fourcc)
if t==1:
	cap.set(cv2.CAP_PROP_FRAME_WIDTH, 240)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)
	if t==0:
		cap.set(cv2.CAP_PROP_FRAME_WIDTH, 12)
		cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
r, f = cap.read()
h, w, ch = f.shape
print("camaer high and camaer weight:", h, w)
center_x1 = int(w / 2)
center_y1 = int(h / 2)
print("center of camaer：", center_x1, center_y1)
f_x = f_y = f_w = f_h = None
while True:
	ret, frame = cap.read()
	height, width, channels = frame.shape
	center_x = int(width / 2)
	center_y = int(height / 2)
	length = 90
	left_up_x = int(center_x - (length / 3)) 
	left_up_y = int(center_y - (length / 3))
	cv2.rectangle(frame, (left_up_x, left_up_y), (left_up_x + length, left_up_y + length), (0, 0, 255),3)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(60, 60))
	for (x, y, w, h) in faces:
		f_x, f_y, f_w, f_h = x, y, w, h
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

	if len(faces) > 0:
		f_z_x = int(f_x + (f_w / 2))
		f_z_y = int(f_y + (f_h / 2))
		print("face_center_x:", f_z_x, "face_cneter_y:",  f_z_y)
	else:
		f_z_x, f_z_y = center_x, center_y 
		print("cant found the face")


	cv2.imshow("feeding!!!",frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
