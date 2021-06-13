""" Server controller which is responsible of all bot actions """

import logging
import os

from aiogram import Bot, Dispatcher, executor, types

from ..services.middlewares import AccessMiddleware


API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
ACCESS_ID = os.getenv("TELEGRAM_ACCESS_ID")

NOTE_OPERATOR = "&" # operator used to recognize notes

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(AccessMiddleware(ACCESS_ID))


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """ Send welcome message """
    await message.answer("WELCOME BUDDY!")


@dp.message_handler()
async def handle_message(message: types.Message):
    """ Handle message with delegating further operations to appropriate instance """
    if message[0] == NOTE_OPERATOR:
        add_note(message)


async def add_note(message: types.Message):
    """ Add new note """
    await message.answer("Note added.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
