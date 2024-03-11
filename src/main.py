from time import sleep
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--speed')
parser.add_argument('-t', '--time')
parser.add_argument('-p', '--prespeed')
parser.add_argument('-e', '--easein')
args = parser.parse_args()
speed = float(args.speed)
time = float(args.time) / 1000
try:
    prespeed = float(args.prespeed)
    pretime = float(args.easein) / 1000
except:
    prespeed = 0
    pretime = 0.01

pigpio = PiGPIOFactory()

servo = Servo("WPI24", pin_factory=pigpio)
servo.value = prespeed
sleep(pretime)
servo.value = speed
sleep(time)
servo.close()

# полный вниз: 15 с @ -1
# полный вверх: 23 с @ 1
# минимальная скорость страгивания: около 0.12
# минимальная скорость страгивания без мучений: около 0.2