import time
import RPi.GPIO as GPIO

from servo_part import *

board, servo_pin9, servo_pin10, servo_pin11, servo_pin12 = arduino_setup()
init_servo()

rotate_servo9(90)
rotate_servo10(80)
rotate_servo11(75)
rotate_servo12(100)

#setup_servo()
#init_servo()
#left_heavy()
#right_heavy()
#left_left()
#left_right()
#right_left()
#right_right()


#rotate_servo9(90)
#rotate_servo10(90)
#rotate_servo11(90)
#rotate_servo12(90)




print('finish')
