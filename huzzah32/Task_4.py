# Task 4
import machine, neopixel
import time

np = neopixel.NeoPixel(machine.Pin(21), 2) # create NeoPixel driver on GPIO21 for 2 pixels
# The sensor is defined to its clock line pin and data line pin numbers
sensor = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(23))
# The regestry for data saved by the sensor is noted
address = 24
temp_reg = 5
res_reg = 8
# sensor reading data transformed to degrees celsius
# this piece of code was taken directly from the setup instructions
# and was not explained further
def temp_c(data):
    value = data[0] << 8 | data[1]
    temp = (value & 0xFFF) / 16.0
    if value & 0x1000:
        temp -= 256.0
    return temp
# both pixels are turned off from the start
np[0] = (0, 0, 0)
np[1] = (0, 0, 0)
np.write() # write data to all pixels

# creating an infinite loop
while True:
    data = bytearray(2) # data from the sensor is saved in a buffer array
    sensor.readfrom_mem_into(address, temp_reg, data)
    time.sleep(0.01) # short delay between readings
    print(temp_c(data)) # printing temperature in celsius
    if temp_c(data) < 25: # below the threshold of 25 degrees the pixels will be green
        np[0] = (255, 0, 0)
        np[1] = (255, 0, 0)
    elif temp_c(data) > 28: # above the threshold of 28 degrees the pixels will be red
        np[0] = (0, 255, 0)
        np[1] = (0, 255, 0)
    else: # for anything in between the pixels will be yellow
        np[0] = (128, 128, 0)
        np[1] = (128, 128, 0)
    np.write() # write data to all pixels
