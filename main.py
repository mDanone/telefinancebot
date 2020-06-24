from subprocess import Popen
from subprocess import PIPE
import investpy

from telegram import Bot, Update
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler
from telegram.ext import Filters

from Buttons import BUTTON1_YANDEX
from Buttons import BUTTON2_APTEKA36_6
from Buttons import BUTTON3_SBERBANK
from Buttons import BUTTON4_MCDONALDS
from Buttons import get_base_reply_keyboard
from config import TG_TOKEN


def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Здравствуй, я могу отправить тебе курсы по акциям',
        reply_markup=get_base_reply_keyboard()
    )


def do_help(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Если хотите узнать курс акций нажимайте на'
             ' кнопки клавиатуры',
    )


def do_info(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Данный бот может показать вам курсы акций,'
             'в скором времени добавим аналитику курсов',
    )


def do_time(bot: Bot, update: Update):
    process = Popen("echo %date% %time:~-11,8%", shell=True, stdout=PIPE)
    text, error = process.communicate()
    if error:
        text = "Произошла ошибка, время неизвестно"
    else:
        text = text.decode("utf-8")
    bot.send_message(
        chat_id=update.message.chat_id,
        text=text
    )


def do_echo(bot: Bot, update: Update):
    chat_id = update.message.chat_id
    text = update.message.text
    if text == BUTTON2_APTEKA36_6:
        df = investpy.get_stock_recent_data(stock='aptk', country='russia')
        bot.send_message(
            chat_id=chat_id,
            text="На открытии Курс акций Аптека36.6 : {} {}, на закрытии : {} {}"
                 " Изменение составило {} {}".format(df['Open'][-1], df['Currency'][-1],
                                                     df['Close'][-1], df['Currency'][-1],
                                                     "%2f" % (df['Close'][-1] - df['Open'][-1]),
                                                     df['Currency'][-1]),
        )
    elif text == BUTTON1_YANDEX:
        df = investpy.get_stock_recent_data(stock='yndx', country='russia')
        bot.send_message(
            chat_id=chat_id,
            text="На открытии Курс Яндекса : {} {}, на закрытии : {} {}"
                 " Изменение составило {} {}".format(df['Open'][-1], df['Currency'][-1],
                                                     df['Close'][-1], df['Currency'][-1],
                                                     "%2f" % (df['Close'][-1] - df['Open'][-1]),
                                                     df['Currency'][-1]),
        )
    elif text == BUTTON3_SBERBANK:
        df = investpy.get_stock_recent_data(stock='SBER', country='russia')
        bot.send_message(
            chat_id=chat_id,
            text="На открытии курс Сбербанка : {} {}, на закрытии : {} {}"
                 " Изменение составило {} {}".format(df['Open'][-1], df['Currency'][-1],
                                                     df['Close'][-1], df['Currency'][-1],
                                                     "%2f" % (df['Close'][-1] - df['Open'][-1]),
                                                     df['Currency'][-1]),
        )
    elif text == BUTTON4_MCDONALDS:
        df = investpy.get_stock_recent_data(stock='MCD', country='United States')
        bot.send_message(
            chat_id=chat_id,
            text="На открытии курс McDonalds : {} {}, на закрытии : {} {}"
                 " Изменение составило {} {}".format(df['Open'][-1], df['Currency'][-1],
                                                     df['Close'][-1], df['Currency'][-1],
                                                     "%2f" % (df['Close'][-1] - df['Open'][-1]),
                                                     df['Currency'][-1]),
        )


def main():
    bot = Bot(
        token=TG_TOKEN,
    )
    updater = Updater(
        bot=bot
    )
    start_handler = CommandHandler('start', do_start)
    time_handler = CommandHandler('time', do_time)
    help_handler = CommandHandler('help', do_help)
    info_handler = CommandHandler('info', do_info)
    echo_handler = MessageHandler(Filters.text, do_echo)
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(info_handler)
    updater.dispatcher.add_handler(time_handler)
    updater.dispatcher.add_handler(echo_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
