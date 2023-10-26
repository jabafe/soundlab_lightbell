import neopixel
from machine import Pin
import time

ws_pin1 = 28
ws_pin2 = 26
bell_sw = Pin(27, Pin.IN, Pin.PULL_UP)
led_num1 = 16
led_num2 = 32
brightness = 1 # flash
brightness2 = 0.01 # control light
bell_cnt = 24 # how often it flashes
bell_speed = 1000 # bell interval time
speed = 40 # flash light time

neoRing1 = neopixel.NeoPixel(Pin(ws_pin1), led_num1)
neoRing2 = neopixel.NeoPixel(Pin(ws_pin2), led_num2)

# control LED brightness for flash light and control light(outside)
def set_brightness(color):
    r, g, b = color
    r = int(r * brightness)
    g = int(g * brightness)
    b = int(b * brightness)
    return(r, g, b)

def set_brightness2(color):
    r, g, b = color
    r = int(r * brightness2)
    g = int(g * brightness2)
    b = int(b * brightness2)
    return(r, g, b)

# flash bell function
def flash():
    color = (255, 255, 255)
    color = set_brightness(color)
    neoRing1.fill(color)
    neoRing1.write()
    time.sleep_ms(speed)

# LEDs off
def dark():
    color = (0, 0, 0)
    neoRing1.fill(color)
    neoRing1.write()

# red LEDs indicate switch is used
def dingdong():
    color = (255, 0, 0)
    color = set_brightness2(color)
    neoRing2.fill(color)
    neoRing2.write()

# green LEDs indicate bell is ready
def idle():
    dark()
    color = (0, 255, 0)
    color = set_brightness2(color)
    neoRing2.fill(color)
    neoRing2.write()

# function for the bell itself
def ringding():
    dingdong()
    for i in range(1, bell_cnt):
        flash()
        dark()
        time.sleep_ms(bell_speed)

while True:
    bell = bell_sw.value()
    if bell != True:
        ringding()
    else:
        idle()
