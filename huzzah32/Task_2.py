#Task 2 second attempt

import machine
import time
#Defining the different led's to their respective call pin numbers
ledgreen = machine.Pin(21, machine.Pin.OUT)
ledorange = machine.Pin(26, machine.Pin.OUT)
ledred = machine.Pin(25, machine.Pin.OUT)
#The button is also defined to the call pin number
button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
#Creating a counter, to keep track of the order in which the led's light up
i = 0
#turning the green led on from the beginning
ledgreen.value(1)
#infinite outer loop
while True:
    #the button value is read twice with 0.01 seconds between the readings
    first = button.value()
    time.sleep(0.01)
    second = button.value()
    #If the first reading is true, i.e the button is not pushed
    #and the second reading is false, i.e the button is pushed
    #then the if condition is true and the inner loop runs.  
    if first and not second:
        #after first push the green is turned off
        #the orange is turned on
        #the counter is increased
        if i == 0:
            ledgreen.value(0)
            ledorange.value(1)
            ledred.value(0)
            i = i+1
        #after second push the orange is turned off
        #the red is turned on
        #the counter is increased
        elif i == 1:
            ledgreen.value(0)
            ledorange.value(0)
            ledred.value(1)
            i = i+1
        #after third push the red is turned off
        #the green is turned on
        #the counter is reset to 0
        #the cycle can start over
        elif i == 2:
            ledgreen.value(1)
            ledorange.value(0)
            ledred.value(0)
            i = 0
    #If the button continues to be pushed, then both the first and second will be false
    #and the if condition is false, so it doesnt run, so one click only counts as one click
    #regardless of how long the click is
    