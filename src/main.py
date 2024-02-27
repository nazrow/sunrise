import troykahat
import time
import datetime
# from gpiozero import Servo

servomin = 0.000544
servomax = 0.0024
step = (servomax - servomin) / 200
now = (servomax + servomin) / 2
gpio = troykahat.GpioExpander()
gpio.pinMode(0, gpio.OUTPUT)
# servo = Servo("WPI24", min_pulse_width=servomin, max_pulse_width=servomax)

print(f'Hey bitch! It\'s {datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%s")}')
while True:
    print(now)
    time.sleep(0.1)
    # servo.value = now
    gpio.analogWrite(0, now)
    now = now + step
    if now > servomax:
        step = step * (-1)
        now = servomax
    elif now < servomin:
        step = step * (-1)
        now = servomin
