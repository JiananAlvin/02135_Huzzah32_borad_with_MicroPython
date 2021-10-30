# Task1
import machine
import time
# Defining the led to its call pin number
led = machine.Pin(21, machine.Pin.OUT)
button = button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
#Create an infinite loop
while True:
    # button.value is a boolean, so when its true, the button is not pushed
    # when not true the button is pushed
    if not button.value():
        led.value(1)
        time.sleep(0.5)
        led.value(0)
        time.sleep(0.5)
        #The sleep timer makes the led be on for half a second, then off for half a second
        #resulting in a blinking frequency of 1Hz
