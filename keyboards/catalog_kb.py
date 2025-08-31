from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = 'Кроссовки')],
                                     [KeyboardButton(text = 'Футболки')],
                                     [KeyboardButton(text = 'Куртки')],
                                     [KeyboardButton(text = 'Джинсы')],
                                     [KeyboardButton(text = 'Назад')]],
                                     resize_keyboard = True,
                                     input_field_placeholder = 'Выберите товар')