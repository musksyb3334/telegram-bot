
from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
import watch, add_ad, withdraw

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

watch.register_handlers(dp)
add_ad.register_handlers(dp)
withdraw.register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
