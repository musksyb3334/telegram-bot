
from aiogram import types
from aiogram.dispatcher import Dispatcher
from config import ADMIN_USERNAME

def register_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['add_ad'])
    async def add_ad(message: types.Message):
        if message.from_user.username != ADMIN_USERNAME:
            await message.answer("❌ غير مصرح لك.")
            return
        await message.answer("✏️ أرسل نص الإعلان الجديد:")
