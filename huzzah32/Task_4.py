# Task 4
import machine, neopixel
import time

np = neopixel.NeoPixel(machine.Pin(21), 2)
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

np[0] = (0, 0, 0)
np[1] = (0, 0, 0)
np.write()

while True:
    data = bytearray(2)  
    sensor.readfrom_mem_into(address, temp_reg, data)
    time.sleep(0.01)
    print(temp_c(data))
    if temp_c(data) < 25:
        np[0] = (255, 0, 0)
        np[1] = (255, 0, 0)
    elif temp_c(data) > 28:
        np[0] = (0, 255, 0)
        np[1] = (0, 255, 0)
    else:
        np[0] = (128, 128, 0)
        np[1] = (128, 128, 0)
    np.write()
