from __future__ import division
import time
import Adafruit_PCA9685

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
def stand():
	i=0
	if(i<6):
		set_servo_angle(i, 90)
		i+=1
		time.sleep(1)
	else:
		set_servo_angle(i,45)
		i+=1
pwm.set_pwm_freq (50)
x = 0
d = 0
while(d!=-1):
	print("input the servo num and angle")
	x = int(input())
	d = int(input())
	set_servo_angle (x, d)
	#stand()

# pwm. set pwm (4, 0, 300)
# time. sleep (1)
# pwm. set pwm (5, 0, 300)
# time. sleep (1)

