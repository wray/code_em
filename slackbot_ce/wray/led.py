
GREEN_LED = 27
RED_LED = 17
LAUNCH_LED = BLUE_LED = 11

try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GREEN_LED, GPIO.OUT)
    GPIO.setup(RED_LED, GPIO.OUT)
    GPIO.setup(BLUE_LED, GPIO.OUT)
except ImportError:
    pass

DEBUG = 1

def green_led(state):
    GPIO.output(GREEN_LED,state)

def red_led(state):
    GPIO.output(RED_LED,state)
        
def blue_led(state):
    GPIO.output(BLUE_LED,state)

def launch_led(state):
    blue_led(state)

def launch_led(state):
    blue_led(state)

def all_leds(state):
    green_led(state)
    red_led(state)
    blue_led(state)
