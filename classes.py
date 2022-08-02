from config import *
from enum import Enum
from aiogram import types


class TextsRu:
    # содержание кнопок для команды /access
    access_button_text = 'Восстановить доступ к ИС (Origami, SAP, 1C  т.д)'
    access_button_text2 = 'Создать/разблокировать учетную запись пользователя'
    access_button_text3 = 'Доступ к сетевым ресурсам, удаленный доступ'
    access_button_text4 = 'Доступ к файлам и электронной почте сотрудника'

    # список кнопок для команды /access
    ACCESS_BUTTONS = (access_button_text, access_button_text2, access_button_text3, access_button_text4)

    # сообщение выходит при отправке боту команды /start
    GREETING_MESSAGE = "Здравствуйте {0.first_name} {0.last_name}! Нажмите на кнопку меню и выберите /about \n " \
                       "Если среди предложенных вариантов нет пункта по вашему вопросу свяжитесь со " \
                       "службой поддержки \n"

    # сообщение выходит при отправке боту команды /about
    ABOUT_MESSAGE = "Выберите соответствующий вашему вопросу пункт из списка ниже: \n\n /access - доступ к " \
                    "информационным системам и ресурсам компании \n\n /software - установка, обновление программного " \
                    "обеспечения\n\n /ecp - получение обновление ЭЦП, доступ на порталы egov, ЭСФ и прочие порталы с " \
                    "авторизацией по ЭЦП \n\n /equipment - установка перефирийного оборудования (принтеры. сканеры, " \
                    "камеры и т.д.) \n\n /sap - вопросы по SAP \n\n /1C - вопрос по 1С\n\n /network - локальная " \
                    "сеть, телефония, доступ в интернет \n\n /another - другой вопрос \n\n"
    @classmethod
    def get_access_buttons(cls, greeting_msg=ACCESS_BUTTONS):
        return greeting_msg

    @staticmethod
    def get_start_message(from_user, greeting_message=GREETING_MESSAGE):
        return greeting_message.format(from_user)

    @staticmethod
    def get_about_message(about_message=ABOUT_MESSAGE):
        return about_message


class Commands(Enum):
    access = 'access'
    soft = 'software'
    ecp = 'ecp'
    equip = 'equipment'
    sap = 'sap'
    ones = '1C'
    net = 'network'
    other = 'another'


# class ButtonsGenerator:
#
#     @classmethod
#     def make_buttons(cls, access_buttons=ACCESS_BUTTONS, keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)):
#         for i in range(len(access_buttons)):
#             button_i = types.KeyboardButton(text=access_buttons[i])
#             keyboard.add(button_i)


class ButtonsGenerator:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    @classmethod
    def make_buttons(cls, actions_list, keyboard=keyboard):
        for i in range(len(actions_list)):
            button_i = types.KeyboardButton(text=actions_list[i])
            keyboard.add(button_i)
