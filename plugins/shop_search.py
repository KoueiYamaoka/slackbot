# coding: utf-8

from slackbot.bot import listen_to, respond_to
import json, re, datetime
import random

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
    # check arguments
    for s in opt:
        if re.match('ramen|ラーメン|麺|:ramen:', s):
            flag[0] = 1
        if re.match('定食|teishoku', s):
            flag[0] = 2
        if re.match('ファミレス|レストラン', s):
            flag[0] = 3
        if re.match('天久保|amakubo', s):
            flag[1] = 'amakubo'
        if re.match('桜|sakura', s):
            flag[1] = 'sakura'
        if re.match('徒歩|walk', s):
            flag[1] = 'nearby'
        if re.match('春日|kasuga', s):
            flag[1] = 'kasuga'
    # make list
    mlist = []
    idx = 0
    meshiya = 0
    selected = []
    if flag[0] == 0:
        mlist.extend(shops['ramen'])
        mlist.extend(shops['teishoku'])
        mlist.extend(shops['restaurant'])
        mlist.extend(shops['other'])
    if flag[0] == 1:
        mlist.extend(shops['ramen'])
    if flag[0] == 2:
        mlist.extend(shops['teishoku'])
    if flag[0] == 3:
        mlist.extend(shops['restaurant'])
    for i in range(0, 50):
        idx = int(random.random() * len(mlist))
        meshiya = mlist[idx]
        # check area
        if 'none' != flag[1]:
            if meshiya['area'] != flag[1]:
                continue
        # check time
        for t in meshiya['open'][day]:
            if t[0] <= nowtime <= t[1]:
                selected.append(meshiya)
                mlist.pop(idx)
        if len(selected) == 3 or len(mlist) == 0:
            break
    outstr = ''
    if len(selected) != 0:
        for s in selected:
            outstr += ('・' + s['name'] + '\n')
        message.send(outstr)
    else:
        message.send('飯屋どこもやっていないんじゃないですか？')

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
