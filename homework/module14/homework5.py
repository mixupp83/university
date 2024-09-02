from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import crud_functions5

api = "7249341772:AAHHFBW3zLzr2Aco1eN1fu9Y-C4hJ_1ZaWY"  # Замените на ваш API-токен
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Создание клавиатур
main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.add(KeyboardButton('Рассчитать'))
main_keyboard.add(KeyboardButton('Информация'))
main_keyboard.add(KeyboardButton('Купить'))
main_keyboard.add(KeyboardButton('Регистрация'))

buy_inline_keyboard = InlineKeyboardMarkup()
buy_inline_keyboard.add(InlineKeyboardButton('Product1', callback_data='product_buying'))
buy_inline_keyboard.add(InlineKeyboardButton('Product2', callback_data='product_buying'))
buy_inline_keyboard.add(InlineKeyboardButton('Product3', callback_data='product_buying'))
buy_inline_keyboard.add(InlineKeyboardButton('Product4', callback_data='product_buying'))

# Инициализация базы данных
crud_functions5.initiate_db()


# Класс состояний для регистрации
class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


# Обработчики и функции
@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=main_keyboard)


@dp.message_handler(lambda message: message.text == 'Купить')
async def get_buying_list(message: types.Message):
    products = crud_functions5.get_all_products()

    for product in products:
        if len(product) < 5:
            await message.answer(f"Ошибка: Неполные данные для продукта {product[1]}")
            continue

        title, description, price, image_url = product[1], product[2], product[3], product[4]

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


@dp.message_handler(lambda message: message.text == 'Регистрация')
async def sign_up(message: types.Message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if crud_functions5.is_included(username):
        await message.answer('Пользователь существует, введите другое имя:')
    else:
        await state.update_data(username=username)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    user_data = await state.get_data()
    crud_functions5.add_user(user_data['username'], user_data['email'], user_data['age'])
    await message.answer('Регистрация завершена!')
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)