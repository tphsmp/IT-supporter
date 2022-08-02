from config import *
from enum import Enum
from aiogram import Bot, Dispatcher, executor, types


class TextRu:

    def get_start_message(self):
        start_message = GREETING_MESSAGE
        return start_message

    def get_about_message(self):
        about = ABOUT_MESSAGE
        return about


class Commands(Enum):
    access = 'access'
    soft = 'software'
    ecp = 'ecp'
    equip = 'equipment'
    sap = 'sap'
    ones = '1C'
    net = 'network'
    other = 'another'


class ButtonsGenerator:

    def make_buttons(actions_list):
        for i in range(len(actions_list)):
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button_i = types.KeyboardButton(text=actions_list[i])
            keyboard.add(button_i)
            return keyboard

