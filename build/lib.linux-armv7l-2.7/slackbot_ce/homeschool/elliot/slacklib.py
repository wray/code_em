# Put your commands here
COMMAND1 = "what do i look like?"
COMMAND2 = "bluedibal"
COMMAND3 = "what is a computer"
COMMAND4 = "i don't like harry potter"
# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "does it look like i have eyes too you."
        
    elif command.find(COMMAND2) >= 0:
        response = "eniglesh plz."
        
    elif command.find(COMMAND3) >= 0:
        response = "you are using one."
    
    elif command.find(COMMAND4) >= 0:
        response = "you are wasting your life."

    return response

