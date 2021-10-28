# Task 3
import machine
import time
ledgreen = machine.Pin(21, machine.Pin.OUT)
ledorange = machine.Pin(26, machine.Pin.OUT)
ledred = machine.Pin(25, machine.Pin.OUT)
sensor = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(23))
address = 24
temp_reg = 5
res_reg = 8

def temp_c(data):
    value = data[0] << 8 | data[1]
    temp = (value & 0xFFF) / 16.0
    if value & 0x1000:
        temp -= 256.0
    return temp

while True:
    data = bytearray(2)
    sensor.readfrom_mem_into(address, temp_reg, data)
    time.sleep(0.01)
    print(temp_c(data))
    if temp_c(data) < 25:
        ledgreen.value(1)
        ledorange.value(0)
        ledred.value(0)
    elif temp_c(data) > 28:
        ledgreen.value(0)
        ledorange.value(0)
        ledred.value(1)
    else:
        ledgreen.value(0)
        ledorange.value(1)
        ledred.value(0)
        
        