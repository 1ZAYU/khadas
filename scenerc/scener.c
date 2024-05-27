#include <stdio.h>
#include <wiringPi.h>
 
const int gpio_pin =2;

int main()
{
	wiringPiSetup();
    pinMode(gpio_pin,OUTPUT);
 
    while(1){
        digitalWrite(gpio_pin,HIGH);
        printf("wPi Pin %d now is GIGH\n",gpio_pin);
        delay(100);
        digitalWrite(gpio_pin,LOW);
        printf("wPi Pin %d now is LOW\n",gpio_pin);
        delay(100);
    }
 
    return 0;
}
