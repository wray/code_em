# Put your commands here
COMMAND1 = "would you rather live your entire life in a virtual reality where all of your wishes are granted, or in the real world?"
COMMAND2 = "would you rather be completely invisible for one day, or be able to fly for one day?"
COMMAND3 = "would you rather have four hands, or four feet?"
COMMAND4 = "would you rather be a reverse mermaid, or a reverse centaur?"
COMMAND5 = "would you rather have the ability to never be paper cut, or get something stuck in your eye?"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if COMMAND1 in command:
        response = "I would rather live on the real world... if I could... ;-;"
    if COMMAND2 in command:
        response = "I would rather be invisible because if you were able to fly, people would perform experiment on you. *see.. common sense..*"    
    if COMMAND3 in command:
        response = "I would rather be a monkey and have hand feet (4 hands), so I could grab stuffs with my feet."    
    if COMMAND4 in command:
        response = "I would rather be a reverse mermaid because fish are beautiful... *sobs in corner*"    
    if COMMAND5 in command:
        response = "I would rather have the ability to never get something stuck in my eye because I struggle..."  
    return response
