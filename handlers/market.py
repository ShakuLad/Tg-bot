from aiogram import Router, F 
from aiogram.types import FSInputFile, Message
from aiogram.filters import Command
from config import user 


market_router = Router()

@market_router.message(Command('market'))
async def market(message: Message):
    await message.answer(text = f'''Добро пожаловать {user.get['name']} в наш магазин''')
