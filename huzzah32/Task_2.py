#Task 2 second attempt

import machine
import time
# Defining the different led's to their respective call pin numbers
ledgreen = machine.Pin(21, machine.Pin.OUT)
ledorange = machine.Pin(26, machine.Pin.OUT)
ledred = machine.Pin(25, machine.Pin.OUT)
# The button is also defined to the call pin number
button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
# Creating a counter, to keep track of the order in which the led's light up
i = 0
# turning the green led on from the beginning
ledgreen.value(1)
# infinite outer loop
while True:
    # the button value is read twice with 0.01 seconds between the readings
    first = button.value()
    time.sleep(0.01)
    second = button.value()
    # If the first reading is true, i.e the button is not pushed
    # and the second reading is false, i.e the button is pushed
    # then the if condition is true and the inner loop runs.  
    if first and not second:
        # after first push
        if i == 0:
            ledgreen.value(0) # the green is turned off
            ledorange.value(1) # the orange is turned on
            ledred.value(0)
            i = i+1 # the counter is increased
        # after second push
        elif i == 1:
            ledgreen.value(0)
            ledorange.value(0) # the orange is turned off
            ledred.value(1) # the red is turned on
            i = i+1 # the counter is increased
        # after third push
        elif i == 2:
            ledgreen.value(1) # the green is turned on
            ledorange.value(0) 
            ledred.value(0) # the red is turned off
            i = 0 # the counter is reset to 0, the cycle can start over
    # If the button continues to be pushed, then both the first and second will be false
    # and the if condition is false, so it doesnt run, so one click only counts as one click
    # regardless of how long the click is
    