# Task 3
import machine
import time
#The led's are defined to their respective call pin number
ledgreen = machine.Pin(21, machine.Pin.OUT)
ledorange = machine.Pin(26, machine.Pin.OUT)
ledred = machine.Pin(25, machine.Pin.OUT)
#The sensor is defined to its clock line pin, and data line pin numbers
sensor = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(23))
#The regestry for data saved by the sensor is noted
address = 24
temp_reg = 5
res_reg = 8
#sensor reading data transformed to degrees celsius
#this piece of code was taken directly from the setup instructions
#and was not explained further
def temp_c(data):
    value = data[0] << 8 | data[1]
    temp = (value & 0xFFF) / 16.0
    if value & 0x1000:
        temp -= 256.0
    return temp
#Creating the outer infinite loop
while True:
    #data from the sensor is saved in a buffer array
    data = bytearray(2)
    sensor.readfrom_mem_into(address, temp_reg, data)
    #setting a short delay in between readings
    #this proved necissary to not overload the program with data
    time.sleep(0.01)
    #printing the actual temp readings in celcius to track on screen
    print(temp_c(data))
    #if the temperature is under 25 degrees the green light alone is on
    if temp_c(data) < 25:
        ledgreen.value(1)
        ledorange.value(0)
        ledred.value(0)
    #if the temperature is above 28 degrees the red light alone is on
    elif temp_c(data) > 28:
        ledgreen.value(0)
        ledorange.value(0)
        ledred.value(1)
    #for anything in between the yellow/orange light alone is on
    else:
        ledgreen.value(0)
        ledorange.value(1)
        ledred.value(0)
# the thresholds was found by testing the heat response from placing a finger on the sensor
        
        