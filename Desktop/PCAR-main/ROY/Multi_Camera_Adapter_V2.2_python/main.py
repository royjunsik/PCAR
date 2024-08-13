import RPi.GPIO as GPIO
import time
import os
from pyfirmata import Arduino, util
from find_weight import *
from sound_control import *
from servo_part import *
import test_img
from AdapterTestDemo import *


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.output(4, False)
GPIO.output(17, False)
GPIO.output(18, True)

board, servo_pin = arduino_setup()

#rotate_servo(servo_pin,0)
while True :
    test=find_weight()
    print("weight : ", test)
    if(test >100) :
        rotate_servo(servo_pin,90)
        play_mp3('/home/tony8181/Downloads/Please_empty_the_liquid.mp3')
    else:
        capture()
      
        abc = test_img.test_PET()
        if(abc == 0) :
                play_mp3('/home/tony8181/Downloads/This_is_PET.mp3')
        elif(abc == 1) :
                play_mp3('/home/tony8181/Downloads/Please_remove_the_label.mp3')
        else :
                play_mp3('/home/tony8181/Downloads/This_is_Plastic.mp3')
        rotate_servo(servo_pin,180)

