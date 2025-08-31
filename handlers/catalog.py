from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from config import user
from inline_button.shop import shoes
from inline_button.shop import tshirt
from inline_button.shop import jacket
from inline_button.shop import jeans

import keyboards.catalog_kb as kb
import keyboards.menu_kb as kb2


catalog_router = Router()

@catalog_router.message(F.text == 'Кроссовки')
async def menu(message: Message):
    photo = FSInputFile('static_files/images.jpeg')
    await message.answer_photo(photo = photo, caption = 'Стоимость товара: 100', reply_markup = shoes)

@catalog_router.callback_query(F.data == 'shoes')
async def shoes_1(callBack: CallbackQuery):
    user.minus_balance(user.get_product1())
    user.add_orders('Кроссовки')
    await callBack.message.answer(text = f"Вы успешно купили кроссовки, теперь ваш баланс {user.get_balance()}")


@catalog_router.message(F.text == 'Футболки')
async def menu2(message: Message):
    photo = FSInputFile('static_files/6528aa77160e94620547c408-white-tshirt-for-men-gildan-2000-men.jpg')
    await message.answer_photo(photo = photo, caption = 'Стоимость товара: 50', reply_markup = tshirt)

@catalog_router.callback_query(F.data == 'tshirt')
async def t_shirt(callBack: CallbackQuery):
    user.minus_balance(user.get_product2())
    user.add_orders('Футболка')
    await callBack.message.answer(text = f"Вы успешно купили футболку, теперь ваш баланс {user.get_balance()}")


@catalog_router.message(F.text == 'Куртки')
async def menu3(message: Message):
    photo = FSInputFile('static_files/Uk-Mens-Ma1-Bomber-Jacket-Tactical-Air-Navy-Pilot-Motorbike-Hip-Hop-Jacket.jpeg')
    await message.answer_photo(photo = photo, caption = 'Стоимость товара: 300', reply_markup = jacket)

@catalog_router.callback_query(F.data == 'jacket')
async def jackets(callBack: CallbackQuery):
    user.minus_balance(user.get_product3())
    user.add_orders('Куртка')
    await callBack.message.answer(text = f"Вы успешно купили куртку, теперь ваш баланс {user.get_balance()}")


@catalog_router.message(F.text == 'Джинсы')
async def menu4(message: Message):
    photo = FSInputFile('static_files/eljdp00106_element,f_bnt0_frt1.jpg')
    await message.answer_photo(photo = photo, caption = 'Стоимость товара: 150', reply_markup = jeans)

@catalog_router.callback_query(F.data == 'jeans')
async def jeans_1(callBack: CallbackQuery):
    user.minus_balance(user.get_product4())
    user.add_orders('Джинсы')
    await callBack.message.answer(text = f"Вы успешно купили джинсы, теперь ваш баланс {user.get_balance()}")


@catalog_router.message(F.text == 'Назад')
async def menu5(message: Message):
    await message.answer(text = 'Меню', reply_markup = kb2.main)