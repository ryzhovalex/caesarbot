""" Работа с расходами — их добавление, удаление, статистики"""
import datetime
import re
from typing import List, NamedTuple, Optional

import pytz

from . import db


def add_note(message: str) -> None:
	db.insert("note", {
		"date_created": parsed_message.amount,
		"date_created": _get_now_formatted(),
		"category_codename": category.codename,
		"raw_text": raw_message
	})


def get_today_statistics() -> str:
	"""Возвращает строкой статистику расходов за сегодня"""
	cursor = db.get_cursor()
	cursor.execute("select sum(amount)"
				   "from expense where date(created)=date('now', 'localtime')")
	result = cursor.fetchone()
	if not result[0]:
		return "Сегодня ещё нет расходов"
	all_today_expenses = result[0]
	cursor.execute("select sum(amount) "
				   "from expense where date(created)=date('now', 'localtime') "
				   "and category_codename in (select codename "
				   "from category where is_base_expense=true)")
	result = cursor.fetchone()
	base_today_expenses = result[0] if result[0] else 0
	return (f"Расходы сегодня:\n"
			f"всего — {all_today_expenses} руб.\n"
			f"базовые — {base_today_expenses} руб. из {_get_budget_limit()} руб.\n\n"
			f"За текущий месяц: /month")


def _get_now_formatted() -> str:
	""" Return date as string """
	return _get_now_datetime().strftime("%Y-%m-%d %H:%M:%S")


def _get_now_datetime() -> datetime.datetime:
	""" Return datetime for certain timezone """
	tz = pytz.timezone("Europe/Saratov")
	now = datetime.datetime.now(tz)
	return now



