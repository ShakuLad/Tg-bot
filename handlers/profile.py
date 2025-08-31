from aiogram import Router, F 
from aiogram.types import FSInputFile, Message
from aiogram.filters import Command
from config import user 


profile_router = Router()

@profile_router.message(F.text == 'Профиль')
async def contacts(message: Message):
    await message.answer(text = user.about())

