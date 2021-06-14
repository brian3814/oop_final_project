from PgEngine import *
import pytest


test = get_account()

execute(""" SELECT pg_terminate_backend(pg_stat_activity.pid)
            FROM pg_stat_activity
            WHERE pg_stat_activity.datname = 'temp';""")

execute("""DROP DATABASE IF EXISTS TEMP;""");

execute("""CREATE DATABASE TEMP;""");
setting['database']='temp'

'''
truncate_all_tables_in_test ="""CREATE OR REPLACE FUNCTION truncate_tables(username IN VARCHAR) RETURNS void AS $$
                                DECLARE
                                    statements CURSOR FOR
                                        SELECT tablename FROM pg_tables
                                        WHERE tableowner = username AND schemaname = 'public';
                                BEGIN
                                    FOR stmt IN statements LOOP
                                        EXECUTE 'TRUNCATE TABLE ' || quote_ident(stmt.tablename) || ' CASCADE;';
                                    END LOOP;
                                END;
                                $$ LANGUAGE plpgsql;"""

execute('SELECT trunctate_tables(postgres);')
'''

with open('{}/CreateSqlTable.sql'.format(os.path.dirname(__file__)),'r',encoding='utf-8') as create_table_sql:
    execute(create_table_sql.read())

# Create accounts
create_account('brianliang','Brian','Liang','brianliang@gmail.com', 'm', '2021/06/12', 164, 63)
create_account('paigelin','Paige','Lin','paigelin@gmail.com', 'f', '2021/06/12', 165, 55)
create_account('peiyuleu','Andy','Leu','peiyuleu@gmail.com', 'm', '2021/06/12', 165, 55)
create_account('juliahuang','Julia','Huang','juliahuang@gmail.com', 'f', '2021/06/12', 170, 63)

accounts = get_account()
assert len(accounts)==4
account=accounts[0]

# Create access
access = create_access('brian3814@gmail.com', 'test123')

# Create foods
create_food('sandwitch',50,50,50)
create_food('avocado',50,50,50)
create_food('spaghetti',50,50,50)
create_food('burgers',50,50,50)

food_list = get_food_list()

# Create meal
meal_id = create_meal(account.uuid, '2021/06/14 13:10:59', 'lunch')
add_food_to_meal(meal_id,3) # Food id of 3 is spaghetti



read_setting()
print('PgEngine_Test Complete')