import os
from PgEngine import *
from _data_config import *

# Create temp db with mockup data for test
execute(""" SELECT pg_terminate_backend(pg_stat_activity.pid)
            FROM pg_stat_activity
            WHERE pg_stat_activity.datname = 'temp';""")
execute("""DROP DATABASE IF EXISTS temp;""");
execute("""CREATE DATABASE temp;""");
setting['database']='temp'


with open('{}/CreateSqlTable.sql'.format(os.path.dirname(__file__)),'r',encoding='utf-8') as create_table_sql:
    execute(create_table_sql.read())


# Get access id
access_info = check_access('Andy@email.com','Andy')
access_id = access_info['id']
print(access_id) 


# return_value: [{'name':'apple','carb':70,'protein':10,'fat':0.5}, ...]
food_list = get_food_list()
print(food_list)

# Get person
person = get_person(access_id)
print(person)

meal_of_person = get_account_all_meals(access_id)
print(meal_of_person)


events= get_events()
print(events)

