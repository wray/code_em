# Put your commands here
COMMAND1 = "what color is the sky?"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "It depends on who you are asking. I would say it is purple."
        
    return response

