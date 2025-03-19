from machine import Pin
from time import sleep

led = Pin(25,Pin.OUT)

n = 0

sleepT= 1 # 1sec Delay
while True:
    led.toggle()
    print("Counting from {} delay is {} sec".format(n,sleepT))
    n = n + 1
    sleep(sleepT)