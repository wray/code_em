import random
import json
import urllib3
import shelve

import temp_humidity
#import led

COMMAND1 = "who are you"
COMMAND2 = "what can you do"
COMMAND3 = "temp"
COMMAND4 = "name an animal"
COMMAND5 = "new command"
COMMAND6 = "del command"

def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "I am a simpleton bot."
    elif command.find(COMMAND2) >= 0:
        response = "Not much right now... waiting for students to teach me."
    elif command.find(COMMAND3) >= 0:
        try:
            temp_c,temp,humidity = temp_humidity.read_temp_humidity()
            response = "At my location, the temperature is " + str(temp) + " and the relative humidity is " + str(humidity)
        except:
            response = "At my location, there is a sensor malfunction."

    elif command.find(COMMAND4) >= 0:
        http = urllib3.PoolManager()
        animals = json.loads(http.request('GET','https://www.randomlists.com/data/animals.json').data.decode('utf-8'))['data']
        response = animals[random.randint(0,len(animals)-1)]

    elif command.find(COMMAND5) >= 0:
        commands = shelve.open('commands')
        parse = command.split(',')
        pc = parse[0].find(':')
        parse_command = parse[0][pc+1:].strip()
        commands[parse_command] = parse[1].strip()
        commands.sync()
        print commands
        commands.close()
        response = "ok"

    elif command.find(COMMAND6) >= 0:
        commands = shelve.open('commands')
        pc = command.find(':')
        try:
            commands.pop(command[pc+1:].strip())
        except:
            pass
        commands.sync()
        commands.close()
        response = "ok"
    else:
        commands = shelve.open('commands')
        if commands.has_key(command.strip()):
            response = commands[command.strip()]
        commands.close()
        
    return response

