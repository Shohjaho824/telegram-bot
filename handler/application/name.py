from aiogram.types import Message
from aiogram.dispatcher import FSMContext


from loader import dp
from utils import texts, buttons
from utils.state import APPLICATION
from .handler import APPLICATION

from asyncio import create_task


async def application_handler_task(message: Message, state: FSMContext):

    name = message.text
    print(name)

    await state.update_data({
        'name': name
    })
    await message.answer(texts.AGE_HANDLER, reply_markup=buttons.AGE)

    await APPLICATION.age.set()

    
@dp.message_handler(content_types=['text'], state=APPLICATION.name)
async def passenger_handler(message: Message, state: FSMContext):
    await create_task(application_handler_task(message, state))


