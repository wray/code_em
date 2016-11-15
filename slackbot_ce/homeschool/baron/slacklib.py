# Put your commands here
COMMAND1 = "what is you harry potter house?"
COMMAND2 = "1 times 8,888"
COMMAND3 = "what is your favrit tree?"
COMMAND4 = "hello world"
COMMAND5 = "space unicorn"
COMMAND6 = "what is the couler of the sky"

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

    elif command.find(COMMAND4) >= 0:
           response = "its me"

    elif command.find (COMMAND5) >= 0:
            response = "soring thru the sky delivering the rainbow all a round the world"

     elif command.find (COMMAND6) >= 0:
            response = "i dont have eyes" 
       
      
        
    return response

