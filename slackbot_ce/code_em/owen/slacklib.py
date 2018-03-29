# Put your commands here
COMMAND1 = "is it iphone10 or iphonex"
COMMAND2 = "do you like cake"
COMMAND3 = "do you like the walking dead"
COMMAND4 = "half-life 1 or half-life 2"
COMMAND5 = "do you like me"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if COMMAND1 in command:
        response = "Iphone10."
    if COMMAND2 in command:
        response = " YEEEEEEEEEEEESSSSSSSSSSSSSSSSSS!" 
    if COMMAND3 in command:
        response = "The show stinks but the comic is geat."
    if COMMAND4 in command:   
        response = "Half-life 1."
    if COMMAND5 in command:   
        response = "No."
        
        
        
        
        
    return response
