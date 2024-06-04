import cv2

# 打开指定的相机设备
cap = cv2.VideoCapture('/dev/video1')

# 检查相机是否成功打开
if not cap.isOpened():
    print("无法打开相机")
    exit()

# 强制设置视频格式为 MJPG
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
cap.set(cv2.CAP_PROP_FOURCC, fourcc)

# 设置分辨率
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 240)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

# 打印当前设置的格式
def get_fourcc_str(cap):
    fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
    return "".join([chr((fourcc >> 8 * i) & 0xFF) for i in range(4)])

print("强制设置格式后的格式:", get_fourcc_str(cap))

# 读取并显示视频帧
while True:
    ret, frame = cap.read()
    if not ret:
        print("无法接收帧（流结束？）")
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
