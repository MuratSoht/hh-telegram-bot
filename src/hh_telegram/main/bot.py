from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
# from hh_telegram.main.config import BOT_TOKEN
from src.hh_telegram.application.telegram.handlers import router

import asyncio


bot = Bot(token='7313468547:AAGqCPYZLx7hxmiPy_W3TvASM_uyNch5V6Q')
dp = Dispatcher(storage=MemoryStorage())

# @dp.message()
# async def send_welcome(message: types.Message):
#     await message.reply("Hello!")

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())