# Put your commands here
COMMAND1 = "what is 4+4?"
COMMAND2 = "does a fish live in water?"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if COMMAND1 in command:
        response = "8"
    
    elif COMMAND2 in command:
		response = "Yes."
	
        
    return response

