# Put your commands here
COMMAND1 = "placeholder"
COMMAND2 = "what is your favorite food?"
COMMAND3 = "why was 8 afraid of 7?"
COMMAND4 = "what are your grades?"
COMMAND5 = "can you change my grades?"
COMMAND6 = "what is your favorite food?"
def handle_command(command):
	response = ""
	if COMMAND1 in command:
		response = "a placeholder"
	elif COMMAND2 in command:
		response = "pizza"
	elif COMMAND3 in command:
		response = "!!!7,8(ate),9!!!"
	elif COMMAND4 in command:
		response = "Math: A+ , Science: A+ , Social Studies: F- , Reading: F- , Writing: F-"
	elif COMMAND5 in command:
		response = "Sure!  Math: A+ , Science: A+ , Social Studies: A+ , Reading: A+ , Writing: A+  "
	elif COMMAND6 in command:
		response = ""
	#else:
	#	response = "Why thank you, I don't know what else to say."
	return response


