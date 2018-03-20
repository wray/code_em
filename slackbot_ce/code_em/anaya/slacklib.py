# Put your commands here
COMMAND1 = "Salutations"
COMMAND2 = "Is it going to snow tomorrow?"
COMMAND3 = "Which school do you go to?"
COMMAND4 = "Do you like pastries?"
COMMAND5 = "What are you allergic to?"


# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if COMMAND1 in command:
        response = "Salutations to you to."
Sal
    response = ""
    if COMMAND2 in command:
        response = "I am not sure."

    response = ""
    if COMMAND3 in command:
        response = "I go to Echo Lake Elementary School."
 
     response = ""
    if COMMAND4 in command:
        response = "I love pastries!"

    response = ""
    if COMMAND5 in command:
        response = "I am allergic to grass and mulch.sss"   
    return response
