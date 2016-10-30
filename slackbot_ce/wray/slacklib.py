
COMMAND1 = "who are you"
COMMAND2 = "what can you do"

def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "I am a simpleton bot."
    elif command.find(COMMAND2) > = 0:
        response = "Not much right now... waiting for students to teach me."

    return response

