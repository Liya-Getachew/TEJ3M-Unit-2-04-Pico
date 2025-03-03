"""
Created by Liya G. 
Created on March 4th 2025

This turns an RGB LED on, cycling through the colors. 
"""

import time
import board
import digitalio

led_green = digitalio.DigitalInOut(board.GP11)
led_blue = digitalio.DigitalInOut(board.GP12)
led_red = digitalio.DigitalInOut(board.GP13)

led_green.direction = digitalio.Direction.OUTPUT
led_blue.direction = digitalio.Direction.OUTPUT
led_red.direction = digitalio.Direction.OUTPUT

blink_time = 1000

# loop forever
while True:
    led_green.value = True # GREEN
    time.sleep(blink_time) 
    led_green.value = False 
    time.sleep(blink_time) 

    led_blue.value = True # BLUE
    time.sleep(blink_time) 
    led_blue.value = False 
    time.sleep(blink_time)

    led_red.value = True # RED
    time.sleep(blink_time) 
    led_red.value = False 
    time.sleep(blink_time) 

    led_red.value = True # YELLOW
    led_green.value = True 
    time.sleep(blink_time) 
    led_red.value = False 
    led_green.value = False 
    time.sleep(blink_time)  

    led_blue.value = True # CYAN
    led_green.value = True 
    time.sleep(blink_time) 
    led_blue.value = False 
    led_green.value = False 
    time.sleep(blink_time) 

    led_blue.value = True # MAGENTA
    led_red.value = True 
    time.sleep(blink_time) 
    led_blue.value = False 
    led_red.value = False 
    time.sleep(blink_time)  

    led_green.value = True # WHITE
    led_blue.value = True
    led_red.value = True 
    time.sleep(blink_time)
    led_green.value = False  
    led_blue.value = False 
    led_red.value = False 
    time.sleep(blink_time) 

