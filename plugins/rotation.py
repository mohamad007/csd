# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  rotation.py importado.{/cyan}'))


@bot.message_handler(
    func=lambda m: m.content_type == 'text' and m.text in [
        'ROTAÇÃO',
        'ROTACJA',
        'ФРИПИК',
        'ROTACION',
        'ROTATION',
        'ROTAZIONE'])
@bot.message_handler(commands=['rotation'])
def command_rotation(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        botan.track(
            botan_token,
            cid,
            to_json(m),
            "/rotation"
        )
    except:
        pass
    if not is_recent(m):
        return None
    if is_banned(uid) or is_banned(cid):
        if not extra['muted']:
            bot.send_chat_action(cid, 'typing')
            bot.reply_to(m, responses['banned'])
        return None
    if is_user(cid):
        txt = responses['rotation'][lang(cid)] + '\n'
        with open('extra_data/rotation.txt', 'rt') as f:
            txt += f.read()
        bot.send_chat_action(cid, 'typing')
        #bot.send_photo( cid, open('extra_data/rotation.jpg','rb'))
        bot.send_photo(cid, extra['rotation'])
        bot.send_message(cid, txt)
    else:
        bot.send_message(cid, responses['not_user'])


@bot.message_handler(commands=['update_rotation_text'])
def command_update_rotation(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        botan.track(
            botan_token,
            cid,
            to_json(m),
            "/update_rotation_text"
        )
    except:
        pass
    if not is_recent(m):
        return None
    if is_admin(uid):
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['update_rotation_text_1'])
        userStep[cid] = 'update_rotation_text'


@bot.message_handler(commands=['update_rotation_pic'])
def command_update_pic(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        botan.track(
            botan_token,
            cid,
            to_json(m),
            "/update_rotation_pic"
        )
    except:
        pass
    if not is_recent(m):
        return None
    if is_admin(uid):
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['update_rotation_pic_1'])
        userStep[cid] = 'update_rotation_pic'
