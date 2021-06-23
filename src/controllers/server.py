""" Server controller which is responsible of all bot actions """

import os
import logging
import click
import random

from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext
from flask_migrate import Migrate
from aiogram import Bot, Dispatcher, executor, types

from ..models.middlewares import AccessMiddleware
from ..models import notebook, orm


###########
# Aiogram #
###########
NOTE_OPERATOR = "*" # operator used to recognize notes

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
ACCESS_ID = os.getenv("TELEGRAM_ACCESS_ID")

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
	if message.text[0] == NOTE_OPERATOR:
		await add_note(message)
	else:
		await message.answer("Not recognized command!")


async def add_note(message: types.Message):
	""" Add new note """
	notebook.add_note(message)
	await message.answer("Note added.")


#########
# Flask #
#########
db = SQLAlchemy()


def create_app():
    # proper init sequence from here: https://stackoverflow.com/a/20749534/14748231
    app = Flask(__name__)

    # source: https://flask.palletsprojects.com/en/2.0.x/api/#flask.Config.from_object
    from ..models import config
    app.config.from_object(config.DevelopmentConfig())

    db.init_app(app)

    # source: https://github.com/miguelgrinberg/flask-migrate
    migrate = Migrate(app, db)
    # if first time initialization:
    # -- $ flask db init
    # after each change at models:
    # -- $ flask db migrate
    # -- $ flask db upgrade

    # app.cli.add_command(add_test_user)

    # from ..views import home
    # app.register_blueprint(home.bp)

    return app


# @click.command("add-test-user")
# @with_appcontext
# def add_test_user():
#     from .models import User
#     user = User(name=str(random.randint(-10**6, 10**6)), age=random.randint(5, 80))
#     db.session.add(user)
#     db.session.commit()
#     click.echo("New test user added.")
