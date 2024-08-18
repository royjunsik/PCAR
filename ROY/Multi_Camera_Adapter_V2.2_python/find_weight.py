#!/usr/bin/env python3
import pickle
import os

import RPi.GPIO as GPIO  # import GPIO
from hx711 import HX711  # import the class HX711

def find_weight_1():
    tmp=0.0

    try:
        GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering
        # Create an object hx which represents your real hx711 chip
        # Required input parameters are only 'dout_pin' and 'pd_sck_pin'
        hx = HX711(dout_pin=21, pd_sck_pin=20)
        # Check if we have swap file. If yes that suggest that the program was not
        # terminated proprly (power failure). We load the latest state.
        swap_file_name = 'swap_file_1.swp'
        if os.path.isfile(swap_file_name):
            with open(swap_file_name, 'rb') as swap_file:
                hx = pickle.load(swap_file)
                # now we loaded the state before the Pi restarted.
                #print("Now, I will read data in infinite loop. To exit press 'CTRL + C'")
                #input('Press Enter to begin reading')
                while True:
                    weight = hx.get_weight_mean(10)
                    print(weight, 'g')
                    if(weight > 10 and abs(tmp - weight) <0.1):
                        print("Found it! : ", weight)
                        return weight
                        break
                    tmp = weight
                    
                
        else:
            print("There is no file")

        

    except (KeyboardInterrupt, SystemExit):
        print('Bye :)')

    finally:
        GPIO.cleanup()

def find_weight_2():

    tmp=0.0

    try:
        GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering
        # Create an object hx which represents your real hx711 chip
        # Required input parameters are only 'dout_pin' and 'pd_sck_pin'
        hx = HX711(dout_pin=16, pd_sck_pin=12)
        # Check if we have swap file. If yes that suggest that the program was not
        # terminated proprly (power failure). We load the latest state.
        swap_file_name = 'swap_file_2.swp'
        if os.path.isfile(swap_file_name):
            with open(swap_file_name, 'rb') as swap_file:
                hx = pickle.load(swap_file)
                # now we loaded the state before the Pi restarted.
                #print("Now, I will read data in infinite loop. To exit press 'CTRL + C'")
                #input('Press Enter to begin reading')
                while True:
                    weight = hx.get_weight_mean(10)
                    print(weight, 'g')
                    if(weight > 10 and abs(tmp - weight) <0.1):
                        print("Found it! : ", weight)
                        return weight
                        break
                    tmp = weight
                    
                
        else:
            print("There is no file")

        

    except (KeyboardInterrupt, SystemExit):
        print('Bye :)')

    finally:
        GPIO.cleanup()
