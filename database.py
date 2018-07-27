import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()
    
    # if rows[1][1] == 1:
    #     return "user exists"
    # return "user does not exist"

def insert(item,quantity,price):
    db_connection=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
    db_cursor = db_connection.cursor()
    # db_cursor.execute("INSERT INTO store VALUES('%s','%s','%s')", (item,quantity,price))
    db_cursor.execute("INSERT INTO store VALUES(%s,%s,%s)", (item,quantity,price))
    db_connection.commit()
    db_connection.close()

def update(item, quantity, price):
    db_connection = psycopg2.connect("dbname='database' user='postgres' password='1Lomkones.' host='localhost'")
    db_cursor = db_connection.cursor()
    db_cursor.execute("UPDATE store SET price=%s, quantity=%s WHERE item=%s", (price, quantity, item))
    db_connection.commit()
    db_connection.close()



create_table()
insert("Orange",10,15)
# delete("wine glass"))
# print(view())
# insert("coffee cup",10,5)