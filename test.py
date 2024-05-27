import time
import wiringpi as GPIO
while 1:
	x=0
	sum1=0.0
	while x<10:
		GPIO.delay(100)
		with open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw","r",encoding='UTF-8')as vo10:
			vol10 = int(vo10.read())
			res = (vol10/4096)*1.8
			x+=1
			sum1 += res
	res1 = sum1/10
	with open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw","r",encoding='UTF-8')as vo10:
			vol10 = int(vo10.read())
			res3 = (vol10/4096)*1.8
	res2 = ((res3-res1)/3)*1000
	if abs(res2)>2:
		print("Waring! the gas temp is %",'%.2f'% abs(res2))
	else:
		print("GAS sencer do not scan gas")
