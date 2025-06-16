import pymysql

connection = pymysql.connect(
    host = "127.0.0.1",
    user = "root",
    password = "password",
    db = "classicmodels",
    charset = "utf8mb4",
    cursorclass = pymysql.cursors.DictCursor
)

# cursor = connection.cursor()

# sql = "SELECT * FROM customers"
# cursor.execute(sql)

# customers = cursor.fetchone()
# print(customers)
# print(customers["customerNumber"])
# print(customers["customerName"])
# print(customers["country"])

# def add_customer():
#     cursor = connection.cursor()
#     name = "kimkim"
#     family_name = "Kim"
#     sql = f'INSERT INTO customers(customerNumber, customerName, contactLastName) VALUES({10000}, "{name}", "{family_name}")'
#     cursor.execute(sql)
#     connection.commit()

# add_customer()

# def update_customer():
#     cursor = connection.cursor()
#     update_name = "update_kimkim"
#     contactLastName = "update_Kim"
#     sql = f'UPDATE customers SET customerName = "{update_name}", contactLastName = "{contactLastName}" WHERE customerNumber = 10000'
#     cursor.execute(sql)
#     connection.commit()
#     cursor.close()

# update_customer()

def delete_customer():
    cursor = connection.cursor()
    sql = "DELETE FROM customers WHERE customerNumber = 10000"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

delete_customer()