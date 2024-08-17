from aiogram import Dispatcher
from aiogram.types import ChatMember, User
from aiogram.bot import Bot
from aiogram.utils.executor import start_polling
from create_bot import dp, bot

async def on_startup(_) -> None:
	me: User = await bot.get_me()
	UserInfo: ChatMember = await bot.get_chat_member(me.id, me.id)
	username: str = f"@{UserInfo.user.username}"

	text: str = f"Бот запущений | {username} - {me.first_name}"
	print(text)

from handlers import general

def register_handlers(dp):
	general.register_handlers_general(dp)

def main() -> None:
	register_handlers(dp)
	start_polling(dp, skip_updates=False, on_startup=on_startup)

if __name__ == "__main__":
	main()