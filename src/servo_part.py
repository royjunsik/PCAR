import time
from pyfirmata import Arduino, util

setting_time = 0.3
waiting_time = 1
large_angle = 150
small_angle = 30
down_left = 75
down_right = 100

#global servo_pin9, servo_pin10, servo_pin11, servo_pin12

# Specify the port to which the Arduino is connected
# Example for Linux: '/dev/ttyUSB0'
# Example for Windows: 'COM3'
# Example for macOS: '/dev/tty.usbmodem1421'
def arduino_setup():
    board = Arduino('/dev/ttyACM0')  # Change this to your actual portDefine the servo pin
    global servo_pin9, servo_pin10, servo_pin11, servo_pin12
    servo_pin9 = board.get_pin('d:9:s')
    servo_pin10 = board.get_pin('d:10:s')
    servo_pin11 = board.get_pin('d:11:s')
    servo_pin12 = board.get_pin('d:12:s')
    return board, servo_pin9, servo_pin10, servo_pin11, servo_pin12

def rotate_servo9(angle):
    servo_pin9.write(angle)
    #time.sleep(0.5)  # Allow some time for the servo to reach the position
    
def rotate_servo10(angle):
    servo_pin10.write(angle)
    
def rotate_servo11(angle):
    servo_pin11.write(angle)

def rotate_servo12(angle):
    servo_pin12.write(angle)
    
def setup_servo():
    rotate_servo9(90)
    rotate_servo10(90)
    rotate_servo11(90)
    rotate_servo12(90)
    
def init_servo():
    rotate_servo9(90)
    rotate_servo10(80)
    rotate_servo11(down_left)
    rotate_servo12(down_right)
    time.sleep(setting_time)
    
def left_heavy():
    rotate_servo9(small_angle)
    rotate_servo10(80)
    rotate_servo11(down_left)
    rotate_servo12(down_right)
    
    time.sleep(waiting_time)
    init_servo()

def right_heavy():
    rotate_servo9(90)
    rotate_servo10(large_angle)
    rotate_servo11(down_left)
    rotate_servo12(down_right)
    
    time.sleep(waiting_time)
    init_servo()
    
def right_right():
    
    rotate_servo9(90)
    rotate_servo10(80)
    rotate_servo11(down_left)
    rotate_servo12(small_angle)
    
    time.sleep(setting_time)
    
    rotate_servo9(90)
    rotate_servo10(large_angle)
    rotate_servo11(down_left)
    rotate_servo12(small_angle)
    
    time.sleep(waiting_time)
    init_servo()
    
def right_left():
    
    rotate_servo9(90)
    rotate_servo10(80)
    rotate_servo11(large_angle)
    rotate_servo12(down_right)
    
    time.sleep(setting_time)
    
    rotate_servo9(90)
    rotate_servo10(large_angle)
    rotate_servo11(large_angle)
    rotate_servo12(down_right)
    
    time.sleep(waiting_time)
    init_servo()

def left_left():
    
    rotate_servo9(90)
    rotate_servo10(80)
    rotate_servo11(large_angle)
    rotate_servo12(down_right)
    
    time.sleep(setting_time)
    
    rotate_servo9(small_angle)
    rotate_servo10(80)
    rotate_servo11(large_angle)
    rotate_servo12(down_right)
    
    time.sleep(waiting_time)
    init_servo()

def left_right():
    
    rotate_servo9(90)
    rotate_servo10(80)
    rotate_servo11(down_left)
    rotate_servo12(small_angle)
    
    time.sleep(setting_time)
    
    rotate_servo9(small_angle)
    rotate_servo10(80)
    rotate_servo11(down_left)
    rotate_servo12(small_angle)
    
    time.sleep(waiting_time)
    init_servo()

# Rotate the servo to 90 degrees
#rotate_servo(0)
#rotate_servo(90)
#print("finsh")
#rotate_servo(30)
#rotate_servo(0)
# Cleanup and close the communication with Arduino
#board.exit()
