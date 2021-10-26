# Task1
import machine
import time
led = machine.Pin(21, machine.Pin.OUT)
button = button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
while True:
    if not button.value():
        led.value(1)
        time.sleep(0.5)
        led.value(0)
        time.sleep(0.5)
