# Put your commands here
COMMAND1 = "what do i look like?"
<<<<<<< Updated upstream
COMMAND2 = ""
=======
COMMAND2 = "bluedibal"
>>>>>>> Stashed changes

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
          response = ""
        
    elif command.find(COMMAND2) >= 0:
        response = "eniglesh plz"
        
    return response

