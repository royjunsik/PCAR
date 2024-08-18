#!/usr/bin/env python3
import pickle
import os

import RPi.GPIO as GPIO  # import GPIO
from hx711 import HX711  # import the class HX711

try:
    GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering
    
    # Create HX711 objects for two load cells
    hx1 = HX711(dout_pin=21, pd_sck_pin=20)
    hx2 = HX711(dout_pin=16, pd_sck_pin=12)

    # Check if we have swap files for each HX711. If yes, that suggests that the program was not
    # terminated properly (power failure). We load the latest state.
    swap_file_name_1 = 'swap_file_1.swp'
    swap_file_name_2 = 'swap_file_2.swp'

    # Measure tare and save the value as offset for current channel
    # and gain selected. That means channel A and gain 128
    err1 = hx1.zero()
    err2 = hx2.zero()

    # Check if successful
    if err1:
        raise ValueError('Tare for HX711 #1 is unsuccessful.')
    if err2:
        raise ValueError('Tare for HX711 #2 is unsuccessful.')

    # Calibration for Load Cell 1
    reading1 = hx1.get_raw_data_mean()
    if reading1:
        print('HX711 #1: Data subtracted by offset but still not converted to units:', reading1)
    else:
        print('HX711 #1: Invalid data', reading1)

    input('Put known weight on Load Cell 1 and then press Enter')
    reading1 = hx1.get_data_mean()
    if reading1:
        print('HX711 #1: Mean value from HX711 subtracted by offset:', reading1)
        known_weight_grams_1 = input('Write how many grams it was and press Enter: ')
        try:
            value1 = float(known_weight_grams_1)
            print(value1, 'grams')
        except ValueError:
            print('Expected integer or float and I have got:', known_weight_grams_1)

        ratio1 = reading1 / value1  # Calculate the ratio for channel A and gain 128
        hx1.set_scale_ratio(ratio1)  # Set ratio for current channel
        print('HX711 #1: Ratio is set.')
    else:
        raise ValueError('Cannot calculate mean value for HX711 #1. Try debug mode. Variable reading:', reading1)

    # Calibration for Load Cell 2
    reading2 = hx2.get_raw_data_mean()
    if reading2:
        print('HX711 #2: Data subtracted by offset but still not converted to units:', reading2)
    else:
        print('HX711 #2: Invalid data', reading2)

    input('Put known weight on Load Cell 2 and then press Enter')
    reading2 = hx2.get_data_mean()
    if reading2:
        print('HX711 #2: Mean value from HX711 subtracted by offset:', reading2)
        known_weight_grams_2 = input('Write how many grams it was and press Enter: ')
        try:
            value2 = float(known_weight_grams_2)
            print(value2, 'grams')
        except ValueError:
            print('Expected integer or float and I have got:', known_weight_grams_2)

        ratio2 = reading2 / value2  # Calculate the ratio for channel A and gain 128
        hx2.set_scale_ratio(ratio2)  # Set ratio for current channel
        print('HX711 #2: Ratio is set.')
    else:
        raise ValueError('Cannot calculate mean value for HX711 #2. Try debug mode. Variable reading:', reading2)

    # Save the HX711 states to swap files on persistent memory
    print('Saving the HX711 #1 state to swap file on persistent memory')
    with open(swap_file_name_1, 'wb') as swap_file:
        pickle.dump(hx1, swap_file)
        swap_file.flush()
        os.fsync(swap_file.fileno())

    print('Saving the HX711 #2 state to swap file on persistent memory')
    with open(swap_file_name_2, 'wb') as swap_file:
        pickle.dump(hx2, swap_file)
        swap_file.flush()
        os.fsync(swap_file.fileno())

    # Read data several times and return mean value
    # subtracted by offset and converted by scale ratio to
    # desired units. In this case, grams.
    print("Now, I will read data from both load cells in an infinite loop. To exit, press 'CTRL + C'")
    input('Press Enter to begin reading')
    while True:
        print(f'Load Cell 1: {hx1.get_weight_mean(20)} g, Load Cell 2: {hx2.get_weight_mean(20)} g')

except (KeyboardInterrupt, SystemExit):
    print('Bye :)')

finally:
    GPIO.cleanup()
