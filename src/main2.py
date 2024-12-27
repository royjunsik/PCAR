import threading
import time
import pygame
import RPi.GPIO as GPIO

from find_weight import *
from capture_image import *
from sound_control import *
from test_img import *
from servo_part import *

camera_lock = threading.Lock()
servo_lock  = threading.Lock()

board, servo_pin9, servo_pin10, servo_pin11, servo_pin12 = arduino_setup()
init_servo()

print("start")

# degree 0 is default(closed), and degree 90 is opened

def thread_1():
    try: 
        while True:
            weight1 = find_weight_1()
            if(weight1 > 50):
                servo_lock.acquire()
                play_mp3('water.mp3')
                left_heavy()
                servo_lock.release()
                
            else:
                camera_lock.acquire()
                camera_A()
                camera_lock.release()
                result1 = resnet18_test(1)
                if(result1 == 0):
                    servo_lock.acquire()
                    play_mp3('PET.mp3')
                    left_left()
                    servo_lock.release()
                
                elif(result1 == 1):
                    servo_lock.acquire()
                    play_mp3('label.mp3')
                    left_heavy()
                    servo_lock.release()
                    
                elif(result1 == 2):
                    servo_lock.acquire()
                    play_mp3('normal.mp3')
                    left_right()
                    servo_lock.release()
                    
                
    except KeyboardInterrupt:
        print("\nProgram interrupted! Cleaning up GPIO and exiting...")
        
def thread_2():
    try: 
        while True:
            weight2 = find_weight_2()
            
            if(weight2 > 50):
                servo_lock.acquire()
                play_mp3('water.mp3')
                right_heavy()
                servo_lock.release()
            
            else:
                camera_lock.acquire()
                camera_B()
                camera_lock.release()
                
                result2 = resnet18_test(2)
                
                if(result2 == 0):
                    servo_lock.acquire()
                    play_mp3('PET.mp3')
                    right_left()
                    servo_lock.release()
                
                elif(result2 == 1):
                    servo_lock.acquire()
                    play_mp3('label.mp3')
                    right_heavy()
                    servo_lock.release()
                    
                elif(result2 == 2):
                    servo_lock.acquire()
                    play_mp3('normal.mp3')
                    right_right()
                    servo_lock.release()

                
    except KeyboardInterrupt:
        print("\nProgram interrupted! Cleaning up GPIO and exiting...")
        

if __name__ == "__main__":
    try:
        for i in range(1):
            # Create two threads
            thread1 = threading.Thread(target=thread_1)
            thread2 = threading.Thread(target=thread_2)
            
            thread1.start()
            thread2.start()
            
            thread1.join()
            thread2.join()
            
    except KeyboardInterrupt:
        print("\nProgram interrupted! Cleaning up GPIO and exiting...")
        # Additional cleanup can be done here if necessary
    finally:
        GPIO.cleanup()
            
