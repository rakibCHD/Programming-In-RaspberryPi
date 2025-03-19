from machine import Pin

led = Pin(25, Pin.OUT)   # Built-in LED on Pico
switch = Pin(21, Pin.IN, Pin.PULL_DOWN)  # Switch input on GPIO 21 with pull-down
gpio_20 = Pin(20, Pin.OUT)  # GPIO 20 set HIGH

gpio_20.on()  # Ensure GPIO 20 is HIGH

while True:
    if switch.value():  # If switch (GPIO 21) is HIGH
        led.on()
    else:
        led.off()
