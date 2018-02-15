import os
from slackclient import SlackClient


BOT_NAME = 'sirexa'
CHANNEL_NAME = 'mission_control'

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

def get_id():
    id = None
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        # retrieve all users so we can find our bot
        users = api_call.get('members')
        for user in users:
            print(user.get('name'))
            if 'name' in user and user.get('name') == BOT_NAME:
                print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
                id = user.get('id')
    else:
        print("could not find bot user with the name " + BOT_NAME)

    return id

def get_user_name(id):
    api_call = slack_client_api_call("users.info",user=id)
    if api_call.get('ok'):
        return api_call.get('user').get('name')

def get_channel_id():
    id = None
    api_call = slack_client.api_call("channels.list")
    if api_call.get('ok'):
        # retrieve all channels so we can find our channel
        channels = api_call.get('channels')
        for channel in channels:
            print(channel.get('name'))
            if 'name' in channel and channel.get('name') == CHANNEL_NAME:
                print("Channel ID for '" + CHANNEL_NAME + "' is " + channel.get('id'))
                id = channel.get('id')
    else:
        print("could not find channel user with the name " + CHANNEL_NAME)

    return id

def get_group_id():
    id = None
    api_call = slack_client.api_call("groups.list")
    if api_call.get('ok'):
        # retrieve all channels so we can find our channel
        channels = api_call.get('groups')
        for channel in channels:
            print(channel.get('name'))
            if 'name' in channel and channel.get('name') == CHANNEL_NAME:
                print("Channel ID for '" + CHANNEL_NAME + "' is " + channel.get('id'))
                id = channel.get('id')
    else:
        print("could not find channel user with the name " + CHANNEL_NAME)

    return id


def get_channel_name(id):
    api_call = slack_client_api_call("channels.info",channel=id)
    if api_call.get('ok'):
        return api_call.get('channel').get('name')
