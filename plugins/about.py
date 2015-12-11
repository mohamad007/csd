# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  about.py importado.{/cyan}'))

@bot.message_handler(commands=['about'])
def command_about(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        bot.send_message( cid, responses['about'][lang(cid)])
    else:
        bot.send_message( cid, responses['not_user'])
