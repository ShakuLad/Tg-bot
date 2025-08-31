from aiogram import Bot, Dispatcher
import asyncio

from handlers.start import start_router
from handlers.menu import menu_router
from handlers.profile import profile_router
from handlers.catalog import catalog_router


async def main():
    TOKEN = '8316260931:AAFwiRSjP-uq73MHrRXXhqh47z3y6ih1T2w'
    bot = Bot(token = TOKEN)
    dp = Dispatcher()
    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(profile_router)
    dp.include_router(catalog_router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main=main())
    except KeyboardInterrupt:
        print('бот выключен')
