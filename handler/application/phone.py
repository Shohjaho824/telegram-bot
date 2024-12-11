from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp
from utils import texts, buttons
from utils.state import APPLICATION

@dp.message_handler(content_types=['contact'], state=APPLICATION.pxone)
async def application_handler(message: Message, state: FSMContext):
    pxone = message.contact.phone_number

    await state.update_data({
        'pxone': pxone
    })

    data = await state.get_data()
    name = data.get('name')
    age = data.get('age')
    fields = data.get('fields')

    await message.answer(texts.check(
        name=name,
        age=age,
        pxone=pxone,
        fields=fields
    ), reply_markup=buttons.SEND_GROUP)

    await APPLICATION.check.set()

