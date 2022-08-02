TOKEN = ""


# сообщение выходит при отправке боту команды /start
GREETING_MESSAGE = "Здравствуйте {0.first_name} {0.last_name}! Нажмите на кнопку меню и выберите /about \n " \
                   "Если среди предложенных вариантов нет пункта по вашему вопросу свяжитесь со службой поддержки \n"

# сообщение выходит при отправке боту команды /about
ABOUT_MESSAGE = "Выберите соответствующий вашему вопросу пункт из списка ниже: \n\n /access - доступ к " \
                   "информационным системам и ресурсам компании \n\n /software - установка, обновление программного " \
                   "обеспечения\n\n /ecp - получение обновление ЭЦП, доступ на порталы egov, ЭСФ и прочие порталы с " \
                   "авторизацией по ЭЦП \n\n /equipment - установка перефирийного оборудования (принтеры. сканеры, " \
                   "камеры и т.д.) \n\n /sap - вопросы по SAP \n\n /1C - вопрос по 1С\n\n /network - локальная " \
                   "сеть, телефония, доступ в интернет \n\n /another - другой вопрос \n\n"

# список кнопок для команды /access
ACCESS_BUTTONS = ('Восстановить доступ к ИС (Origami, SAP, 1C  т.д)',
                  'Создать/разблокировать учетную запись пользователя',
                  'Доступ к сетевым ресурсам, удаленный доступ',
                  'Доступ к файлам и электронной почте сотрудника')

# список кнопок для команды /software
SOFTWARE_BUTTONS = ('',)

# список кнопок для команды /ecp
ECP_BUTTONS = ('',)

# список кнопок для команды /equipment
EQUIPMENT_BUTTONS = ('',)

# список кнопок для команды /sap
SAP_BUTTONS = ('',)

# список кнопок для команды /1C
ONEC_BUTTONS = ('',)

# список кнопок для команды /network
NETWORK_BUTTONS = ('',)
