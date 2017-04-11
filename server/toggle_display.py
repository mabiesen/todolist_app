#Toggle the display on an off depending
#upon motion detection
import os
import subprocess
import time
import RPI.GPIO as GPIO

os.environ['DISPLAY'] = ":0"
GPIO.setmode(GPIO.BCM)
pir_pin = 13
GPIO.setup(pir_pin, GPIO.IN)
displayison = False
maxidle = 2*60 # seconds
lastsignaled = 0
while True:
    now = time.time()
    if GPIO.input(pir_pin):
        if not displayison:
            subprocess.call('xset dpms force on', shell=True)
            displayison = True
        lastsignaled = now
    else:
        if now-lastsignaled > maxidle:
            if displayison:
                subprocess.call('xset dpms force off', shell=True)
                displayison = False
    time.sleep(1)
