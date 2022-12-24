from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
import random
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("прив)")
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    answer = "список возможных команд:\n" + "/help - выводит это сообщение\n" + "/rnd - возвращает случайное число от 0 до 133722869\n" + "/gcd a b - возвращает наибольший общий делитель чисел a и b\n" + "/getdiv a - возвращает делители числа а\n"
    await message.answer(answer)
@dp.message_handler(commands=['rnd'])
async def gen_random_number(msg: types.Message):
    numb = random.random()
    numb *= 133722869
    answer = str(round(numb))
    await msg.answer(answer) 
def gcd(a,b):
    while(b):
        a%=b
        a,b=b,a
    return a
@dp.message_handler(commands=['gcd']) 
async def get_gcd(msg: types.Message):
    arr = msg.text.split(' ')
    gg = gcd(int(arr[1]), int(arr[2]))
    answer= str(gg)
    await msg.answer(answer)

@dp.message_handler(commands=['getdiv']) 
async def get_divisors(msg: types.Message):
    arr = msg.text.split(' ')
    numb = int(arr[1])
    divisors = []
    answer = ""
    for i in range(1,numb+1):
        if(i*i > numb):
            break
        if(numb % i ==0):
            divisors.append(i)
            if(i*i!=numb):
                divisors.append(numb//i)
    divisors =sorted(divisors)
    answer= str(divisors)
    await msg.answer(answer)    
@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
if __name__ == '__main__':
    executor.start_polling(dp)    
