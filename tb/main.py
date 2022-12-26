from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '5807819960:AAFAlZRLq5_8xKJuZ1vRqOOz3GqwM7bIt4U'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def greeting(message):
    await message.reply('Привет!\n',
    'Я бот, который поможет тебе с простыми арифметическими действиями!\n',
    'Ты можешь запросить результат суммы, разности, умножения, деления и даже факториал!\n',
    'К сожалению, пока я могу проводить операции с <2  числами, но обещаю исправиться!\n',
    'И еще! Краткая сводка как пользоваться ботом:\n',
    'Сумма "+"\n',
    'Разность "-"\n',
    'Умножение "*"\n',
    'Деление ":"\n',
    'Факториал "!"\n')
def sum(a, b):
    return a+b
def diff(a, b):
    return a - b
def multi(a, b):
    return a*b
def div(a, b):
    return a / b
def fact(a):
    ans = 1
    for i in range(1, a+1):
        ans *= i
    return ans
@dp.message_handler()
async def answer(message):
    a = message[0]
    b = message[2]
    if '+' in message:
        print(f'Получилось {sum(a, b)}')
    elif '-' in message:
        print(f'Получилось {diff(a, b)}')
    elif '*' in message:
        print(f'Получилось {multi(a, b)}')
    elif '*' in message:
        print(f'Получилось {multi(a, b)}')
    elif ':' in message:
        print(f'Получилось {div(a, b)}')
    elif '!' in message:
        print(f'Получилось {fact(a)}')
    else:
        print('Ты ввел что-то не то, попробуй еще раз!')