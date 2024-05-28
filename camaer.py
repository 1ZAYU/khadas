import wiringpi as GPIO
GPIO.wiringPiSetup()
print("---------2222222-----------")
GPIO.pinMode(18,1)
while 1:
	GPIO.delay(100)
	result = GPIO.digitalRead(18)
	print("the voltage is",result)
9
