
COMMAND1 = "what is 4+4?"
COMMAND2 = "does a fish live in water?"
COMMAND3 = "what is 8x7?"

def handle_command(command):
	
	response = ""
	
	if COMMAND1 in command:
		response = "8"
	elif COMMAND2 in command:
		response = "Yes."
	
	elif COMMAND3 in command:
		response = "56"
	return response

