from .model_aliases import *


class Note(model()):
	__tablename__ = "note"

	id = column(integer(), primary_key=True)
	content = column(text(), nullable=False)
	created_datetime = column(dtime(), nullable=False)

	def __repr__(self):
		return f"Note: id={self.id} | created: {self.created_datetime} | text: {self.text}"
