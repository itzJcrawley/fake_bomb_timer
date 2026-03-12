import RPi.GPIO as GPIO
import time

PIN = 17
BUTTON = 23

GPIO.setmode(GPIO
GPIO.setup(PIN,GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
try:
    while True:
        if GPIO.input(BUTTON) == GPIO.LOW:

            i=1
            while(i>0.000002):
                  GPIO.output(PIN,GPIO.HIGH)
                  time.sleep(0.1)
                  GPIO.output(PIN,GPIO.LOW)
                  time.sleep(i)
                  i = i - 0.01
            j = 100
            while(j>1):
                  GPIO.output(PIN,GPIO.HIGH)
                  time.sleep(0.1)
                  GPIO.output(PIN,GPIO.LOW)
                  time.sleep(0.01)
                  j = j - 1
                     
        else:
            GPIO.output(PIN,GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
