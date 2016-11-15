# Put your commands here
COMMAND1 = "what is the best video "
COMMAND2 = ""
# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = "no"
    if command.find(COMMAND1) >= 0:
        response = "Castelvania"
        
    return response

