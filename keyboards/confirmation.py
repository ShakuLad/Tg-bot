from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

confirm = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = 'Да')],
                                     [KeyboardButton(text = 'Нет')]],
                                     resize_keyboard = True,
                                     input_field_placeholder = 'Подтвердите действие')