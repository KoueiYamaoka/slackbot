# coding: utf-8

from slackbot.bot import listen_to, respond_to
import json, re, datetime
from numpy import *

@respond_to(r'^(meshi)(\s\w+){0,2}$')
@listen_to(r'^(meshi)(\s\w+){0,2}')
def meshi_search(message, *args):
    fid = open('./plugins/data/shop.json', 'r')
    shops = json.load(fid)
    cmd = message.body['text']
    opt = cmd.split(' ')
    flag = [0, 'none']
    now = datetime.datetime.now()
    nowtime = now.hour * 100 + now.minute
    day = now.weekday()
    day = 6 if day == 0 else day - 1
    # check arguments
    for s in opt:
        if re.match('ramen|ラーメン|麺', s):
            flag[0] = 1
        if re.match('定食', s):
            flag[0] = 2
        if re.match('ファミレス|レストラン', s):
            flag[0] = 3
        if re.match('天久保|amakubo', s):
            flag[1] = 'amakubo'
        if re.match('桜|sakura', s):
            flag[1] = 'sakura'
        if re.match('徒歩|walk', s):
            flag[1] = 'nearby'
    # make list
    list = []
    if flag[0] == 1:
        list.extend(shops['ramen'])
        list.extend(shops['teishoku'])
        list.extend(shops['restaurant'])
        list.extend(shops['other'])
    if flag[0] == 1:
        list.extend(shops['ramen'])
    if flag[0] == 2:
        list.extend(shops['teishoku'])
    if flag[0] == 3:
        list.extend(shops['restaurant'])
    while True:
        meshiya = random.choice(list)
        # check area
        if 'none' != flag[1]:
            if meshiya['area'] != flag[1]:
                continue
        # check time
        for t in meshiya['open'][day]:
            if t[0] <= nowtime <= t[1]:
                message.send(meshiya['name'] + ' が提案されました')
                return

@respond_to('^(man meshi)')
@listen_to('^(man meshi)')
def man_meshi(message, *args):
    msg = 'Usage:\n' + \
          '```\n' + \
          'meshi [category area](optional)' + \
          '```\n' + \
          'Example:\n' + \
          '```\n' + \
          'meshi\n' + \
          'meshi ご飯 天久保\n' + \
          '```'
    message.send(msg)
