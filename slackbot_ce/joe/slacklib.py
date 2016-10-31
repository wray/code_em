

# Put your commands here
COMMAND1 = "are you awake?"
COMMAND2 = "what is your full name?"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "Just barely..."
    elif command.find(COMMAND2) >= 0:
        response = "Sirexa Bart"
        
    return response

