# -*- coding: utf-8 -*-

import sys
from slacker import Slacker
sys.path.append('/home/yamaoka/tsukuba/mmlab/slackbot')
import slackbot_settings


def get_user_list(slack):
    raw_data = slack.users.list().body

    users = {}
    for data in raw_data['members']:
        users[data['name']] = data['id']

    return users


def post_direct_message(username, message):
    slack = Slacker(slackbot_settings.API_TOKEN)
    users = get_user_list(slack)
    slack.chat.post_message(users[username], message, as_user=True)


if __name__ == '__main__':
    args = sys.argv
    post_direct_message(args[1], args[2] + ' execution is finished :slack:')
