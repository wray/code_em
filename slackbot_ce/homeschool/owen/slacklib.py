# Put your commands here
COMMAND1 = "make me a sandvich."
COMMAND2 = "ok"
COMMAND3 = "what food do you like to eat"
COMMAND4 = "how old are you?"
COMMAND5 = "do you like apples?"
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
        response = "ok for what?"
    elif command.find(COMMAND3) >= 0:
        response = "i can't eat stupid"
    elif command.find(COMMAND4) >= 0:
        response = "i have no age mortal!"
    elif command.find(COMMAND5) >= 0:
        response = "I cannot eat!"


    return response