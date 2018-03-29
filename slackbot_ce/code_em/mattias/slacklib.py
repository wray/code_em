# Put your commands here
COMMAND1 = "urgranny"
COMMAND2 = "ursister"
COMMAND3 = "urgrans"
COMMAND4 = "urbrother"
COMMAND5 = "ursistery"
# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a respnse, if necessary.
    """
    response = ""
    if COMMAND1 in command:
        response = "IF YOU SHIP MADDIE AND BOJANGLES YOU GET BODADDY" 
    if COMMAND2 in command:
        response = "IF YOU SHIP MADDIE AND BOJANGLES YOU GET BODADDY"
	if COMMAND3 in command:
		response = "IF YOU SHIP MADDIE AND BOJANGLES YOU GET BODADDY"
    if COMMAND4 in command:
        response = "IF YOU SHIP MADDIE AND BOJANGLES YOU GET BODADDY"
    if COMMAND5 in command:
        response = "IF YOU SHIP MADDIE AND BOJANGLES YOU GET BODADDY"
    return response
