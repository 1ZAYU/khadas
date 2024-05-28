import wiringpi as GPIO
     
INPUT = 0
OUTPUT = 1
OUTPUT_PIN = 3
INPUT_PIN = 10
INPUT_PIN2 = 11
OUTPUT_HIGH = 1
OUTPUT_LOW = 0
pinstatus_list = ['warning','normal']
GPIO.wiringPiSetup()
print("---------2222222-----------")
GPIO.pinMode(3,1)
GPIO.delay(1000)
print("---------set out put-----------")
GPIO.digitalWrite(3,0)
GPIO.delay(1000)
GPIO.digitalWrite(3,1)
GPIO.delay(1000)
GPIO.digitalWrite(3,0)
GPIO.delay(1000)
GPIO.digitalWrite(3,1)
GPIO.pinMode(OUTPUT_PIN,OUTPUT)
GPIO.pinMode(INPUT_PIN, INPUT)
GPIO.pinMode(INPUT_PIN2, INPUT)
GPIO.digitalWrite(3,0)
while 1:
	result = GPIO.digitalRead(INPUT_PIN)
	if(result==0):
		GPIO.pinMode(3,1)
		GPIO.delay(100)
		GPIO.digitalWrite(3,0)
		GPIO.delay(100)
		GPIO.digitalWrite(3,1)
		GPIO.delay(100)
		GPIO.digitalWrite(3,0)
		GPIO.delay(100)
		GPIO.digitalWrite(3,1)
		GPIO.delay(100)
		GPIO.digitalWrite(3,0)
		GPIO.delay(100)
		GPIO.digitalWrite(3,1)
		GPIO.delay(100)
		GPIO.digitalWrite(3,0)
		GPIO.delay(100)
		GPIO.digitalWrite(3,1)

	print('{}{}'.format('SENCER mode is  ', pinstatus_list[result]))
	GPIO.digitalWrite(OUTPUT_PIN, OUTPUT_LOW) 
	GPIO.delay(200)
	#print("TEST2")

	#result = GPIO.digitalRead(INPUT_PIN2)
	#print('{}{}'.format('The read Pin value is', result))
	#if(result==1):
	#	GPIO.digitalWrite(3,1) 
	  
		 
GPIO.delay(2000)
GPIO.digitalWrite(OUTPUT_PIN, OUTPUT_LOW) 
print("End")

