from picozero import LED
from time import sleep

# define the LED pins
led_pins = [9, 10, 11, 12, 13, 14, 15]
led_list = [LED(pin) for pin in led_pins]

# define the musical notes (frequency in Hz)
E4 = 329.63
D_sharp4 = 311.13
B3 = 246.94
D4 = 293.66
C4 = 261.63
A3 = 220.00

# define the musical sequence
sequence = [E4, D_sharp4, E4, D_sharp4, E4, B3, D4, C4, A3, A3, C4, E4, D4, C4, B3]

# loop infinitely through the list of leds
def playMusic():
    while True:
        for i, led in enumerate(led_list):
            # blink the LED
            led.blink(0.2, 0.2)

            # play the corresponding musical note
            frequency = sequence[i % len(sequence)]
            sleep(0.2)
            led.off()
            sleep(0.2)
            led.blink(1/frequency, 1/frequency)
try:
    playMusic()
    
except KeyboardInterrupt:
    machine.reset()

