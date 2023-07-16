from aiogram import Bot, Dispatcher
from config import TOKEN

import functions
from data import my_dict
from classes import *

# полученный у @BotFather
BOT_TOKEN: str = TOKEN


# Создаем объекты бота и диспетчера
bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()









if __name__ == '__main__':
    dp.run_polling(bot)