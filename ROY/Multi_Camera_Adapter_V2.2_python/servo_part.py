import time
from pyfirmata import Arduino, util

# Specify the port to which the Arduino is connected
# Example for Linux: '/dev/ttyUSB0'
# Example for Windows: 'COM3'
# Example for macOS: '/dev/tty.usbmodem1421'
def arduino_setup():
    board = Arduino('/dev/ttyACM0')  # Change this to your actual portDefine the servo pin
    servo_pin = board.get_pin('d:9:s')
    return board, servo_pin

def rotate_servo(servo_pin, angle):
    servo_pin.write(angle)
    time.sleep(1)  # Allow some time for the servo to reach the position

# Rotate the servo to 90 degrees
#rotate_servo(0)
#rotate_servo(90)
#print("finsh")
#rotate_servo(30)
#rotate_servo(0)
# Cleanup and close the communication with Arduino
#board.exit()