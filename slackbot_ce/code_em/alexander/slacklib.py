# Put your commands here
COMMAND1 = "what is the best video "
COMMAND2 = "reply"
COMMAND3 = "best thing to kill time"
# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = "no"
    if command.find(COMMAND1) >= 0:
        response = "Castelvania"
        
          if command.find(COMMAND2) >= 0:
        response = "Answer"
        
        if command.find(COMMAND3) >= 0:
        response = "video games"
        
        
    return response

