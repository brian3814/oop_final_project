import os,sys,json,shutil
import psycopg2
import logging

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

def execute(query_string):
    conn = build_connection()
    cur = conn.cursor()
    cur.execute(query_string)
    
    for notice in conn.notices:
        logger.info(f'{notice}')
    
    conn.commit()

def get_meal():
    get_meal_query=''
    # execute(sql_query)
    pass

# For test only

def drop_table(table_name):
    sql_query = 'DROP TABLE IF EXISTS {};'.format(table_name)
    execute(sql_query)


drop_table('meal')