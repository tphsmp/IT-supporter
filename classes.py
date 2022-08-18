from enum import Enum
from aiogram import types


class TextsRu:
    # сообщение выходит при отправке боту команды /start
    PRE_ACTION_MESSAGE = 'Выберите действие'

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

    @staticmethod
    def get_preaction_message(pre_action_message=PRE_ACTION_MESSAGE):
        return pre_action_message

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


class ButtonsGenerator:
    # содержание кнопок для команды /access
    access_button_text = 'Восстановить доступ к ИС (Origami, SAP, 1C  т.д)'
    access_button_text2 = 'Создать/разблокировать учетную запись пользователя'
    access_button_text3 = 'Доступ к сетевым ресурсам, удаленный доступ'
    access_button_text4 = 'Доступ к файлам и электронной почте сотрудника'
    # список кнопок для команды /access
    ACCESS_BUTTONS = (access_button_text, access_button_text2, access_button_text3, access_button_text4)

    # содержание кнопок для команды /software
    software_button_text = 'Обновить/установить ПО'
    software_button_text2 = 'Проблемы с работой ПО'
    # список кнопок для команды /access
    SOFTWARE_BUTTONS = (software_button_text, software_button_text2)

    # содержание кнопок для команды /ecp
    ecp_button_text = 'Получить/продлить ЭЦП'
    ecp_button_text2 = 'Вход на портал по ЭЦП'
    ecp_button_text3 = 'Проблемы с авторизацией по ЭЦП'
    # список кнопок для команды /access
    ECP_BUTTONS = (ecp_button_text, ecp_button_text2, ecp_button_text3)

    # содержание кнопок для команды /equipment
    equipment_button_text = 'Установка принтера/сканера/камеры и т.д.'
    equipment_button_text2 = 'Подключение ПК и перефирийного оборудования'
    equipment_button_text3 = 'Проблемы с работой принтера/сканера'
    equipment_button_text4 = 'Прочие внешние устройства'
    # список кнопок для команды /equipment
    EQUIPMENT_BUTTONS = (equipment_button_text, equipment_button_text2, equipment_button_text3, equipment_button_text4)

    # содержание кнопок для команды /sap
    sap_button_text = 'Сохранение/распечатка документов'
    sap_button_text2 = 'Работа с программой'
    sap_button_text3 = 'Другие вопросы'
    # список кнопок для команды /sap
    SAP_BUTTONS = (sap_button_text, sap_button_text2, sap_button_text3)

    # содержание кнопок для команды /1C
    ones_button_text = 'Сохранение/распечатка документов'
    ones_button_text2 = 'Работа с программой'
    ones_button_text3 = 'Другие вопросы'
    # список кнопок для команды /1C
    ONES_BUTTONS = (ones_button_text, ones_button_text2, ones_button_text3)

    # содержание кнопок для команды /network
    network_button_text = 'Доступ в интернет'
    network_button_text2 = 'Подключение к ЛВС/Интернет'
    network_button_text3 = 'Проблемы с локальной сетью'
    network_button_text4 = 'Проблемы с работой телефона'
    # список кнопок для команды /network
    NETWORK_BUTTONS = (network_button_text, network_button_text2, network_button_text3, network_button_text4)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    @classmethod
    def make_buttons(cls, buttons_list, keyboard=keyboard):
        for i in range(len(buttons_list)):
            button_i = types.KeyboardButton(text=buttons_list[i])
            keyboard.add(button_i)