# coding: utf-8

from slackbot.bot import respond_to


@respond_to('ping')
def pong(message):
    message.reply('pong')
