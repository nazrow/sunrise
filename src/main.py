from time import sleep
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory

pigpio = PiGPIOFactory()
servo = Servo("WPI24", pin_factory=pigpio)
servo.value = 1
sleep(10)
servo.value = -1
sleep(10)
servo.close()