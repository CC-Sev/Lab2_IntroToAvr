/*	Author: lab
 *  Partner(s) Name: roz
 *	Lab Section:
 *	Assignment: Lab #  Exercise #
 *	Exercise Description: [optional - include for your own benefit]
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */
#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

int main(void) {
    /* Insert DDR and PORT initializations */
	DDRA = 0x00; PORTA = 0xFF;
	DDRB = 0x00; PORTB = 0xFF;
	DDRC = 0x00; PORTC = 0x00;
	DDRD = 0xFF; PORTD = 0x00;
    /* Insert your solution below */
    
    unsigned char temp = 0x00;
    unsigned char totalWeight = 0x00;
    unsigned short difference = 0x00;

    while (1) {
    	
	temp = 0;
	totalWeight = 0x00;
	difference = 0x00;
	
	totalWeight = PINA + PINB + PINC;
	temp = totalWeight >> 2;
	temp = temp & 0xFC;

	if(totalWeight > 140){
		temp = temp | 0x01;
	}

	difference = PINA - PINC;

	if(difference >= 80){
		temp = temp | 0x02;
	}

	PORTD = temp;	
    }
    return 0;
}
