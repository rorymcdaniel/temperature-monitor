import os

import MySQLdb
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

class TemperatureDB:


    def __init__(self):
        self.conn = MySQLdb.connect(passwd=os.environ.get("MYSQL_PASS"), user=os.environ.get("MYSQL_USER"),
                               db=os.environ.get("MYSQL_DBNAME"), host=os.environ.get("MYSQL_HOST"))

        self.cursor = self.conn.cursor()

    def insert_data(self, location, temperature):
        try:
            self.cursor.execute("""INSERT INTO observations (location, temperature )VALUES (%s,%s)""", (location, temperature))
            self.conn.commit()
        except Exception:
            self.conn.rollback()


    def close(self):
        self.conn.close()