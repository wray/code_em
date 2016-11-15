# Put your commands here
COMMAND1 = "whats your name?"
COMMAND2 = "What is mary poppins??"
COMMAND3 = "what is pie?"
COMMAND4 = "why are you a pie?"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "Im Piebot!"
        
    elif command.find(COMMAND2) >= 0:
        response = "Shes supercalifragulisticexpialidocious"
    elif command.find(COMMAND3) >= 0:
        resonse = "How could you not know this? Have you been living under a rock? Pie is a delicious pastry, of course!"


    elif command.find(COMMAND4) >= 0:
        response = "Because pie is awesome, and Im awesome, so I must be a pie!"
     return response
