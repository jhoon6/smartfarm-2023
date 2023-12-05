import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(19, GPIO.OUT) #4ch-relay-first
GPIO.setup(16, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

li = [19,16,26,20]

for i in li:
        GPIO.output(i, GPIO.HIGH)

while(True):
    for i in li:
        for o in li:
            GPIO.output(o, GPIO.HIGH)
        GPIO.output(i, GPIO.LOW)
        input(i)