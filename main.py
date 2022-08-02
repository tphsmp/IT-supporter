from aiogram import Bot, Dispatcher, executor, types
from config import *
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


# Обработка команды /access"""
# @dp.message_handler(commands=[Commands.access.value])
# async def command_access(message: types.Message, keyboard=None):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     for i in range(len(ACCESS_BUTTONS)):
#         button_i = types.KeyboardButton(text=ACCESS_BUTTONS[i])
#         keyboard.add(button_i)
#     await message.answer("Выберите действие", reply_markup=keyboard)
#

# Обработка команды /access
@dp.message_handler(commands=[Commands.access.value])
async def handle_command_access(message: types.Message, keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)):
    ButtonsGenerator.make_buttons(TextsRu.get_access_buttons(), keyboard)
    await message.answer("Выберите действие", reply_markup=keyboard)


# Обработка команды /software
@dp.message_handler(commands=[Commands.soft.value])
async def handle_command_software(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Установить/обновить ПО")
    keyboard.add(button_1)
    button_2 = types.KeyboardButton(text="Проблемы с работой ПО")
    keyboard.add(button_2)

    await message.answer("Выберите действие", reply_markup=keyboard)


# Обработка команды /ecp
@dp.message_handler(commands=[Commands.ecp.value])
async def handle_command_ecp(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Получить/продлить ЭЦП")
    keyboard.add(button_1)
    button_2 = types.KeyboardButton(text="Вход на портал по ЭЦП")
    keyboard.add(button_2)
    button_3 = types.KeyboardButton(text="Проблемы с авторизацией по ЭЦП")
    keyboard.add(button_3)
    await message.answer("Выберите действие", reply_markup=keyboard)


# Обработка команды /equipment
@dp.message_handler(commands=[Commands.equip.value])
async def handle_command_equipment(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Установка принтера/сканера/камеры и т.д.")
    keyboard.add(button_1)
    button_2 = types.KeyboardButton(text="Подключение перефирийного оборудования")
    keyboard.add(button_2)
    button_3 = types.KeyboardButton(text="Проблемы с работой принтера/сканера")
    keyboard.add(button_3)
    button_4 = types.KeyboardButton(text="Прочие внешние устройства")
    keyboard.add(button_4)
    await message.answer("Выберите действие", reply_markup=keyboard)


# Обработка команды /sap
@dp.message_handler(commands=[Commands.sap.value])
async def handle_command_sap(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Сохранение/распечатка документов")
    keyboard.add(button_1)
    button_2 = types.KeyboardButton(text="Работа с программой")
    keyboard.add(button_2)
    button_3 = types.KeyboardButton(text="Другие вопросы")
    keyboard.add(button_3)
    await message.answer("Выберите действие", reply_markup=keyboard)


# Обработка команды /1C
@dp.message_handler(commands=[Commands.ones.value])
async def handle_command_1c(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Сохранение/распечатка документов")
    keyboard.add(button_1)
    button_2 = types.KeyboardButton(text="Работа с программой")
    keyboard.add(button_2)
    button_3 = types.KeyboardButton(text="Другие вопросы")
    keyboard.add(button_3)
    await message.answer("Выберите действие", reply_markup=keyboard)


# Обработка команды /network
@dp.message_handler(commands=[Commands.net.value])
async def handle_command_network(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Доступ в интернет")
    keyboard.add(button_1)
    button_2 = types.KeyboardButton(text="Подключение к ЛВС/Интернет")
    keyboard.add(button_2)
    button_3 = types.KeyboardButton(text="Проблемы с локальной сетью")
    keyboard.add(button_3)
    button_4 = types.KeyboardButton(text="Проблемы с работой телефона")
    keyboard.add(button_4)
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
