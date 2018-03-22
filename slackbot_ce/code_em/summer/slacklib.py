# Put your commands here
COMMAND1 = "Hello. My name is Summer. Who are you?"
COMMAND2 = "Yes please!"
COMMAND3 = "Pattern Game"
COMMAND4 = "a,b"
COMMAND5 = "b,a"
# Your handling code goes in this function
def handle_command(command):

	response = ""
	if COMMAND1 in command:
		response = "My name is Lidiya. Would you like to play a game? "
	if COMMAND2 in command:
		response = "Great! Do you want to play a pattern game or, a math game?"
	if COMMAND3 in command: 
		response = "Ok. a,b,a,a,a,b, a,b,a,a, what two letters come next?"
	if COMMAND4 in command: 
		response = "Correct! Well, that was fun!"
	if COMMAND5 in command: 
		response = "Sorry, that's incorrect. Please try again."
	return response
