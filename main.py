from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import asyncio

from handlers.start import start_router
from handlers.help import help_router
from handlers.market import market_router

TOKEN = '8316260931:AAFwiRSjP-uq73MHrRXXhqh47z3y6ih1T2w'
bot = Bot(token = TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(start_router)
    dp.include_router(help_router)
    dp.include_router(market_router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main=main())

num = 0