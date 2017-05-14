# -*- coding: utf-8 -*-

from slackbot.bot import listen_to, respond_to
import re
import math

@listen_to(r'^(\d+)(,|,\s)(\d+)(,|,\s)?(\s\d+|\d+)?(\s)?')
@listen_to(r'(\d+)(符|ふ)(\d+)(翻|飜|はん)(\s\d+|\d+)?(本場|ほんば)?')
@listen_to(r'(\d+)(翻|飜|はん)(\d+)(符|ふ)(\s\d+|\d+)?(本場|ほんば)?')
@respond_to(r'^(\d+)(,|,\s)(\d+)(,|,\s)?(\s\d+|\d+)?(\s)?')
@respond_to(r'(\d+)(符|ふ)(\d+)(翻|飜|はん)(\s\d+|\d+)?(本場|ほんば)?')
@respond_to(r'(\d+)(翻|飜|はん)(\d+)(符|ふ)(\s\d+|\d+)?(本場|ほんば)?')
def calc(message, *params):

    # set hu and han
    out_order = 0
    if re.match('(符|ふ)', params[1]):
        hu, han = int(params[0]), int(params[2])
        out_order = 1
    elif re.match('(翻|飜|はん)', params[1]):
        han, hu = int(params[0]), int(params[2])
    else:
        han, hu = int(params[0]), int(params[2])
        if han > hu:
            han, hu = hu, han
            out_order = 1
    # set homba
    if re.match('(本場|ほんば)', str(params[5])):
        homba = int(params[4])
    elif params[4] is not None:
        # message.send(params[4] + '本場で計算しますよ')
        homba = int(params[4])
    else:
        homba = 0

    # reject crazy input
    if han < 1 or not (20 <= hu <= 110) or (han == 1 and
                                            (hu == 20 or hu == 25)):
        message.send('そんな和了ありえません')
        return

    # round up
    hu_orig = hu
    hu = hu if hu == 25 else math.ceil(hu / 10) * 10

    # calc basic point
    basic_point = hu * 2**(han + 2)
    add_status = ""
    if basic_point > 2000:
        if han < 6:
            basic_point = 2000
            add_status = " 満貫"
        elif 6 <= han <= 7:
            basic_point = 3000
            add_status = " 跳満"
        elif 8 <= han <= 10:
            basic_point = 4000
            add_status = " 倍満"
        elif 11 <= han <= 12:
            basic_point = 6000
            add_status = " 三倍満"
        else:
            basic_point = 8000
            add_status = " 数え役満"

    # pay
    rh = 300 * homba
    th = 100 * homba
    msg = '```\n'
    if homba > 0:
        if out_order:
            msg += str(hu_orig) + '符' + str(han) + '飜 ' + str(homba) + \
                   '本場' + add_status + '\n'
        else:
            msg += str(han) + '飜' + str(hu_orig) + '符 ' + str(homba) + \
                   '本場' + add_status + '\n'
    else:
        if out_order:
            msg += str(hu_orig) + '符' + str(han) + '飜' + add_status + '\n'
        else:
            msg += str(han) + '飜' + str(hu_orig) + '符' + add_status + '\n'
    msg += '親: ' + str(ceil10(basic_point * 6) + rh) + \
          ' (' + str(ceil10(basic_point * 2) + th) + ' all)\n'\
          '子: ' + str(ceil10(basic_point * 4) + rh) + \
          ' (' + str(ceil10(basic_point * 1) + th) + \
          ', ' + str(ceil10(basic_point * 2) + th) + ')\n' + \
          '```'
    message.send(msg)


def ceil10(x):
    return math.ceil(x / 100) * 100
