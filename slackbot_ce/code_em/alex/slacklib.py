# Put your commands here
COMMAND1 = "damn daniel"
COMMAND2 = "back at it again in the wrong hood"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = "Huh?"
    if command.find(COMMAND1) >= 0:
        response = "Huh?"

    elif command.find(COMMAND2) >= 0:
        response = "I'm not sure I follow."
        
    return response

