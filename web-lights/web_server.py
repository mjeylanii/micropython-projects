import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led, LED
import machine
from light_management_htlmini import webpage
from secrets import *
import json

ssid = SSID
password = PWD


def connect():
    # Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    pico_led.on()
    print(f'Connected on {ip}')
    return ip


def open_socket(ip):
    # Open a socket
    print(f'Opening socket on {ip} port 80')
    address = (ip, 80)
    connection = socket.socket()
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind(address)
    connection.listen(1)
    return connection


def serve(connection):
    # Start a web server
    states = ["false"] * 7   # list of states of 4 LEDs
    temperature = 0
    led_pins = [9, 10, 11, 12, 13, 14, 15]  # GPIO pins for the four LEDs
    leds = [LED(pin) for pin in led_pins]
    css_path = "style.css"
    while True:
        print("connection open")
        client = None
        try:
            client = connection.accept()[0]
            request = client.recv(1024)
            request = request.decode()
            try:
                if request.startswith('POST /'):
                    # Get the LED states from the request body
                    body = request.split('\r\n\r\n')[1]
                    print(body)
                    # Get the LED states from the request body
                    led_states = body.split('&')
                    states = ["false"] * 6
                    for i, led_state in enumerate(led_states):
                        if len(led_state) == 0:
                            break
                        led_name, led_value = led_state.split('=')
                        print(led_name, led_value)
                        if led_name == 'led1':
                            states[0] = "true" if led_value == 'true' else "false"
                        elif led_name == 'led2':
                            states[1] = "true" if led_value == 'true' else "false"
                        elif led_name == 'led3':
                            states[2] = "true" if led_value == 'true' else "false"
                        elif led_name == 'led4':
                            states[3] = "true" if led_value == 'true' else "false"
                        elif led_name == 'led5':
                            states[4] = "true" if led_value == 'true' else "false"
                        elif led_name == 'led6':
                            states[5] = "true" if led_value == 'true' else "false"
                        elif led_name == 'led6':
                            states[6] = "true" if led_value == 'true' else "false"
                    # Update the LED states
                    for i, s in enumerate(states):
                        if s == "true":
                            leds[i].on()
                        else:
                            leds[i].off()
            except IndexError:
                pass
            temperature = pico_temp_sensor.temp
            print(states)
            with open('style.css') as css_file:
                css_content = css_file.read()
                css_file.close()      
            with open('javascript.js') as js_file:
                javascript = js_file.read()
                js_file.close()
            for chunk in webpage(states, temperature, css_content, javascript):
                client.sendall(chunk)
            client.close()
        except ConnectionResetError:
            print("ConnectionResetError occurred.")
            if client:
                client.close()
        except Exception as e:
            print(f"An error occurred: {e}")
            if client:
                client.close()

try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
#On connection reset open connection again
except OSError:
    print("Connection reset")
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
    

except KeyboardInterrupt:
    machine.reset()

