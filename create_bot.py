from aiogram import Bot
from aiogram.dispatcher import Dispatcher

import os
from config_bot import TOKEN_API

bot: Bot = Bot(token=TOKEN_API)
dp: Dispatcher = Dispatcher(bot)