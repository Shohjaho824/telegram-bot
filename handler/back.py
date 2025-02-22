from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp
from utils import buttons, texts
from .start import start_handler



@dp.message_handler(lambda message: message.text.startswith(buttons.BASE_BACK), state="*")
async def passenger_handler(message: Message, state: FSMContext):
    print(message.text)
    await start_handler(message, state)