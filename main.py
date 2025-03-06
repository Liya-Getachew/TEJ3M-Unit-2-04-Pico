"""
Created by Liya G. 
Created on March 4th 2025

This turns an RGB LED on, cycling through the colors. 
"""

import time
import board
import digitalio

LED_GREEN = digitalio.DigitalInOut(board.GP11)
LED_BLUE = digitalio.DigitalInOut(board.GP12)
LED_RED = digitalio.DigitalInOut(board.GP13)

LED_GREEN.direction = digitalio.Direction.OUTPUT
LED_BLUE.direction = digitalio.Direction.OUTPUT
LED_RED.direction = digitalio.Direction.OUTPUT

blink_time = 1

# loop forever
while True:
    # GREEN
    LED_GREEN.value = True
    LED_BLUE.value = False
    LED_RED.value = False 
    time.sleep(blink_time) 

    # BLUE
    LED_GREEN.value = False
    LED_BLUE.value = True 
    LED_RED.value = False
    time.sleep(blink_time) 

    # RED
    LED_GREEN.value = False
    LED_BLUE.value = False 
    LED_RED.value = True
    time.sleep(blink_time) 

    # YELLOW
    LED_GREEN.value = True
    LED_BLUE.value = False 
    LED_RED.value = True
    time.sleep(blink_time)  

    # CYAN
    LED_GREEN.value = True
    LED_BLUE.value = True 
    LED_RED.value = False
    time.sleep(blink_time) 

    # MAGENTA
    LED_GREEN.value = False
    LED_BLUE.value = True 
    LED_RED.value = True
    time.sleep(blink_time)   

    # GREEN
    LED_GREEN.value = True
    LED_BLUE.value = True 
    LED_RED.value = True
    time.sleep(blink_time) 

