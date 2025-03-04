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

blink_time = 1000

# loop forever
while True:
    LED_GREEN.value = True # GREEN
    time.sleep(blink_time) 
    LED_GREEN.value = False 
    time.sleep(blink_time) 

    LED_BLUE.value = True # BLUE
    time.sleep(blink_time) 
    LED_BLUE.value = False 
    time.sleep(blink_time)

    LED_RED.value = True # RED
    time.sleep(blink_time) 
    LED_RED.value = False 
    time.sleep(blink_time) 

    LED_RED.value = True # YELLOW
    LED_GREEN.value = True 
    time.sleep(blink_time) 
    LED_RED.value = False 
    LED_GREEN.value = False 
    time.sleep(blink_time)  

    LED_BLUE.value = True # CYAN
    LED_GREEN.value = True 
    time.sleep(blink_time) 
    LED_BLUE.value = False 
    LED_GREEN.value = False 
    time.sleep(blink_time) 

    LED_BLUE.value = True # MAGENTA
    LED_RED.value = True 
    time.sleep(blink_time) 
    LED_BLUE.value = False 
    LED_RED.value = False 
    time.sleep(blink_time)  

    LED_GREEN.value = True # WHITE
    LED_BLUE.value = True
    LED_RED.value = True 
    time.sleep(blink_time)
    LED_GREEN.value = False  
    LED_BLUE.value = False 
    LED_RED.value = False 
    time.sleep(blink_time) 

