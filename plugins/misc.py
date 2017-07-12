# coding: utf-8

from slackbot.bot import listen_to, respond_to

# 例のやつ
@listen_to('5000兆円')
@respond_to('5000兆円')
def many_money(message):
    message.send(':super5::super0::super0::super0::super_cho::super_yen:\n' \
                 ':space::space::hoshii_left::hoshii_center::hoshii_right:')

# アルファベット，数字，仮名，漢字の後に「欲しい」が続くと何か言ってくる
@listen_to('([a-zA-Z0-9]|[\u3041-\u3096]|[\u30A1-\u30FA]|' \
           '[\u3400-\u9FFF\uF900-\uFAFF]|[\uD840-\uD87F]|[\uDC00-\uDFFF])欲しい')
@respond_to('([a-zA-Z0-9]|[\u3041-\u3096]|[\u30A1-\u30FA]|' \
            '[\u3400-\u9FFF\uF900-\uFAFF]|[\uD840-\uD87F]|[\uDC00-\uDFFF])欲しい')
def super_please(message, args):
    message.send(':hoshii_left::hoshii_center::hoshii_right:')
