import os
import sys
import time
from slackclient import SlackClient

import bot_id
import glob
import importlib

# Instructor and student imports
names_paths = glob.glob("./*/slacklib.py")
names_homeschool_paths = glob.glob("./homeschool/*/slacklib.py")
names_code_em_paths = glob.glob("./code_em/*/slacklib.py")
names = []
names_homeschool = []
names_code_em = []
for i in range(0, len(names_paths)):
    path = names_paths[i]
    path.lstrip("./")
    path.strip("/slacklib.py")
    names.append(path)
    
for i in range(0, len(names_homeschool_paths)):
    path = names_homeschool_paths[i]
    path.lstrip("./")
    path.strip("/slacklib.py")
    names.append(path)

for i in range(0, len(names_code_em_paths)):
    path = names_code_em_paths[i]
    path.lstrip("./")
    path.strip("/slacklib.py")
    names.append(path)

for i in range(0, len(names)):
    importlib.importmodule(i)
 
for i in range(0, len(names_homeschool)):
    importlib.importmodule(i)
       
for i in range(0, len(names_code_em)):
    importlib.importmodule(i)

# constants
try:
    AT_BOT = "@" + bot_id.get_id()
    CHANNEL = bot_id.get_group_id()
    print(CHANNEL)
except TypeError:
    pass

# instantiate client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
        Need to determine an algorithm for student overloaded commands.
    """

    response = ''
    
    try:
        response = wray.handle_command(command)
        response += joe.handle_command(command)
        response += chris.handle_command(command)
        response += matthew.handle_command(command)
        response += homeschool.baron.handle_command(command)
        response += homeschool.elliot.handle_command(command)
        response += homeschool.kaleb.handle_command(command)
        response += homeschool.owen.handle_command(command)
        response += homeschool.vivian.handle_command(command)
        response += code_em.alec.handle_command(command)
        response += code_em.coy.handle_command(command)
        response += code_em.hadley.handle_command(command)
        response += code_em.qiuqiu.handle_command(command)
        response += code_em.zb.handle_command(command)
        response += code_em.aidan.handle_command(command)
        response += code_em.alex.handle_command(command)
        response += code_em.taixi.handle_command(command)
        response += code_em.al_kareem.handle_command(command)
        
    except:
        response += 'Unexpected Error.'

    print("["+response+"]")
    
    if len(response) == 0:
        response = "Why thank you, I don't know what else to say."

    # Split responses by %% and then add a delay in between
    # First test with separate postings, better approach will be
    # to use the chat.update command which will requires the ts back
    # from the orginial post.

    responses = response.split('%%')

    for response in responses:
    
        api_response = slack_client.api_call("chat.postMessage", channel=channel,
                                text=response, as_user=True)
        print(api_response)
        time.sleep(0.5)

def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    print(output_list)
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and output['channel'] == CHANNEL:
                print("Entering Mission Control")
                #joe.slacklib.blink_green()
                wray.slacklib.mission_control(bot_id,output)

            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            print(command,channel)
            if command and channel:
                handle_command(command, channel)
                
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")



