#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Criado em: 02/12/2018
#
# Por: Henrique Beckmann

import telepot
import subprocess as sub
import sympy
import re

bot = telepot.Bot("Bot API Token") 

def MathBot(msg):
    message = str((msg['text']))
    chat_id = (msg['chat']['id'])
    if message == '/start':
        bot.sendMessage(chat_id, 'Bem Vindo ao Math Bot')
    elif 'plot' in message:
        eq = re.findall("(\w+)[^.](.*[^\)])", message)[0][1]
        save_name = str(chat_id) + ".png"
        graph = sympy.plot(eq, show=False)
        graph = graph.backend(graph)
        graph.process_series()
        graph.fig.savefig(save_name)       
        bot.sendPhoto(chat_id, open(save_name, 'rb'))

    else:
        resp = sub.getoutput("qalc '%s'" %message)
        resp = re.findall("(.*= )(.*)", resp)[0][1]
        bot.sendMessage(chat_id, resp)


bot.message_loop(MathBot)

while True:
    pass
