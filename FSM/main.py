from aiogram.fsm.state import State, StatesGroup

class User(StatesGroup):
    id = State()
    name = State()
    balance = State()
    is_true = State()
    choice = State()
    choice2 = State()
    is_false = State()

