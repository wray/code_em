import random
import json
import urllib3
import time

import temp_humidity
import led

COMMAND1 = "who are you"
COMMAND2 = "what can you do"
COMMAND3 = "temp"
COMMAND4 = "name an animal"
COMMAND5 = "get-ip"

def mission_control(bot_id,output):
    for word in output['text'].split(" "):
        print(word)
        if word.lower() == 'arm-1123':
            led.green_led(1)
        elif word.lower() == 'disarm':
            led.green_led(0)
        elif word.lower() == 'launch-sequence-1123':
            led.green_led(0)
            for i in range(5):
                led.red_led(1)
                time.sleep(1)
                led.red_led(0)
            time.sleep(1)
            led.green_led(1) #led.launch_led(1)
            time.sleep(1)
            led.green_led(0)
            

def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "I am a simpleton bot."
    elif command.find(COMMAND2) >= 0:
        response = "Not too much right now... waiting for students to teach me more."
    elif command.find(COMMAND3) >= 0:
        try:
            import socket
            s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            s.connect(("8.8.8.8",80))
            ip = s.getsockname()[0]

            temp_c,temp,humidity = temp_humidity.read_temp_humidity()
            response = "At my location (" + ip + ") , the temperature is " + str(temp) + " and the relative humidity is " + str(humidity)
        except:
            response = "At my location, there is a sensor malfunction."

    elif command.find(COMMAND4) >= 0:
        try:
            http = urllib3.PoolManager()
            animals = json.loads(http.request('GET','https://www.randomlists.com/data/animals.json').data.decode('utf-8'))['data']
            response = animals[random.randint(0,len(animals)-1)]
        except:
            response = "Cannot find animals."

    elif command.find(COMMAND5) >= 0:
        import socket
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(("8.8.8.8",80))
        response = s.getsockname()[0]

            
        
    return response

