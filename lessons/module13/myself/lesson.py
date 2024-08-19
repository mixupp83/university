from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7249341772:AAHHFBW3zLzr2Aco1eN1fu9Y-C4hJ_1ZaWY"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=["Urban"])
async def urban_massege(message):
    print('Urban message')
    await message.answer('Urban message')


@dp.message_handler(commands=['start'])
async def start_messadge(message):
    print('Start message')
    await message.answer('Рады Вас видеть в нашем боте!')


@dp.message_handler()
async def all_message(message):
    print('Мы получили сообщение')
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
