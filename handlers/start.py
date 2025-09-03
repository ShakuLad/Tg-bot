from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from config import user

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import keyboards.menu_kb as kb
from keyboards.confirmation import confirm

class User(StatesGroup):
    id = State()
    name = State()
    balance = State()
    is_true = State()
    choice = State()
    choice2 = State()
    is_false = State()


start_router = Router()


@start_router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await state.set_state(User.choice)
    await message.answer('Как вас зовут')

@start_router.message(User.choice)
async def choice(message: Message, state: FSMContext):
    await state.set_state(User.choice2)
    await message.answer('Вы подтверждаете действия?', reply_markup = confirm)

@start_router.message(User.choice2)
async def choice2(message: Message, state: FSMContext):
    await state.set_state(User.choice2)
    await message.answer('Вы подтверждаете действия?', reply_markup = confirm)

# @start_router.message(User.name)
# async def name(message: Message, state: FSMContext):
#     await state.set_state(User.balance)
#     await state.update_data(name = message.text)
#     await message.answer('Введите ваш баланс')

# @start_router.message(User.balance)
# async def balance(message: Message, state: FSMContext):
#     await state.update_data(balance = int(message.text))
#     await state.update_data(id = message.from_user.id)
#     data = await state.get_data()
#     print(data['balance'])
#     await state.clear()
#     user.add_balance(data['balance'])
#     user.add_name(data['name'])
#     user.add_id(data['id'])
#     await message.answer(text = 'Мы получили все ваши данные', reply_markup = kb.main)
