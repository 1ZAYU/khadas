#include <stdio.h>
#include <wiringPi.h>
 
#define GP_INPUT 0
#define GP_OUTPUT 1
#define GP_OUTPUT_PIN 2
#define GP_INPUT_PIN 10
#define GP_INPUT_PIN2 11
#define GP_OUTPUT_HIGH 1
#define GP_OUTPUT_LOW 0
	

int main()
{
	wiringPiSetup();
	printf("GPIO STARTING\n");
	pinMode(GP_OUTPUT_PIN,OUTPUT);
	digitalWrite(GP_OUTPUT_PIN,0);
	delay(200);
	printf("---------set out put-----------\n");
	digitalWrite(GP_OUTPUT_PIN,0);
	delay(500);
	digitalWrite(GP_OUTPUT_PIN,1);
	delay(500);
	digitalWrite(GP_OUTPUT_PIN,0);
	delay(500);
	digitalWrite(GP_OUTPUT_PIN,1);
	pinMode(GP_INPUT_PIN,INPUT);
	pinMode(GP_INPUT_PIN2,INPUT);
	int result=1;
	while(1){
	result = digitalRead(GP_INPUT_PIN);
	if(result==0){
		delay(100);
		digitalWrite(GP_OUTPUT_PIN,0);
		delay(100);
		digitalWrite(GP_OUTPUT_PIN,1);
		delay(100);
		digitalWrite(GP_OUTPUT_PIN,0);
		delay(100);
		digitalWrite(GP_OUTPUT_PIN,1);
		delay(100);
		digitalWrite(GP_OUTPUT_PIN,0);
		delay(100);
		digitalWrite(GP_OUTPUT_PIN,1);
		delay(100);
		digitalWrite(GP_OUTPUT_PIN,0);
		delay(100);
		digitalWrite(GP_OUTPUT_PIN,1);
	}
	if(result!=0){
		printf("SENCER mode is normal \n");
	}else{
		printf("SENCER mode is waring \n");
		
		}
	digitalWrite(GP_OUTPUT_PIN,0);
	delay(200);
    }
 
    return 0;
}
