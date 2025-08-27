from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile

from config import user


start_router = Router()

@start_router.message(CommandStart())
async def start(message: Message):
    user['id'] = message.from_user.id
    user['name'] = message.from_user.full_name

    photo = FSInputFile('')
    await message.answer_photo(photo = photo, caption = f'''{user.get('hello')} Что бы перейти в ''')