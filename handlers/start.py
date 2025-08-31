from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from config import user

import keyboards.menu_kb as kb

start_router = Router()

@start_router.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет', reply_markup = kb.main)
