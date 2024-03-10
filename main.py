from config import TOKEN
from aiogram import Bot, Dispatcher, types
import logging
import asyncio
from aiogram import F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode
from keyboards import start_keyboard

dp = Dispatcher()
bot = Bot(TOKEN, parse_mode = ParseMode.HTML)

class Registration(StatesGroup):
    age = State()
    name = State()
    weight = State()
    clear = State()

@dp.message(F.text == "/start")
async def start_bot(message: types.Message):
    await message.answer(f"Приетствую в боте, {message.from_user.full_name}", reply_markup=start_keyboard)

@dp.message(F.text == "Регистрация")
async def registration_bot(message: types.Message, state: FSMContext):
    await message.answer("Сколько Вам полных лет?")
    await state.set_state(Registration.age)

@dp.message(Registration.age)
async def registration_age(message: types.Message, state: FSMContext):
    await state.update_data(age = message.text)
    await message.answer("Введите Ваше имя")
    await state.set_state(Registration.name)

@dp.message(Registration.name)
async def registration_name(message: types.Message, state: FSMContext):
    await state.update_data(name = message.text)
    await message.answer("Введите Ваш вес")
    await state.set_state(Registration.weight)

@dp.message(Registration.weight)
async def registration_weight(message: types.Message, state: FSMContext):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    await message.answer(f"Регистрация окончена успешно.\nВаши данные:\nИмя: {data['name']}\nВес: {data['weight']}\nВозраст: {data['age']}")
    await state.set_state(Registration.clear)


@dp.message(F.text == "Получить данные")
async def get_data_reg(message: types.Message, state: FSMContext):
    data = await state.get_data()
    try:
        await message.answer(f"Ваши данные:\nИмя: {data['name']}\nВес: {data['weight']}\nВозраст: {data['age']}")
    except:
        await message.answer("Вы не прошли регистрацию")

@dp.message(F.text == "Послать Рустама нахуй")
async def fuck_u_rustam(message: types.Message):
    await bot.send_message(chat_id=1460449883, text="Рустам, иди нахуй")
    await message.answer("Рустам был послан нахуй успешно")

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())