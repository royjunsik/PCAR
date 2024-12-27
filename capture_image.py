import RPi.GPIO as GPIO
import os
import time
import threading
import time
from PIL import Image

GPIO.setwarnings(False)

def camera_A():
    try:   
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.OUT)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        
        print('Start testing the camera A')
        i2c = "i2cset -y 1 0x70 0x00 0x04"
        os.system(i2c)

        GPIO.output(4, False)
        GPIO.output(17, False)
        GPIO.output(18, True)
 
        capture(1)

    except KeyboardInterrupt:
        print("\nProgram interrupted! Cleaning up GPIO and exiting...")

def camera_B():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.OUT)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)

        print('Start testing the camera B')
        i2c = "i2cset -y 1 0x70 0x00 0x05"
        os.system(i2c)
        
        GPIO.output(4, True)
        GPIO.output(17, False)
        GPIO.output(18, True)
        capture(2)

    except KeyboardInterrupt:
        print("\nProgram interrupted! Cleaning up GPIO and exiting...")
        

def capture(cam):
    cmd = "libcamera-still -t 0 --immediate --width 256 --height 256 --nopreview -o capture_%d.jpg" % cam
    os.system(cmd)

    image_path = "capture_%d.jpg" % cam
    image = Image.open(image_path)

    width, height = image.size
    if width != 256 or height != 256:
        raise ValueError("Image size is not 256x256")

    pixels = image.load()

    brown = (129, 123, 101)
    for y in range(100):
        for x in range(256):
            pixels[x, y] = brown

    modified_image_path = "capture_%d.jpg" % cam
    image.save(modified_image_path)

    


if __name__ == "__main__":
    try:
        for _ in range(1):
            # Create two threads
            thread1 = threading.Thread(target=camera_A)
            thread2 = threading.Thread(target=camera_B)

            # Start the threads
            thread1.start()
            thread2.start()

            # Wait for both threads to complete
            thread1.join()
            thread2.join()

    except KeyboardInterrupt:
        print("\nProgram interrupted! Cleaning up GPIO and exiting...")
        GPIO.cleanup()
        # Additional cleanup can be done here if necessary

    finally:
        GPIO.cleanup()

