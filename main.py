import telebot
import config
import constants as Const
import datetime


telebot.apihelper.proxy = config.proxy
bot = telebot.TeleBot(config.token)


def read_data(filename):
    columns = 4
    data = []
    with open(filename) as f:
        f.readline()
        for line in f:
            parts = line.split(',')
            if len(parts) == columns:
                data_line = [parts[0], parts[1],
                             int(parts[2]), int(parts[3])]
                data.append(data_line)
    return data


data = read_data('birthdays.csv')
now = datetime.datetime.now()
today_dm = now.strftime("%d.%m")
today_m = now.strftime("%m")


def today_b(list):
    i = 0
    name = ''
    while i <= 36:
        if data[i][0] == str(today_dm):
            name = data[i][1]
        else:
            pass
        i += 1
    return name


todays_bday = today_b(data)


def month_b(list):
    i = 0
    names = ''
    while i <= 36:
        if str(data[i][0])[3:] == today_m:
            names += str(data[i][1]) + '\n'
        else:
            pass
        i += 1
    return names


months_bday = month_b(data)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, Const.msg_start)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, Const.msg_help)
    elif message.text == "/today":
        bot.send_message(message.from_user.id, Const.msg_today + todays_bday + Const.msg_suggest)
    elif message.text == "/yes":
        bot.send_message(message.from_user.id, Const.msg_card)
    elif message.text == "/no":
        bot.send_message(message.from_user.id, Const.msg_no)
    elif message.text == "/month":
        bot.send_message(message.from_user.id, Const.msg_this_month + months_bday)
    else:
        bot.send_message(message.from_user.id, Const.msg_no_const)


bot.polling(none_stop=True, interval=0)
