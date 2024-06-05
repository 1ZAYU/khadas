import cv2

print("input the camaer num")
t = input()
if t==1:
	cap.set(cv2.CAP_PROP_FRAME_WIDTH, 240)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)
	if t==0:
		cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
		cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap = cv2.VideoCapture(t)
if not cap.isOpened():
    print("open failed")
    exit()

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
cap.set(cv2.CAP_PROP_FOURCC, fourcc)

def get_fourcc_str(cap):
    fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
    return "".join([chr((fourcc >> 8 * i) & 0xFF) for i in range(4)])

print("强制设置格式后的格式:", get_fourcc_str(cap))

while True:
    ret, frame = cap.read()
    if not ret:
        print("无法接收帧（流结束？）")
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
