#Task 2 second attempt

import machine
import time
ledgreen = machine.Pin(21, machine.Pin.OUT)
ledorange = machine.Pin(26, machine.Pin.OUT)
ledred = machine.Pin(25, machine.Pin.OUT)
button = button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
i = 0
ledgreen.value(1)
while True:
    first = button.value()
    time.sleep(0.01)
    second = button.value()
    if first and not second:
        if i == 0:
            ledgreen.value(0)
            ledorange.value(1)
            ledred.value(0)
            i = i+1
        elif i == 1:
            ledgreen.value(0)
            ledorange.value(0)
            ledred.value(1)
            i = i+1
        elif i == 2:
            ledgreen.value(1)
            ledorange.value(0)
            ledred.value(0)
            i = 0

    