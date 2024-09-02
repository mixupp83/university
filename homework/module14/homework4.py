from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import crud_functions4

api = "7249341772:AAHHFBW3zLzr2Aco1eN1fu9Y-C4hJ_1ZaWY"  # Замените на ваш API-токен
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Создание клавиатур
main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.add(KeyboardButton('Рассчитать'))
main_keyboard.add(KeyboardButton('Информация'))
main_keyboard.add(KeyboardButton('Купить'))

buy_inline_keyboard = InlineKeyboardMarkup()
buy_inline_keyboard.add(InlineKeyboardButton('Product1', callback_data='product_buying'))
buy_inline_keyboard.add(InlineKeyboardButton('Product2', callback_data='product_buying'))
buy_inline_keyboard.add(InlineKeyboardButton('Product3', callback_data='product_buying'))
buy_inline_keyboard.add(InlineKeyboardButton('Product4', callback_data='product_buying'))

# Инициализация базы данных
crud_functions4.initiate_db()


# Обработчики и функции
@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=main_keyboard)


@dp.message_handler(lambda message: message.text == 'Купить')
async def get_buying_list(message: types.Message):
    products = crud_functions4.get_all_products()

    for product in products:
        title, description, price = product[1], product[2], product[3]
        image_url = f"https://example.com/image{product[0]}.jpg"  # Замените на реальные URL-адреса изображений

        # Проверка доступности URL
        if image_url.startswith('http') and image_url.endswith(('.jpg', '.png', '.jpeg')):
            try:
                await message.answer_photo(photo=image_url,
                                           caption=f"Название: {title} | Описание: {description} | Цена: {price}")
            except Exception as e:
                await message.answer(f"Ошибка при отправке изображения для {title}: {e}")
        else:
            await message.answer(f"Ошибка: Неверный URL изображения для {title}")

    await message.answer('Выберите продукт для покупки:', reply_markup=buy_inline_keyboard)


@dp.callback_query_handler(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer('Вы успешно приобрели продукт!')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)