from aiogram.dispatcher.filters.state import State, StatesGroup


class APPLICATION(StatesGroup):
    age = State()
    name = State()
    pxone = State()        
    fields = State()
    check = State()


