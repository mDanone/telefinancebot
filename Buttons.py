from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup

BUTTON1_YANDEX = "Yandex"
BUTTON2_APTEKA36_6 = "Аптека36.6"
BUTTON3_SBERBANK = "Sberbank"
BUTTON4_MCDONALDS = 'McDonalds'


def get_base_reply_keyboard():
    keyboard = [
        [
            KeyboardButton(BUTTON1_YANDEX),
            KeyboardButton(BUTTON2_APTEKA36_6)

        ],
        [
            KeyboardButton(BUTTON3_SBERBANK),
            KeyboardButton(BUTTON4_MCDONALDS),
        ]
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
