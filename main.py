from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '5875122334:AAEBCNpI1PP7Aw5QLCpAqgPLGGr4mGY--os'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def greeting(message: types.Message):
    await message.answer('Привет!\nЯ бот, который поможет тебе с простыми арифметическими действиями!\nТы можешь запросить результат суммы, разности, умножения, деления и даже факториал!\nК сожалению, пока я могу проводить операции с <= 2  числами, но обещаю исправиться!\nИ еще! Если хочешь использовать нецелые числа, используй "." вместо ",".\nПравильный ввод:\n37.6 : 2')
def calculator(string):
    if '+' in string:
        a = string.index('+')
        s1 = string[:a]
        s1 = float(s1)
        s2 = string[a+1:]
        s2 = float(s2)
        b = s1+s2
        b = str(b)
        if b[-2] + b[-1] == '.0':
            c = b.index('.')
            return b[:c]
        else:
            return b
    elif '-' in string:
        a1 = string.index('-')
        d1 = string[:a1]
        d1 = float(d1)
        d2 = string[a1+1:]
        d2 = float(d2)
        b1 = d1-d2
        b1 = str(b1)
        if b1[-2] + b1[-1] == '.0':
            c1 = b1.index('.')
            return b1[:c1]
        else:
            return b1
    elif '*' in string:
        a2 = string.index('*')
        m1 = string[:a2]
        m1 = float(m1)
        m2 = string[a2+1:]
        m2 = float(m2)
        b2 = m1*m2
        b2 = str(b2)
        if b2[-2] + b2[-1] == '.0':
            c = b2.index('.')
            return b2[:c]
        else:
            return b2
        return m1*m2
    elif ':'  in string:
        a3 = string.index(':')
        de1 = string[:a3]
        de1 = float(de1)
        de2 = string[a3+1:]
        de2 = float(de2)
        if de2 != 0:
            b3 = de1 / de2
            b3 = str(b3)
            if b3[-2] + b3[-1] == '.0':
                c = b3.index('.')
                return b3[:c]
            else:
                return b3
        else:
            return 'На 0 делить нельзя!'
    elif '/'  in string:
        a3 = string.index('/')
        de1 = string[:a3]
        de1 = float(de1)
        de2 = string[a3+1:]
        de2 = float(de2)
        if de2 != 0:
            b3 = de1 / de2
            b3 = str(b3)
            if b3[-2] + b3[-1] == '.0':
                c = b3.index('.')
                return b3[:c]
            else:
                return b3
        else:
            return 'На 0 делить нельзя!'
    elif '!' in string:
        a4 = string.index('!')
        f = string[:a4]
        f = int(f)
        ans = 1
        for i in range(1, f+1):
            ans *= i
        return ans
@dp.message_handler()
async def answer(message: types.Message):
    await message.answer(calculator(message.text))
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)