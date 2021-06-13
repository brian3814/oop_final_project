import os,sys,json,shutil
import psycopg2
import logging
import class_person


# Set logger
logging.basicConfig(filename='PgConnLog.log',
                    level = logging.DEBUG,
                    format = '%(asctime)s [%(levelname)s] %(message)s (%(filename)s %(lineno)d)',
                    datefmt='%Y%m%d %H:%M:%S')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Read settings
with open('setting.json','r',encoding='utf-8') as settings:
    _setting = json.load(settings) if settings != None else None

# Functions below
def execute(query_string,values):
    conn = build_connection()
    cur = conn.cursor()
    exe_result = None

    if values != None:
        cur.execute(query_string, values)
    else:
        cur.execute(query_string)

    if cur.description != None:    
        exe_result = cur.fetchall() 

    for notice in conn.notices:
        logger.info(f'{notice}')
    
    conn.commit()

    return exe_result 

def build_connection():
    if _setting is None:
        logger.error('Failed to build connection with the database')
        return None

    conn_init = psycopg2.connect(
        host = _setting['conn_info']['host'],
        port = _setting['conn_info']['port'],
        database = _setting['conn_info']['database'],
        user = _setting['conn_info']['username'], 
        password = _setting['conn_info']['password'])
    return conn_init

def get_meal():
    get_meal_query=''
    # execute(sql_query)
    pass

# Authorization related
def create_access():
    pass

def check_access():
    pass

# Accout related
def create_account(account_name,gender,birthday,height,weight):
    sql_query ="""INSERT INTO Account (account_name,gender,birthday,height,weight) VALUES (%s,%s,%s,%s,%s)""" 
    values =(account_name,gender,birthday,height,weight)
    execute(sql_query,values)
    print('Account: {} has been created sucessfully'.format(account_name))

def get_account():
    sql_query ="""SELECT row_to_json(Account) FROM Account;""" 
    values = None
    result =execute(sql_query,values)
    for i in range(len(result)):
        print('Accounts: {}'.format(result[i]))

    return [class_person.Person(json.dumps(i[0])) for i in result]

# Meal related

def orm_test():
    sql_query ="""SELECT row_to_json(Account) FROM Account;""" 
    values = None
    result =execute(sql_query,values)
    for i in range(len(result)):
        print('Accounts: {}'.format(result[i]))

    return [orm_factory('Person',i[0]) for i in result]

def orm_factory(target_class,info):
    if target_class =='Person':
        temp = class_person.Person()
        for k,v in info.items():
            if k in temp.__dict__:
                temp.__dict__[k]=v
        return temp
    


