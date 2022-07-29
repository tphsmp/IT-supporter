from aiogram import Bot, Dispatcher, executor, types

from config import *

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

"""Обработка команды /start"""
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, GREETING_MESSAGE.format(message.from_user))

"""Вывод списка команд по группам"""
@dp.message_handler(commands=['about'])
async def bot_message(message: types.Message):
    await bot.send_message(message.from_user.id, "Выберите соответствующий вашему вопросу пункт из списка ниже: \n\n"
                                                 "/access - доступ к информационным системам и ресурсам компании \n\n"
                                                 "/software - установка, обновление программного обеспечения\n\n"
                                                 "/ecp - получение обновление ЭЦП, доступ на порталы egov, ЭСФ и "
                                                 "прочие порталы с авторизацией по ЭЦП \n\n"
                                                 "/equipment - установка перефирийного оборудования "
                                                 "(принтеры. сканеры, камеры и т.д.) \n\n"
                                                 "/sap - вопросы по SAP \n\n"
                                                 "/1C - вопрос по 1С\n\n"
                                                 "/network - локальная сеть, телефония, доступ в интернет \n\n"
                                                 "/another - другой вопрос \n\n")

"""Обработка команды /access"""
@dp.message_handler(commands=['access'])
async def command_access(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Восстановить доступ к ИС (Origami, SAP, 1C  т.д)")
    keyboard.add(button_1)
    button_2 = types.KeyboardButton(text="Создать/разблокировать учетную запись пользователя")
    keyboard.add(button_2)
    button_3 = types.KeyboardButton(text="Доступ к сетевым ресурсам, удаленный доступ")
    keyboard.add(button_3)
    button_4 = types.KeyboardButton(text="Доступ к файлам и электронной почте сотрудника")
    keyboard.add(button_4)
    await message.answer("Выберите действие", reply_markup=keyboard)

"""Обработка команды /software"""
@dp.message_handler(commands=['software'])
async def command_access(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Установить/обновить ПО")
    keyboard.add(button_1)
    button_2 = types.KeyboardButton(text="Проблемы с работой ПО")
    keyboard.add(button_2)
    await message.answer("Выберите действие", reply_markup=keyboard)

"""Обработка команды /ecp"""
@dp.message_handler(commands=['ecp'])
async def command_access(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Получить/продлить ЭЦП")
    keyboard.add(button_1)
    button_2 = types.KeyboardButton(text="Вход на портал по ЭЦП")
    keyboard.add(button_2)
    button_3 = types.KeyboardButton(text="Проблемы с авторизацией по ЭЦП")
    keyboard.add(button_3)
    await message.answer("Выберите действие", reply_markup=keyboard)

"""Обработка команды /equipment"""
@dp.message_handler(commands=['equipment'])
async def command_access(message: types.Message):
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

"""Обработка команды /sap"""
@dp.message_handler(commands=['sap'])
async def command_access(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Сохранение/распечатка документов")
    keyboard.add(button_1)
    button_2 = types.KeyboardButton(text="Работа с программой")
    keyboard.add(button_2)
    button_3 = types.KeyboardButton(text="Другие вопросы")
    keyboard.add(button_3)
    await message.answer("Выберите действие", reply_markup=keyboard)

"""Обработка команды /1C"""
@dp.message_handler(commands=['1C'])
async def command_access(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Сохранение/распечатка документов")
    keyboard.add(button_1)
    button_2 = types.KeyboardButton(text="Работа с программой")
    keyboard.add(button_2)
    button_3 = types.KeyboardButton(text="Другие вопросы")
    keyboard.add(button_3)
    await message.answer("Выберите действие", reply_markup=keyboard)

"""Обработка команды /network"""
@dp.message_handler(commands=['network'])
async def command_access(message: types.Message):
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

"""Обработка команды /another"""
@dp.message_handler(commands=['another'])
async def access(message: types.Message):
    await message.answer("Свяжитесь с специалистом сектора поддержки по номеру 5555")


# async def origami(message: types.Message):
#     if (message.text == "ИС Оригами"):
#         await message.answer("пароль сбросить да?")
#

"""Обработка кнопок раздела sap"""
@dp.message_handler(lambda message: message.text == "Работа с программой" or message.text == "Другие вопросы")
async def sono(message: types.Message):
    await message.answer("Свяжитесь со специалистом сектора безнес-приложений по номеру 2124 или 2156")

"""Конец обработка кнопок раздела sap"""

"""Обработка кнопок раздела 1C"""
@dp.message_handler(lambda message: message.text != "Работа с программой" or message.text != "Другие вопросы")
async def sono(message: types.Message):
    await message.answer("Свяжитесь со специалистом сектора поддержки по номеру 5555")

"""Конец обработка кнопок раздела 1C"""

"""Запуск бота"""
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
