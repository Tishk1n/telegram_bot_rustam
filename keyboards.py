from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_buttons = [
    [KeyboardButton(text="Регистрация")],
    [KeyboardButton(text="Получить данные"),
    KeyboardButton(text="Послать Рустама нахуй")]
]

start_keyboard = ReplyKeyboardMarkup(keyboard=start_buttons, resize_keyboard=True)
