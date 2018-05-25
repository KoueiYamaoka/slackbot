# -*- coding: utf-8 -*-

from slackbot.bot import listen_to, respond_to
from requests import get
from re import match
from math import log10
import datetime
import json


@listen_to('event')
@respond_to('event')
def getDateEvent(message, *params):
    # Set tesmup's URL and API_KEY
    with open('config.json', 'r') as f:
        config = json.load(f)
    URL = config['teamup']['URL']
    API_KEY = config['teamup']['API_KEY']

    opt = message.body['text'].split()
    nopt = len(opt)

    # Check error
    err = checksyntax(message, opt)
    if err:
        return

    # get today's event if nopt == 1
    date = str(datetime.date.today()).split('-')
    day = 'today'
    if nopt > 1:
        if opt[1] == '-t':
            # get tomorrow's event
            date[2] = str(int(date[2]) + 1)
            day = 'tomorrow'

        elif opt[1] == '-d':
            # get events of a specified date
            year = date[0]
            date = opt[2].split('/')
            if len(date) == 2:
                date.insert(0, year)
            if int(log10(int(date[0])) + 1) == 2:
                date[0] = '20' + date[0]
            day = 'someday'

    date = [int(s) for s in date]
    # Check error and convert the format of date
    date, err = convertDate(message, date)
    if err:
        return
    # get event
    getSchedule(message, date, day, URL, API_KEY)


def getSchedule(message, date, day, teamup_URL, API_KEY):
    # Get event from teamup
    URL = teamup_URL + 'events?startDate=' + date + '&endDate=' + date
    API_KEY = {'Teamup-Token': API_KEY}
    r = get(URL, headers=API_KEY).json()
    events = r['events']

    if day == 'today':
        msg = '今日の予定は...\n'
    elif day == 'tomorrow':
        msg = '明日の予定は...\n'
    elif day == 'someday':
        msg = date.replace('-', '/') + ' の予定は...\n'

    # get events
    for i in range(0, len(events)):
        ce = events[i]
        # Title
        msg += 'Title: {}'.format(ce['title'])

        # Who
        if len(ce['who']) == 0:
            msg += '\n'
        else:
            msg += ' ({})\n'.format(ce['who'])

        # When
        if ce['all_day']:
            msg += 'When: 終日\n'
        else:
            msg += 'When: {}-{}\n'.format(ce['start_dt'][11:16],
                                          ce['end_dt'][11:16])
        # Location
        if len(ce['location']) != 0:
            msg += 'Location: {}\n'.format(ce['location'])

        # Subcalendars
        for idx, val in enumerate(ce['subcalendar_ids']):
            if idx == 0:
                msg += 'Calendar: '
            else:
                msg += ', '
            scURL = teamup_URL + 'subcalendars/' + str(val)
            sc = get(scURL, headers=API_KEY).json()['subcalendar']
            msg += '{}'.format(sc['name'])
        msg += '\n'

        # Notes
        if ce['notes'] is not None:
            notes = ce['notes'].splitlines()
            for i in range(0, len(notes)):
                if i == 0:
                    msg += 'Notes: '
                else:
                    msg += ' ' * 13
                msg += '{}\n'.format(notes[i][3:-4])
        msg += '\n'

    message.reply(msg)


def checksyntax(message, opt):
    nopt = len(opt)

    if nopt == 1:
        return 0
    else:
        if match('-(t|d)', opt[1]) is None:
            msg = 'Error: 使用できるオプションは以下の通りです．\n' \
              + '-t: 明日の予定を表示\n' \
              + '-d: YYYY-MM-DD or MM-DD で指定された日時の予定を表示\n'
            message.send(msg)
            return 1


def convertDate(message, date):
    try:
        date = str(datetime.date(date[0], date[1], date[2]))
        flag = 0
    except ValueError:
        msg = 'Error: 日付の指定方法は以下の3種類です．\n' \
          + 'YYYY-MM-DD, YY-MM-DD, MM-DD\n' \
          + '2000年代であれば上位2桁を，今年であれば年を省略できます．'
        message.send(msg)
        flag = 1
    return date, flag
