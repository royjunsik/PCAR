import RPi.GPIO as GPIO
from hx711 import HX711

GPIO.setmode(GPIO.BCM)

hx = HX711(dout_pin=6, pd_sck_pin=5)

hx.zero()

input('Place known weight on scale & press Enter : ')
reading = hx.get_data_mean(readings=100)

known_weight_grams = input('Enter the known weight in grams & press Enter : ')
value = float(known_weight_grams)

ratio = reading/value
hx.set_scale_ratio(ratio)

while True:
    weight = hx.get_weight_mean()
    print(weight)
