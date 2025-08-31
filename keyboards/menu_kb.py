from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = 'Каталог')],
                                     [KeyboardButton(text = 'Профиль')],
                                     [KeyboardButton(text = 'Контакты')],
                                     [KeyboardButton(text = 'О нас')]],
                                     resize_keyboard = True,
                                     input_field_placeholder = 'Выберите пункт меню')