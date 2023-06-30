"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2

#  открываем файл и достаем информацию
with open('./north_data/employees_data.csv') as f:
    list_from_employees_data = []
    data = csv.reader(f, delimiter=",")
    for line in data:
        change_list_to_tuple = tuple(line)
        list_from_employees_data.append(change_list_to_tuple)

with open('./north_data/customers_data.csv') as f:
    list_from_customers_data = []
    data = csv.reader(f, delimiter=",")
    for line in data:
        change_list_to_tuple = tuple(line)
        list_from_customers_data.append(change_list_to_tuple)

with open('./north_data/orders_data.csv') as f:
    list_from_orders_data = []
    data = csv.reader(f, delimiter=",")
    for line in data:
        change_list_to_tuple = tuple(line)
        list_from_orders_data.append(change_list_to_tuple)

# подключаемся к базе данных
conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='1005')
cur = conn.cursor()  # Включение курсора
cur.executemany('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', list_from_employees_data[1:])
cur.executemany('INSERT INTO customers VALUES (%s, %s, %s)', list_from_customers_data[1:])
cur.executemany('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', list_from_orders_data[1:])
conn.commit()  # коммитим изменения

cur.close()  # закрываем курсор
conn.close()  # закрываем подключение к БД
