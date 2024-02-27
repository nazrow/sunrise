from time import sleep
from gpiozero import Servo
import random

servo = Servo("WPI24")
while True:
    servo.value = random.uniform(-1, 1)
    sleep(random.uniform(0.01, 0.5))
