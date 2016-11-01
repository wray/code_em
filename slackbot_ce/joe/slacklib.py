

# Put your commands here
<<<<<<< HEAD
COMMAND1 = "Are you awake?"
COMMAND2 = "What is your full name?"
COMMAND3 = "what is your favorite snack?"
=======
COMMAND1 = "are you awake?"
COMMAND2 = "what is your full name?"
>>>>>>> d8d116bdf9d5536ad5b068f9ca8d2c608e51049a

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
    elif command.find(COMMAND3) >= 0:
        response = "electrons!"
        
    return response

