# coding: utf-8

from slackbot.bot import listen_to, respond_to
import time

@respond_to('^(vote|投票) (\d|\d-\d)')
@listen_to('^(vote|投票) (\d|\d-\d)')
def vote(message, *args):
    num_list = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'keycap_ten'
    }
    num = args[1].split("-")
    if len(num) == 1:
        num.insert(0, 1)
    for i in range(int(num[0]), int(num[1]) + 1):
        message.react(num_list[i])
        time.sleep(1)
