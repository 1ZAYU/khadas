#include <stdio.h>
#include <wiringPi.h>
 
#define outputpin1 2
 
int main()
{
    pinMode(outputpin1,OUTPUT);
 
    while(1){
        digitalWrite(outputpin1,HIGH);
        printf("wPi Pin %d now is GIGH\n",outputpin1);
        delay(200);
        digitalWrite(outputpin1,LOW);
        printf("wPi Pin %d now is LOW\n",outputpin1);
        delay(200);
    }
 
    exit(0);
}
