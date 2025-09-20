import sqlite3

def create_table_order():
    connection = sqlite3.connect('orders.db')
    cursor = connection.cursor()
    (cursor.execute
        ("""create table if not exists orders 
        (id integer primary key  autoincrement ,
     product_name text,
     order_datetime datetime,
     status text,
     deliver_datetime datetime,)"""))
    connection.commit()
    connection.close()

def save_order(product_name, order_datetime, status, deliver_datetime):
    connection = sqlite3.connect('orders.db')
    cursor = connection.cursor()
    cursor.execute("""insert into orders (product_name, order_datetime, status, deliver_datetime) values (?,?,?,?), 
                   [product_name, order_datetime,  status, delivery_datetime ]""")
    connection.commit()
    connection.close()

def find_rejected_orders():
    connection = sqlite3.connect('rejected_orders.db')
    cursor = connection.cursor()
    cursor.execute("""select product_name, order_datetime from orders
     where status="rejected" or deliver_datetime is null""")
    rejected_orders = cursor.fetchall()
    connection.close()
    return rejected_orders

def find_sent_orders():
    connection = sqlite3.connect('rejected_orders.db')
    cursor = connection.cursor()
    cursor.execute("""select product_name, order_datetime from orders
     where status="send""""")
    sent_orders = cursor.fetchall()
    connection.close()
    return sent_orders