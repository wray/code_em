# Put your commands here
COMMAND1 = "~~"
COMMAND2 = "what is your name?"
COMMAND3 = "what is yor favorite color?"
COMMAND4 = "Purple"
COMMAND5 = "How old are you?"
COMMAND6 = "12"
COMMAND7 = "Hello"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "Huh?"

    elif command.find(COMMAND2) >= 0:
        response= "hi?"
    elif command.find(COMMAND3) >= 0:
        response= "how old are you?"
    elif command.find(COMMAND4) >= 0:
        response= "12"
    elif command.find(COMMAND5) >= 0:
        response= "what is your favorite color? mine is blue!"
    elif command.find(COMMAND6) >= 0:
        response= "cool"
    return response

