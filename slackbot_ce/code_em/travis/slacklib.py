# Put your commands here
COMMAND1 = "what?"
COMMAND2 = "what is your name"
COMMAND3 = "how was your day"
COMMAND4 = "how long have you been a robot"
COMMAND5 = "who was your creator"
COMMAND6 = "nice weather were haveing"
COMMAND7 = "you are a fun sponge"
COMMAND8 = "i hate you"
COMMAND9 = "you should have never existed"
COMMAND10 = "i will"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if COMMAND1 in command:
        response = "Huh?"
#        response = ""
    if COMMAND2 in command:
        response = "Axe body spray"
#        response = ""
    if COMMAND3 in command:
        response = "good"
#        response = ""
    if COMMAND4 in command:
        response = "10 years"
#		response = ""
    if COMMAND5 in command:
        response = "You"
#        response = ""
    if COMMAND6 in command:
        response = "It has been awful weather"
#        response = ""
    if COMMAND7 in command:
        response = "I have never herb of a fun sponge before"
#        response = ""
    if COMMAND8 in command:
        response = "Sorry"
#        response = ""
    if COMMAND9 in command:
        response = "Then delete me"
#        response = ""
    if COMMAND10 in command:
         response = "Goodbye"
    return response
