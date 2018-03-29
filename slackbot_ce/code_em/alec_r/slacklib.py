# Put your commands here
COMMAND1 = "is this meme dank?"
COMMAND2 = "yes"
COMMAND3 = "no"
COMMAND4 = "how much is the new MacBook Pro?"
COMMAND5 = "yea"
COMMAND6 = "how many things has Linus dropped?"

# Your handling code goes in this function
def handle_command(command):

	response = ""
	if COMMAND1 in command:
		response = "It depends. Is it on r/dankmemes?"
	if COMMAND2 in command:
		response = "Yes. Your meme is in fact dank."
	if COMMAND3 in command:
		response = "boi u best be on r/dankmemes"
	if COMMAND4 in command:
		response = "Did you mean _**DongleBook Pro**_?"
	if COMMAND5 in command:
		response = "boiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
	if COMMAND6 in command:
		response = "I'm sorry, I had the answer but Linus dropped it."
        
	return response
