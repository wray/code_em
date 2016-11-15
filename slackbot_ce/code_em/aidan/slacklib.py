# Put your commands here
COMMAND1 = "hey aidan"
COMMAND2 = "how are you?"
COMMAND3="yes?"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "yes?"
    elif command.find(COMMAND2) >=0:
        response = "what aidan? "
    elif command.find(COMMAND3)>= 0:
        response = "hi"




        return response


