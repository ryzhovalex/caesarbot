""" Работа с расходами — их добавление, удаление, статистики"""
import datetime
import re
from typing import List, NamedTuple, Optional

import pytz

from . import orm


def add_note(message: str) -> None:
	note = orm.Note(content=message.text[1::], created_datetime=_get_now_datetime())
	orm.session.add(note)
	orm.session.commit()


def _get_now_datetime() -> datetime.datetime:
	""" Return datetime for certain timezone """
	tz = pytz.timezone("Europe/Saratov")
	now = datetime.datetime.now(tz)
	return now


def _get_now_formatted() -> str:
	""" Return date as string """
	return _get_now_datetime().strftime("%Y-%m-%d %H:%M:%S")


