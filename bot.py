import config
import logging
from aiogram import Bot, Dispatcher, executor, types

# log
logging.basicConfig(level=logging.INFO)

# init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

#echo
@dp.message_handler(commands=['start'])
async def echo(message):
    await message.answer('Привет, меня зовут Слеш, я твой бот помощник🤗 \nВведи команду /help и получишь весь список команд😏')


@dp.message_handler(commands=['help'])
async def echo(message):
    await message.answer('Вот список команд😉: \n/give_name - узнать создателя бота')


@dp.message_handler(commands=['give_name'])
async def echo(message):
    await message.answer('Меня создал Сулумбек \nего тг никнейм @Nk_sulumbek')
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)