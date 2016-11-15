# Put your commands here
COMMAND1 = "Hi"
COMMAND2 = "ERROR..."

#Your handling code toes in this function
def handle_command(comand):	
	response = ""
	if command.find(COMMAND1) >= 0:
		response="Donald J. Trump"
	elif command.find(COMMAND2) >= 0:
		response="Donald will WIN"
	return response
while True:
	command = raw_input('serexona > ')
	response = handle_command(command)
	print response
	print	Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "Oh hi there, Please input ERROR..."

    elif command.find(COMMAND2) >= 0:
        for i in range(100000000000000000000000000000):
            response = "ERROR..."
        
    return response

