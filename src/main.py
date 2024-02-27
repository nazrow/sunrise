import troykahat
import time
import datetime
from gpiozero import Servo

servomin = 0.000544
servomax = 0.0024
now = (servomax + servomin) / 2
clockwise = True
servo = Servo("WPI6", min_pulse_width=servomin, max_pulse_width=servomax)

print(f'Hey bitch! It\'s {datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%s")}')
while True:
    time.sleep(0.1)
    servo.value = now
    now = now + 0.0003 if clockwise else now - 0.0003
    if now > servomax:
        clockwise = False
        now = servomax
    elif now < servomin:
        clockwise = True
        now = servomin
    print(now)
