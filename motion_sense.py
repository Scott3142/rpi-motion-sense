from gpiozero import MotionSensor
from time import sleep
from picamera import PiCamera
from datetime import datetime

motion=MotionSensor(12)
camera = PiCamera()
camera.rotation = 180

while True:
    motion.wait_for_motion()
    dt_string = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
    filename = "/home/pi/pir/pic" + dt_string + ".jpg"
    camera.capture(filename)
    sleep(2)
