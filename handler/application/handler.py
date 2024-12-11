from aiogram.types import Message, ReplyKeyboardMarkup
from aiogram.dispatcher import FSMContext

from loader import dp
from utils import texts, buttons
from utils.state import APPLICATION

@dp.message_handler(lambda message: message.text.startswith(buttons.ARIZA), state='*')
async def passenger_handler(message: Message, state: FSMContext):
    print(message.text)
    
    await message.answer(texts.NAME, reply_markup=buttons.NAME)
    await APPLICATION.name.set()
