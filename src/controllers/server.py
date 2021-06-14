""" Server controller which is responsible of all bot actions """

import logging
import os

from aiogram import Bot, Dispatcher, executor, types

from ..models.middlewares import AccessMiddleware
from ..models import notebook, orm


NOTE_OPERATOR = "*" # operator used to recognize notes

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
ACCESS_ID = os.getenv("TELEGRAM_ACCESS_ID")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(AccessMiddleware(ACCESS_ID))


def run():
	executor.start_polling(dp, skip_updates=True)


def init_db():
	orm.init_db()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
	""" Send welcome message """
	await message.answer("WELCOME BUDDY!")


@dp.message_handler()
async def handle_message(message: types.Message):
	""" Handle message with delegating further operations to appropriate instance """
	if message.text[0] == NOTE_OPERATOR:
		await add_note(message)
	else:
		await message.answer("Not recognized command!")


async def add_note(message: types.Message):
	""" Add new note """
	notebook.add_note(message)
	await message.answer("Note added.")


