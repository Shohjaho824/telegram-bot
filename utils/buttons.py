from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import ReplyKeyboardMarkup


ARIZA = "Ariza topshirish✉️"


BASE_BACK = 'Bekor qilish❌'


START = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=ARIZA),
        ]
    ],
    resize_keyboard=True

)

NAME = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=BASE_BACK)
        ]
    ],
    resize_keyboard=True
)

AGE = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=BASE_BACK)
        ]
    ],
    resize_keyboard=True
)

PHONE_NUMBER = 'Telefon raqam yuborish📞'


PHONE = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=PHONE_NUMBER, request_contact=True)
        ],
        [
            KeyboardButton(text=BASE_BACK)
        ]
    ],
    resize_keyboard=True
)


F = 'FRONTEND'
B = 'BACKEND'

COUNT = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text=F),
            KeyboardButton(text=B),
        ],

        [
            KeyboardButton(text=BASE_BACK),
        ]

    ],

    resize_keyboard=True
)


CHECK = 'Tasdiqlash✅'


SEND_GROUP = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=CHECK)
        ],
        [
            KeyboardButton(text=BASE_BACK)
        ]
    ],
    resize_keyboard=True
)
