# Put your commands here
COMMAND1 = "hi"
COMMAND2 = "what is your name?"
COMMAND3 = "what is yor favorite color?"
COMMAND4 = "purple"
COMMAND5 = "how old are you?"
COMMAND6 = "12"
COMMAND7 = "hello"
COMMAND8 = "do you like doctor who?" 
COMMAND9 = "no!"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "Huh?"

    elif command.find(COMMAND2) >= 0:
        response= "hi?"
    elif command.find(COMMAND3) >= 0:
        response= "how old are you?"
    elif command.find(COMMAND4) >= 0:
        response= "12"
    elif command.find(COMMAND5) >= 0:
        response= "what is your favorite color? mine is blue!"
    elif command.find(COMMAND6) >= 0:
        response= "cool"
    elif command.find(COMMAND7) >= 0:
       response = "do you like Doctor Who?"
    elif command.find(COMMAND8) >= 0:
       response = "no!"
    elif command.find(COMMAND9) >= 0:
       response = "bye, v!"






     return response
    
