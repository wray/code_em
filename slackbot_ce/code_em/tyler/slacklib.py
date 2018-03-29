# Put your commands here
COMMAND1 = "hello"
COMMAND2 = "vine"
COMMAND3 = "what was before 1899"
COMMAND4 = "ooph"
COMMAND5 = "what is the weather"
COMMAND6 = "why"
# Your handling code goes in this function
def handle_command(command):
        response = ""
        if COMMAND1 in command:
                response = "is it me you're looking for"
        if COMMAND2 in command:
                response = "is dead"
        if COMMAND3 in command:
                response = "1898"
        if COMMAND4 in command:
                response = "k"
        if COMMAND5 in command:
                response = "floor going up on a Tuesday"
        if COMMAND6 in command:
                response = "are you single"
        return response
