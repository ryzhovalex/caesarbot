from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, Text, Boolean, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


Base = declarative_base()
engine = create_engine("postgresql://alex:623649@localhost/caesarbot")
session = sessionmaker(bind=engine)()


def init_db():
	Base.metadata.create_all(engine)


class Note(Base):
	__tablename__ = "note"

	id = Column(Integer, primary_key=True)
	content = Column(Text, nullable=False)
	created_datetime = Column(DateTime, nullable=False)

	def __repr__(self):
		return f"Note: id={self.id} | created: {self.created_datetime} | text: {self.text}"