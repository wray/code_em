# Put your commands here

COMMAND1 = "who is mr_techie"
COMMAND2 = "talk in binary"
COMMAND3 = "i dont like you"
COMMAND4 = "brit"
COMMAND5 = "h@ck3r_1if3"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """

    response = ""
    if command.find(COMMAND1) >= 0:
        response = "I cannot reveal his identity."
    elif command.find(COMMAND2) >= 0:
        response = """01001001 00100000 01100110 01110101 01100011 01101011 0
        1101001 01101110 01100111 00100000 01101000 01100001 01110100 01100101
        00100000 01111001 01101111 01110101!!!"""
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
        running 'john /etc/passwd'...%%%%%%%%%%DONE
        root password is 'password123' :%% wow, this guy is so dumb. %%
        running 'cat rootpass.txt | su -'
        waiting...%%%%DONE
        running script...
        [*] Installing kernel-mode rootkit...%%%%%%DONE
        [*] Regenerating intrd-2.64.img%%%%
        [*] Creating hacked initramfs%%
        [*] All done. Have a nice day :)"""

    return response
