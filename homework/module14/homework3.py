from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

api = "API-TOKEN"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.add(KeyboardButton('Рассчитать'))
main_keyboard.add(KeyboardButton('Информация'))
main_keyboard.add(KeyboardButton('Купить'))

buy_inline_keyboard = InlineKeyboardMarkup()
buy_inline_keyboard.add(InlineKeyboardButton('Product1', callback_data='product_buying'))
buy_inline_keyboard.add(InlineKeyboardButton('Product2', callback_data='product_buying'))
buy_inline_keyboard.add(InlineKeyboardButton('Product3', callback_data='product_buying'))
buy_inline_keyboard.add(InlineKeyboardButton('Product4', callback_data='product_buying'))


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=main_keyboard)


@dp.message_handler(lambda message: message.text == 'Купить')
async def get_buying_list(message: types.Message):
    products = [
        {'name': 'Product1', 'description': 'Описание 1', 'price': 100, 'image': 'https://example.com/image1.jpg'},
        {'name': 'Product2', 'description': 'Описание 2', 'price': 200, 'image': 'https://example.com/image2.jpg'},
        {'name': 'Product3', 'description': 'Описание 3', 'price': 300, 'image': 'https://example.com/image3.jpg'},
        {'name': 'Product4', 'description': 'Описание 4', 'price': 400, 'image': 'https://example.com/image4.jpg'}
    ]

    for product in products:
        await message.answer_photo(photo=product['image'],
                                   caption=f"Название: {product['name']} | Описание: {product['description']} | Цена: {product['price']}")

    await message.answer('Выберите продукт для покупки:', reply_markup=buy_inline_keyboard)


@dp.callback_query_handler(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer('Вы успешно приобрели продукт!')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)