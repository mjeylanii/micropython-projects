import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led, LED
import machine
from light_management_html import webpage
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
    states = ["false"] * 6   # list of states of 4 LEDs
    temperature = 0
    led_pins = [9, 10, 11, 12, 13, 14]  # GPIO pins for the four LEDs
    leds = [LED(pin) for pin in led_pins]
    while True:
        print("connection open")
        client = connection.accept()[0]
        request = client.recv(1024)
        request = request.decode()
        try:
            if request.startswith('GET /leds'):
                # Create a dictionary with the current LED states
                led_states = {
                    "led1": states[0],
                    "led2": states[1],
                    "led3": states[2],
                    "led4": states[3],
                    "led5": states[4],
                    "led6": states[5]
                }

                # Convert the dictionary to a JSON formatted string
                led_states_json = json.dumps(led_states)
                print(led_states_json)
                # Send the JSON data as the response content with the appropriate content type header
                response_headers = [("Content-type", "application/json")]
                header_strings = [f"{header[0]}: {header[1]}" for header in response_headers]
                response = "\r\n".join(["HTTP/1.1 200 OK"] + header_strings + ["", led_states_json])
                connection.sendall(response)
                
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
        html = webpage(states, temperature)
        client.send(html)
        client.close()



try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)

except KeyboardInterrupt:
    machine.reset()
