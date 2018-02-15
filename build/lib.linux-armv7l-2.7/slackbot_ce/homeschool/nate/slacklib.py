# Put your commands here
COMMAND1 = "throw mud at me"
COMMAND2 = "pick it up and throw"
COMMAND3 = "then do water"
COMMAND4 = "try sharks then"
COMMAND5 = "pikachu"
#COMMAND6
#COMMAND7

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "okay how"
    elif command.find(COMMAND2) >=0:
        response = "what does that mean"
    elif command.find(COMMAND3) >=0:       
        response = "water? WHAT IS THAT!?!?!"
    elif command.find(COMMAND4) >=0:       
        response = "WHAT IS MUD WATER AND SHARKS!?!?!?!?!?"
    elif command.find(COMMAND5) >=0:       
        response = "Oh its a pikachu? Wait WHAT IS A PIKACHU!?!?!?!?"

    return response
    
    
