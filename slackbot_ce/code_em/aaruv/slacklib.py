# Put your commands here
COMMAND1 = "epic yo "
COMMAND2 = "hello"
COMMAND3 = "what is your fav football team?"
COMMAND4 = "do you like mincraft?"
COMMAND5 = "what is your name"
# Your handling code goes in this function
def handle_command(command):	
	response = ""
	if COMMAND1 in command:
		response = "Huh?"

	if COMMAND2 in command:
		response = "you stink?"

	if COMMAND3 in command:
		response ="The FALCONS" 

	if COMMAND4 in command:
		response = " Yes" 

	if COMMAND5 in command:
		response = "EPic person"

	return response
    
