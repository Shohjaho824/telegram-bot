from aiogram. types import Message
from aiogram.dispatcher import FSMContext


from loader import dp, bot
from utils import buttons, texts
from utils.env import GROUP_ID
from utils.state import APPLICATION


@dp.message_handler(lambda message: message.text.startswith(buttons.CHECK), state=APPLICATION.check)
async def check_handler(message: Message, state: FSMContext):
    
    data = await state.get_data()
    name = data.get('name')
    age = data.get('age')
    pxone = data.get('phone')
    fields = data.get('fields')
    
    await bot.send_message(
    chat_id=GROUP_ID,
    text=texts.check(
        name=name,
        age=age,
        pxone=pxone,
        fields=fields
    )
    )


    await message.answer('Arizangiz ADMIN ga yuborildi!')