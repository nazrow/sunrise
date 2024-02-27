from time import sleep
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
import random

pigpio = PiGPIOFactory()
servo = Servo("WPI24", pin_factory=pigpio)
while True:
    servo.value = random.uniform(-1, 1)
    sleep(random.uniform(0.01, 0.5))
