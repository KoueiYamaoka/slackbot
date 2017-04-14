# coding: utf-8

from slackbot.bot import listen_to, respond_to
from collections import OrderedDict
import random


@listen_to('(omikuji|おみくじ)')
@respond_to('(omikuji|おみくじ)')
def omikuji(message, not_use):
    message.send('あなたの運勢は...')

    o_set = (('大吉', 16), ('中吉', 13), ('小吉', 11), ('吉', 25), ('末吉', 10),
             ('凶', 20), ('大凶', 5))
    omikuji = OrderedDict(o_set)

    r = random.random() * 100
    tmp_val = 0

    for key in omikuji.keys():
        omikuji[key] += tmp_val
        tmp_val = omikuji[key]
        if r < tmp_val:
            message.send(key + 'です')
            return
