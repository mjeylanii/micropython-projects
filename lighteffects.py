from picozero import LED
from time import sleep
import machine

# define the LED pins
led_pins = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

led_list = [LED(pin) for pin in led_pins]

# loop through the LEDs quickly
def loop():
    for i in range(5):
        for led in led_list:
            led.off()
            sleep(1)
            led.on()

    # turn all the LEDs on
    
#======================================
#Left right effect
def left_right():
    # turn off all the LEDs
    for led in led_list:
        led.off()

    # loop from left to right
    for i in range(len(led_list)):
        led_list[i].on()
        sleep(0.1)

    # loop from right to left
    for i in range(len(led_list) - 1, -1, -1):
        led_list[i].on()
        sleep(0.1)

    # turn all the LEDs off
    for led in led_list:
        led.on()

def send_files_light():
    # turn off all the LEDs
    for led in led_list:
        led.off()

    # loop through the LEDs with a sending pattern
    for i in range(0, len(led_list), 2):
        led_list[i].on()
        sleep(0.2)
        led_list[i+1].on()
        sleep(0.2)

    # turn all the LEDs off
    for led in led_list:
        led.off()


