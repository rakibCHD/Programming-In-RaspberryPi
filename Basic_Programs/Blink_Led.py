from machine import Pin
from time import sleep

led = Pin(25,Pin.OUT)

n = 0

while True:
    led.toggle()
    print("Counting from {} delay is 0.5sec".format(n))
    n = n + 1
    sleep(0.5)