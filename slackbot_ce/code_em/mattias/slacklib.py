# Put your commands here
COMMAND1 = "URGRANNY"
COMMAND2 = "URSISITER"
COMMAND3 = "URGRANS"
COMMAND4 = "URBROTHER"
COMMAND5 = "URSISTER"
# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a respnse, if necessary.
    """
    response = ""
    if COMMAND1 in command:
        response = "UR FAMILY TREE A FAT MONKEY" 
    if COMMAND2 in command:
        response = " UR BROTHER A MOTHER "
	if COMMAND3 in command:
		response = "UR SISTER A MISTER"
    if COMMAND4 in command:
        response = "UR DAUGHTER A FATHER"
    if COMMAND5 in command:
        response = "IF YOU SHIP MADDIE AND BOJANGLES YOU GE BODADDY"
    return response
