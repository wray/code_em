# Put your commands here
COMMAND1 = "hi"
COMMAND2 = "error..."

#Your handling code toes in this function
def handle_command(command):

    response = ""
    if command.find(COMMAND1) >= 0:
        response = "Oh hi there, Please input ERROR..."

    elif command.find(COMMAND2) >= 0:
        response = "ERROR..."
       #for i in range(5):
            #response = "ERROR..."
        
    return response

