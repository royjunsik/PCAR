<<<<<<< HEAD
import RPi.GPIO as GPIO
import os

def capture():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    
    #print('Start testing the camera A')
    i2c = "i2cset -y 1 0x70 0x00 0x04"
    os.system(i2c)
    GPIO.output(4, False)
    GPIO.output(17, False)
    GPIO.output(18, True)

    cmd = "libcamera-still -o capture_%d.jpg" % 1
    os.system(cmd)
    
=======
import RPi.GPIO as gp
import os
import test_img

gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(12, gp.OUT)


def main():
    print('Start testing the camera A')
    i2c = "i2cset -y 1 0x70 0x00 0x04"
    os.system(i2c)
    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)
    capture(1)
>>>>>>> 702581a2eed17f338afcede98f5c286de0021a01
    """
    print('Start testing the camera B') 
    i2c = "i2cset -y 1 0x70 0x00 0x05"
    os.system(i2c)
    gp.output(7, True)
    gp.output(11, False)
    gp.output(12, True)
    capture(2)
    """
<<<<<<< HEAD
    

=======

    
def capture(cam):
    cmd = "libcamera-still -n -o capture_%d.jpg" % cam
    os.system(cmd)

if __name__ == "__main__":
    main()

    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)
    
    test_img.test_PET()
>>>>>>> 702581a2eed17f338afcede98f5c286de0021a01
