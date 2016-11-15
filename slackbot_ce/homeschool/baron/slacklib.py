# Put your commands here
COMMAND1 = "what is you harry potter house?"
COMMAND2 = "1 times 8,888"
COMMAND3 = "what is your favrit tree?"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "Greffendor"
          
    elif command.find(COMMAND2) >= 0:
         response = "8,888"

    elif command.find(COMMAND3) >= 0:
         response = "Pine tree"
       
      
        
    return response

