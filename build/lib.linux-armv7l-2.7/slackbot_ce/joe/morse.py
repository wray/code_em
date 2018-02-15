import RPi.GPIO as GPIO
import time

GREEN_LED = 16
RED_LED = 21
BLUE_LED = 20

GPIO.setmode(GPIO.BCM) #numbering scheme that corresponds to breakout board and pin layout
GPIO.setup(RED_LED,GPIO.OUT) #replace pinNum with whatever pin you used, this sets up that pin as an output
#set LED to flash forever

for i in range(10):
    # M
    GPIO.output(RED_LED,GPIO.HIGH)
    time.sleep(0.75)

    GPIO.output(RED_LED,GPIO.LOW)
    time.sleep(0.75)
    
    # E
    GPIO.output(RED_LED,GPIO.LOW)
    time.sleep(0.3)

    # R
    GPIO.output(RED_LED,GPIO.LOW)
    time.sleep(0.3)

    GPIO.output(RED_LED,GPIO.LOW)
    time.sleep(0.75)

    GPIO.output(RED_LED,GPIO.LOW)
    time.sleep(0.3)

    # R
    GPIO.output(RED_LED,GPIO.LOW)
    time.sleep(0.3)

    GPIO.output(RED_LED,GPIO.LOW)
    time.sleep(0.75)

    GPIO.output(RED_LED,GPIO.LOW)
    time.sleep(0.3)

    # Y
    GPIO.output(RED_LED,GPIO.LOW)
    time.sleep(0.75)

    GPIO.output(RED_LED,GPIO.LOW)
    time.sleep(0.3)

    GPIO.output(RED_LED,GPIO.LOW)
    time.sleep(0.75)

    GPIO.output(RED_LED,GPIO.LOW)
    time.sleep(0.75)
    
