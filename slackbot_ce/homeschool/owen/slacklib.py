# Put your commands here
COMMAND1 = "make me a sandvich."
COMMAND2 = "ok"
# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "i don't have hands make the sandvich yourself."
    elif command.find(COMMAND2) >= 0:
        respomse = "ok for what?"
        
    return response
