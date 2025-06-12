
from aiogram import types
from aiogram.dispatcher import Dispatcher

def register_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['watch'])
    async def watch_ad(message: types.Message):
        await message.answer("🚀 الإعلان هنا! شاهد واحصل على نقاط.")
