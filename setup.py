import psycopg2
import sys
import config


class InitDatabase():

    def __init__(self, db):
        self.db = db
        self.db_connection = psycopg2.connect("dbname='challenge3' user='postgres' password='0725401106' host='localhost' port='5435'")
        self.db_cursor = self.db_connection.cursor()


    def tables_creation(self):
        tables = ("""CREATE TABLE IF NOT EXISTS users (user_id SERIAL PRIMARY KEY, email VARCHAR(150) NOT NULL UNIQUE,
                                                    username VARCHAR(100) NOT NULL, password VARCHAR(450) NOT NULL,
                                                    admin BOOLEAN NOT NULL)""",
                """ CREATE TABLE IF NOT EXISTS entries (entry_id SERIAL PRIMARY KEY, entry VARCHAR(155) NOT NULL,
                                                        user_id VARCHAR(50) NOT NULL, date VARCHAR(100) NOT NULL)""")
        for table in tables:
            self.db_cursor.execute(table)
            self.db_connection.commit()

    def con(self):
        return self.db_cursor

    def commit(self):
        self.db_connection.commit()

    def close(self):
        self.db_connection.commit()
        self.db_cursor.close()
        self.db_connection.close()

    def drop(self):
        try:
            self.db_cursor.execute('DROP TABLE IF EXISTS "users", "entries";')
            self.db_connection.commit()
        except psycopg2.Error:
            raise SystemExit("Failed {}".format(sys.exc_info()))

# db = InitDatabase(config.TestingConfig.db)
db = InitDatabase(config.ProductionConfig.db)
# db.tables_creation()
# db.drop()