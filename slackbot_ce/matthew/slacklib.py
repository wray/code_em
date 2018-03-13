import json

# Put your commands here

COMMAND1 = "who is sirtomato"
COMMAND2 = "talk in binary"
COMMAND3 = "i dont like you"
COMMAND4 = "brit"
COMMAND5 = "h@ck3r_l1f3"
COMMAND6 = "leaderboard"
COMMAND7 = "math"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "A cuber/coder that loves Arch Linux and tiling window managers."
    elif command.find(COMMAND2) >= 0:
        response = """01010111 01101000 01111001 00100000 01100001 01110010 01100101 00100000 01111001 01101111 01110101 00100000 01100001 01100010 01110101 01110011 01101001 01101110 01100111 00100000 01101101 01111001 00100000 01110000 01101111 01110111 01100101 01110010 01110011 00111111 00100000 01010111 01101000 01111001 00100000 01100100 01101111 00100000 01111001 01101111 01110101 00100000 01101000 01100001 01110110 01100101 00100000 01110100 01101000 01100101 00100000 01110100 01101001 01101101 01100101 00100000 01110100 01101111 00100000 01100100 01100101 01100011 01101111 01100100 01100101 00100000 01110100 01101000 01101001 01110011 00111111 """
    elif command.find(COMMAND3) >= 0:
        response = "Well, I don't like you either!"
    elif command.find(COMMAND4) >= 0:
        response = "'Ello!'"
    elif command.find(COMMAND5) >= 0:
        response="""
        Hacking user @noobish_security...%%%%done.%%

        downloading fs...%%
        '/home' -- DONE%%
        '/bin' -- DONE%%
        '/usr' -- DONE%%%%%%
        '/etc' -- DONE%%%%
        '/boot' -- DONE %%

        searching for passwords...%%DONE
        this idiot does not have /etc/shadow...
        running `john /etc/passwd`...%%%%%%%%%%DONE
        root password is `password123` :%% wow, this guy is so dumb. %%
        running `cat rootpass.txt | su -`
        waiting...%%%%DONE
        running script...
        [*] Installing kernel-mode rootkit...%%%%%%DONE
        [*] Regenerating intrd-2.64.img%%%%
        [*] Creating hacked initramfs%%
        [*] All done. Have a nice day, you hacked fool. Ha Ha Ha! :)"""
    elif COMMAND6 in command:
        # Custom commandhandler for sirexa

        if command.lower() == "leaderboard help":
            response = """sirexa leaderboard v0.0.1
                give point: `@sirexa leaderboard +username`
                example: `@sirexa leaderboard +sirtomato`
                
                take point: `@sirexa leaderboard -username`
                example: `@sirexa leaderboard -notsirtomato`
                
                leaderboard: `@sirexa leaderboard points`"""
        elif command.lower().startswith("leaderboard +"):
            pointfile = open("points.json", "r")
            points = json.load(pointfile)
            pointfile.close()
            user = command.lower()[12:]
            try:
                points[user] = points[user] + 1
                return "@"+user[1:]+" has "+points[user]+" points."
            except:
                points[user] = 1
                return "@"+user[1:]+" has 1 point"
            pointfile = open("points.json", "w")
            jsonpoints = json.dumps(points, sort_keys=True, indent="4")
            pointfile.write(jsonpoints)
            pointfile.close()
        elif command.lower().startswith("leaderboard -"):
            pointfile = open("points.json", "r")
            points = json.load(pointfile)
            pointfile.close()
            user = command.lower()[12:]
            try:
                points[user] = points[user] - 1
                return "@"+user[1:]+" has "+points[user]+" points."
            except:
                points[user] = -1
                return "@"+user[1:]+" has -1 points"
            jsonpoints = json.dumps(points, sort_keys=True, indent="4")
            pointfile.write(jsonpoints)
            pointfile.close()
        else:
            for i in points.keys():
                print(i + "\t" + points[i])
    if COMMAND7 in command:
        response = exec(command.split("math ")[0])

    return response

command = raw_input("[<-] command: ")
out = handle_command(command)
print "[->] " + out