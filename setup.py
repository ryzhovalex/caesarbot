""" CaesarBot """

__author__ = "Alexander Ryzhov"
__email__ = "thed4rkof.gmail.com"
__version__ = "0.2.0-proto.2"


""" Alembic:
$ alembic init alembic
set path to database at 'alembic.ini'
$ alembic revision -m "my revision name"
$ alembic upgrade head
"""

import sys
from src.controllers import server


if __name__ == "__main__":
	if len(sys.argv) == 1: # means without any additional parameters 
		server.run()
	elif sys.argv[1] == "init":
		print("Initializing the database...")
		server.init_db()
		print("...initialized!")