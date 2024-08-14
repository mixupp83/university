from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=["Urban"])
async def urban_massege(message):
    print('Urban message')


@dp.message_handler(commands=['start'])
async def start_messadge(message):
    print('Start message')


@dp.message_handler()
async def all_message(message):
    print('Мы получили сообщение')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
