# Task 5
import machine, neopixel
import time
from machine import ADC
import math
np = neopixel.NeoPixel(machine.Pin(21), 2)  # create NeoPixel driver on GPIO21 for 2 pixels
adc = ADC(machine.Pin(39))  # create ADC object on ADC pin
adc.atten(ADC.ATTN_11DB)  # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
adc.width(ADC.WIDTH_9BIT)  # set 9 bit return values (returned range 0-511)
while True:
    adc_data = adc.read()  # read value using the newly configured attenuation and width
    time.sleep(0.01)
    print("brightness: {}".format(math.floor(adc_data/2)))
    # adc_data 0-511 across voltage range 0.0v-3.6v, which corresponds to brightness 0-255
    # mapping adc_data to brightness ex. adc_data 511 -> brightness 255(eq. floor(adc_data/2))
    np[0] = (0, 0, math.floor(adc_data/2))  # set the first pixel to blue
    np[1] = (0, 0, math.floor(adc_data/2))  # set the second pixel to blue
    np.write()  # write data to all pixels



