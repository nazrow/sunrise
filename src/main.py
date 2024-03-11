from time import sleep
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--speed')
parser.add_argument('-t', '--time')
args = parser.parse_args()
speed = float(args.speed)
time = float(args.time) / 1000
pigpio = PiGPIOFactory()
servo = Servo("WPI24", pin_factory=pigpio)
servo.value = speed
sleep(time)
servo.close()