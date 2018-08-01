import psycopg2
import sys
import config


def create_table():
    conn=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, email TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS entries (user_id INTEGER, entry TEXT, date TEXT)")
    conn.commit()
    conn.close()

def insert(username,email,password):
    db_connection=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
    db_cursor = db_connection.cursor()
    db_cursor.execute("INSERT INTO users VALUES('%s','%s','%s')", (username,email,password))
    db_cursor.execute("INSERT INTO users VALUES(%s,%s,%s)", (username,email, password))
    db_connection.commit()
    db_connection.close()

create_table()
insert(1111,222222,3333)

if __name__ == '__main__':
    main()
