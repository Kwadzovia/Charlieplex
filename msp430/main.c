#include <msp430.h> 
#include "stdint.h"
#include "stdlib.h"
/**
 * main.c
 */


uint8_t getPortTri(unsigned const charliePin[3]);
uint8_t getPortLow(unsigned const charliePin[3]);
uint8_t getPortHigh(unsigned const charliePin[3]);
void setLED(unsigned const charliePortLUT[][3],uint8_t ledPIN,size_t MAX_SIZE);

int main(void)
{
	WDTCTL = WDTPW | WDTHOLD;	// stop watchdog timer
	
	PM5CTL0 &= ~LOCKLPM5;       // Exit low power mode

	unsigned const charliePortLUT[][3] = {
      {0x3,0x2,0x1},
      {0x3,0x1,0x2},
      {0x6,0x4,0x2},
      {0x6,0x2,0x4},
      {0x5,0x4,0x1},
      {0x5,0x1,0x4},
	};

	size_t MAX_ROWS_CHARLIE_LUT = sizeof(charliePortLUT)/sizeof(charliePortLUT[0]);

	volatile uint8_t infLoop = 1;
	uint16_t delayIndex = 0;
	uint8_t ledSelect = 0;
	while(infLoop){
	    //Range check on selected LED
	    if(ledSelect > MAX_ROWS_CHARLIE_LUT-1){
	        ledSelect = 0;
	    }

	    //Turn on next LED
	    setLED(charliePortLUT,ledSelect,MAX_ROWS_CHARLIE_LUT);
        ledSelect++;

	    //Short Delay
	    for(delayIndex = 0;delayIndex < 300;delayIndex++){}
	}
	return 0;
}



uint8_t getPortTri(unsigned const charliePin[3]){
    return ((uint8_t) charliePin[0]);
}
uint8_t getPortLow(unsigned const charliePin[3]){
    return ((uint8_t) charliePin[1]);
}
uint8_t getPortHigh(unsigned const charliePin[3]){
    return ((uint8_t) charliePin[2]);
}

void setLED(unsigned const charliePortLUT[][3] ,uint8_t ledPIN,size_t MAX_SIZE){


    //Range Check
    if(ledPIN >= MAX_SIZE){
        P6DIR |= 0x00;
        return;
    } else {
    //SET PORTS


        P6DIR = getPortTri(charliePortLUT[ledPIN]);
        P6OUT &= ~(getPortLow(charliePortLUT[ledPIN]));
        P6OUT |= getPortHigh(charliePortLUT[ledPIN]);
    }

}
