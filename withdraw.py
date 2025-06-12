
from aiogram import types
from aiogram.dispatcher import Dispatcher
from config import ADMIN_USERNAME, USDT_WALLET

def register_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['withdraw'])
    async def withdraw_request(message: types.Message):
        await message.answer(f"🪙 لطلب سحب، أرسل رسالة إلى الإدارة: @{ADMIN_USERNAME}\nمحفظتك: {USDT_WALLET}")
