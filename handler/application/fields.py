from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp
from utils import buttons
from utils.state import APPLICATION

@dp.message_handler(content_types=('text'), state=APPLICATION.fields)
async def application_handler(message: Message, state: FSMContext):

    fields = message.text
    print(fields)
    
    await state.update_data({
        'fields': fields
    })

    data = await state.get_data()
    fields = data.get('fields')

    await message.answer(('ILTIMOS telefon raqamingizni yozib yuboring yoki pasatdagi telefon raqam yuborish tugmasini bosing'),
    reply_markup=buttons.PHONE)
    await APPLICATION.pxone.set()
