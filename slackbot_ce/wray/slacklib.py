import random
import json
import urllib3

COMMAND1 = "who are you"
COMMAND2 = "what can you do"
COMMAND3 = "temp"
COMMAND4 = "name an animal"

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
        response = "Building up skills to sense temperature and humidity now. Stay tuned."
    elif command.find(COMMAND4) >= 0:
        http = urllib3.PoolManager()
        animals = json.loads(http.request('GET','https://www.randomlists.com/data/animals.json').data.decode('utf-8'))['data']
        response = animals[random.randint(0,len(animals)-1)]
        
    return response

