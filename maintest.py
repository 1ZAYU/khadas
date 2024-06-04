from __future__ import division
from multiprocessing import Process,Array
import time, Adafruit_PCA9685, cv2
pwm = Adafruit_PCA9685.PCA9685(busnum=3)
servo_min = 150
servo_max = 600

def set_servo_pulse(channel, pulse):
    pulse_length = 1000000
    pulse_length //= 60
    print ('{0}us per period'.format(pulse_length))
    pulse_length //= 4096
    print ('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)
    
def set_servo_angle (channe1, angle):
    angle=4096*((angle*11)+500)/20000
    pwm.set_pwm(channe1,0,int(angle))
def nine():
	i=0
	while(i<12):
		set_servo_angle(i, 90)
		i+=1
		time.sleep(1)
def stand():
	i=0
	while(i<12):
		if(i<6):
			set_servo_angle(i, 90)
			i+=1
			time.sleep(0.5)
		elif(i<9 and i>=6):
			set_servo_angle(i,135)
			i+=1
			time.sleep(0.5)
		elif(i<12 and i>=9):
			set_servo_angle(i,45)
			i+=1
			time.sleep(0.5)
def go1():
	set_servo_angle(6,45)
	set_servo_angle(8,45)
	set_servo_angle(10,135)
	time.sleep(0.5)
	set_servo_angle(0,60)
	set_servo_angle(2,60)
	set_servo_angle(4,120)
	time.sleep(0.5)
	set_servo_angle(6,135)
	set_servo_angle(8,135)
	set_servo_angle(10,45)
	time.sleep(0.5)
	set_servo_angle(0,90)
	set_servo_angle(2,90)
	set_servo_angle(4,80)
	
	set_servo_angle(9,135)
	set_servo_angle(11,135)
	set_servo_angle(7,45)
	time.sleep(0.5)
	set_servo_angle(3,120)
	set_servo_angle(5,120)
	set_servo_angle(1,60)
	time.sleep(0.5)
	set_servo_angle(9,45)
	set_servo_angle(11,45)
	set_servo_angle(7,135)
	time.sleep(0.5)
	set_servo_angle(3,90)
	set_servo_angle(5,90)
	set_servo_angle(1,90)	
def go2():
	set_servo_angle(9,90)
	time.sleep(0.3)
	set_servo_angle(3,120)
	time.sleep(0.3)
	set_servo_angle(9,45)
	time.sleep(0.3)
	set_servo_angle(6,90)
	time.sleep(0.3)
	set_servo_angle(0,60)
	time.sleep(0.3)
	set_servo_angle(6,135)
	time.sleep(0.3)
	set_servo_angle(10,90)
	time.sleep(0.3)
	set_servo_angle(4,120)
	time.sleep(0.3)
	set_servo_angle(10,45)
	time.sleep(0.3)
	
	set_servo_angle(7,90)
	time.sleep(0.3)
	set_servo_angle(1,60)
	time.sleep(0.3)
	set_servo_angle(7,135)
	time.sleep(0.3)
	
	set_servo_angle(8,90)
	time.sleep(0.3)
	set_servo_angle(2,70)
	time.sleep(0.3)
	set_servo_angle(8,135)
	
	
	time.sleep(0.3)
	set_servo_angle(11,90)
	time.sleep(0.3)
	set_servo_angle(5,110)
	time.sleep(0.3)
	set_servo_angle(11,45)
	time.sleep(0.3)
	
	set_servo_angle(0,90)
	set_servo_angle(1,90)
	set_servo_angle(3,90)
	set_servo_angle(4,90)
	set_servo_angle(2,135)
	set_servo_angle(5,45)
	time.sleep(0.3)
def opencvfowlling():
	global face_cascade
	global cap
	global r, f
	global h, w, ch
	global center_x1
	global center_y1
	global f_x,f_y,f_w,f_h
	global countt
	global flipped_frame
	st=0
	sumx=0 
	sumy=0
	while st<3:
		time.sleep(0.2)
				# 读取相机画面
		ret, frame = cap.read()
				# 画面水平翻转
		flipped_frame = cv2.flip(frame, 1)  # 0时为垂直翻转
				# 获取画面的宽度和高度
		height, width, channels = flipped_frame.shape
				# 计算中心点的坐标
		center_x = int(width / 2)
		center_y = int(height / 2)

				# 正方形的边长
		length = 120
				# 左上角的xy坐标
		left_up_x = int(center_x - (length / 2))  # 因为原点在正方形的中心，处于一半的位置，所以左上角的x坐标需要边长除以2
		left_up_y = int(center_y - (length / 2))
				# 画红色的正方形
		cv2.rectangle(flipped_frame, (left_up_x, left_up_y), (left_up_x + length, left_up_y + length), (0, 0, 255),
							  3)

				# 将帧转换为灰度图像
		gray = cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2GRAY)

				# 进行人脸检测
				# 检测设置，将图片放大1.1倍（一般设1.1倍，看效果而定）
				# 重复检测的次数为6次（检测次数越多，速度越慢，检测也越严格，准确率可能有所提升）
				# 最小的检测框为100*100的正方形，以上的会显示，以下的被屏蔽
		faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6, minSize=(100, 100))

				# 在帧中标记人脸
		for (x, y, w, h) in faces:
			f_x, f_y, f_w, f_h = x, y, w, h
			cv2.rectangle(flipped_frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

				# 计算人脸正方形的中心点坐标
		if len(faces) > 0:  # 判断人脸的数量是否>0
			f_z_x = int(f_x + (f_w / 2))
			f_z_y = int(f_y + (f_h / 2))
			#print("脸部中心x:", f_z_x, "脸部中心y:",  f_z_y)
		else:
			f_z_x, f_z_y = center_x, center_y  # 没有人脸时就默认人脸位置居中，防止后续使用舵机云台时乱动
			#print("脸部中心x:", f_z_x, "脸部中心y:",  f_z_y)

				# 计算人脸中心与画面中心相差的坐标
		difference_value_x = f_z_x - center_x
		difference_value_y = f_z_y - center_y
		#print("x坐标偏移量为：", difference_value_x, "y坐标偏移量为：", difference_value_y)
							# 显示相机画面
		#cv2.imshow("Face following...", flipped_frame)
		countt+=1
		st+=1
		sumx+=difference_value_x
		sumy+=difference_value_y
		#return flipped_frame
	print("----",countt)
	print("x坐标偏移量为：", sumx/3, "y坐标偏移量为：", sumy/3)
	sumx=0
	sumy=0
pwm.set_pwm_freq (50)
x = 0
d = 0
n=0
i=0
countt=0
cv2.namedWindow("Camera Feed")
face_cascade = cv2.CascadeClassifier('/home/khadas/Desktop/testxml.xml')
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
cap.set(cv2.CAP_PROP_FOURCC, fourcc)

# 设置分辨率
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 240)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)
r, f = cap.read()
h, w, ch = f.shape
print("输出画面的高度和宽度", h, w)
center_x1 = int(w / 2)
center_y1 = int(h / 2)
print("输出中心坐标为：", center_x1, center_y1)
f_x = f_y = f_w = f_h = None
flipped_frame = 0 

def main():
	global n,i
	#stand()
	print("input the step num")
	#i = int(input())
	i=5
	while n<i:
		opencvfeed = Process(target = opencvfowlling)
		n+=1
		opencvfeed.start()
		time.sleep(1)
		if(opencvfeed.is_alive):
			opencvfeed.terminate()


if __name__=='__main__':
	main()
