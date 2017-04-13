#Toggle the display on an off depending
#upon motion detection
import os
import subprocess
import time
import RPI.GPIO as GPIO

# os.environ['DISPLAY'] = ":0"
# GPIO.setmode(GPIO.BCM)
# pir_pin = 13
# GPIO.setup(pir_pin, GPIO.IN)
# displayison = False
# maxidle = 2*60 # seconds
# lastsignaled = 0
# while True:
#     now = time.time()
#     if GPIO.input(pir_pin):
#         if not displayison:
#             subprocess.call('xset dpms force on', shell=True)
#             displayison = True
#         lastsignaled = now
#     else:
#         if now-lastsignaled > maxidle:
#             if displayison:
#                 subprocess.call('xset dpms force off', shell=True)
#                 displayison = False
#     time.sleep(1)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #LED output pin
while True:
       i=GPIO.input(11)
       if i==0:                 #When output from motion sensor is LOW
             print "No intruders",i
             GPIO.output(3, 0)  #Turn OFF LED
             time.sleep(0.1)
       elif i==1:               #When output from motion sensor is HIGH
             print "Intruder detected",i
             GPIO.output(3, 1)  #Turn ON LED
             time.sleep(3)
