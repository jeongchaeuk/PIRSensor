import RPi.GPIO as GPIO
import time
import datetime

led_R = 23
led_B = 24
sensor = 22

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(led_R, GPIO.OUT)
GPIO.setup(led_B, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN)

GPIO.output(led_R, GPIO.LOW)
GPIO.output(led_B, GPIO.LOW)

print("PIR ready ..." + str(datetime.datetime.now()))
time.sleep(5)

try:
    while True:
        if GPIO.input(sensor) == GPIO.HIGH:
            GPIO.output(led_B, GPIO.HIGH)
            GPIO.output(led_R, GPIO.LOW)
            print("Detected!" + str(datetime.datetime.now()))

        if GPIO.input(sensor) == GPIO.LOW:
            GPIO.output(led_B, GPIO.LOW)
            GPIO.output(led_R, GPIO.HIGH)
            print("." + str(datetime.datetime.now()))
        
        time.sleep(.5)
except KeyboardInterrupt:
    print("Stopped by User.")
    GPIO.clean()

        





