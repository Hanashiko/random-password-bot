from aiogram import types, Dispatcher
from create_bot import dp, bot

import random
from string import punctuation, ascii_letters, digits

async def command_start(message: types.Message):
	await message.reply("Привіт! Моя основна команда: /password <length of password>")

async def command_password(message: types.Message):
	arg = message.get_args()
	default_password_length = 12
	if not arg:
		password_length = default_password_length
	else:
		password_length = int(arg)

	symbols = ascii_letters + digits + punctuation

	secure_random = random.SystemRandom()
	for i in range(15):
		password = "".join(secure_random.choice(symbols) for i in range(password_length))

		await message.reply(password)


def register_handlers_general(dp: Dispatcher):
	dp.register_message_handler(command_start, commands=['start'])
	dp.register_message_handler(command_password, commands=['password','p'])
