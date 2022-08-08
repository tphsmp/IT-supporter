from config import TOKEN
from aiogram import Bot, Dispatcher, executor
from classes import *

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# Обработка команды /start
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, TextsRu.get_start_message(message.from_user))


# Вывод списка команд по группам
@dp.message_handler(commands=['about'])
async def bot_message(message: types.Message):
    await bot.send_message(message.from_user.id, TextsRu.get_about_message())


# Обработка команды /access
@dp.message_handler(commands=[Commands.access.value])
async def handle_command_access(message: types.Message, keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)):
    ButtonsGenerator.make_buttons(ButtonsGenerator.ACCESS_BUTTONS, keyboard)
    await message.answer("Выберите действие", reply_markup=keyboard)


# Обработка команды /software
@dp.message_handler(commands=[Commands.soft.value])
async def handle_command_software(message: types.Message, keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)):
    ButtonsGenerator.make_buttons(ButtonsGenerator.SOFTWARE_BUTTONS, keyboard)
    await message.answer("Выберите действие", reply_markup=keyboard)


# Обработка команды /ecp
@dp.message_handler(commands=[Commands.ecp.value])
async def handle_command_software(message: types.Message, keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)):
    ButtonsGenerator.make_buttons(ButtonsGenerator.ECP_BUTTONS, keyboard)
    await message.answer("Выберите действие", reply_markup=keyboard)


# Обработка команды /equipment
@dp.message_handler(commands=[Commands.equip.value])
async def handle_command_software(message: types.Message, keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)):
    ButtonsGenerator.make_buttons(ButtonsGenerator.EQUIPMENT_BUTTONS, keyboard)
    await message.answer("Выберите действие", reply_markup=keyboard)


# Обработка команды /sap
@dp.message_handler(commands=[Commands.sap.value])
async def handle_command_software(message: types.Message, keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)):
    ButtonsGenerator.make_buttons(ButtonsGenerator.SAP_BUTTONS, keyboard)
    await message.answer("Выберите действие", reply_markup=keyboard)


# Обработка команды /1C
@dp.message_handler(commands=[Commands.ones.value])
async def handle_command_software(message: types.Message, keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)):
    ButtonsGenerator.make_buttons(ButtonsGenerator.ONES_BUTTONS, keyboard)
    await message.answer("Выберите действие", reply_markup=keyboard)


# Обработка команды /network
@dp.message_handler(commands=[Commands.net.value])
async def handle_command_software(message: types.Message, keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)):
    ButtonsGenerator.make_buttons(ButtonsGenerator.NETWORK_BUTTONS, keyboard)
    await message.answer("Выберите действие", reply_markup=keyboard)


# Обработка команды /another
@dp.message_handler(commands=[Commands.other.value])
async def handle_command_another(message: types.Message):
    await message.answer("Свяжитесь с специалистом сектора поддержки по номеру 5555")


# Обработка кнопок раздела sap
@dp.message_handler(lambda message: message.text == "Работа с программой" or message.text == "Другие вопросы")
async def handle_buttons_sap(message: types.Message):
    await message.answer("Свяжитесь со специалистом сектора безнес-приложений по номеру 2124 или 2156")


# Обработка прочих кнопок
@dp.message_handler(lambda message: message.text != "Работа с программой" or message.text != "Другие вопросы")
async def handle_other_buttons(message: types.Message):
    await message.answer("Свяжитесь со специалистом сектора поддержки по номеру 5555")


# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
