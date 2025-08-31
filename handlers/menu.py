from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from config import user

import keyboards.catalog_kb as kb

menu_router = Router()

@menu_router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer(text = 'Добро пожаловать в наш магазин', reply_markup = kb.main)

@menu_router.message(F.text == 'Контакты')
async def contacts(message: Message):
    await message.answer(text = '+996-777-777-777\n+996-555-555-555\n+996-777-555-777')

@menu_router.message(F.text == 'О нас')
async def market(message: Message):
    await message.answer(text = '''
AVIATOR – это уникальный магазин премиум одежды, который поможет вам выразить свою индивидуальность. Он был создан в 2017 году и за период своего существования завоевал безоговорочное уважение и доверие более чем у 10 тысяч клиентов.

Среди большого ассортимента продукции можно найти все: от курток, брюк и футболок до аксессуаров и обуви. Не важно, что именно Вы выберете, ведь в любом случае можете быть уверены, что получите качественный предмет гардероба, который прослужит длительное время.

Главная миссия магазина – дать возможность украинцам покупать качественную брендовую одежду по европейской цене.

AVIATOR предлагает только оригинальную продукцию для мужчин и женщин от самых известных мировых брендов. На сайте можно приобрести модели от Aeronautica Militare, Bomboogie, Parajumpers, MC2 Saint Barth, Paul&Shark, La Martina, Navigare, Schott, Plein Sport, Bikkembergs, Bertucci, Calvin Klein, Cockpit USA, Hugo Boss, Stone Island, Premiata, Tomy Hilfiger, Invicta, Versace Jeans, CR7 и других именитых производителей.

Отдельного внимания заслуживает то, что AVIATOR является эксклюзивным и официальным дистрибьютором итальянского бренда премиум одежды Aeronautica Militare в Украине. Товары этого бренда можно заказать онлайн или купить в одном из наших монобрендовых магазинов, которые находятся в:

''')
    
