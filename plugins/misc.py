# -*- coding: utf-8 -*-

from slackbot.bot import listen_to, respond_to


# 例のやつ
@listen_to('5000兆円')
@respond_to('5000兆円')
def many_money(message):
    message.send(':super5::super0::super0::super0::super_cho::super_yen:\n'
                 ':space::space::hoshii_left::hoshii_center::hoshii_right:')


# 欲しいっていうとなにか言ってくる
@listen_to('欲しい')
@respond_to('欲しい')
def super_please(message):
    message.send(':hoshii_left::hoshii_center::hoshii_right:')


# このハゲーっていうと，違うだろーって言ってくる
@listen_to('このハゲー')
@respond_to('このハゲー')
def konohagee(message):
    message.send('違うだろー！:face_with_rolling_eyes::triumph::boom::anger:違うだろ！'
                 ':dizzy_face::anger::rage::anger::bomb:')
