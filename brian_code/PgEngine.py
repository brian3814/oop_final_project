import os,sys,json,shutil
import psycopg2
import logging
import class_person
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


# Set logger
logging.basicConfig(filename='PgConnLog.log',
                    level = logging.DEBUG,
                    format = '%(asctime)s [%(levelname)s] %(message)s (%(filename)s %(lineno)d)',
                    datefmt='%Y%m%d %H:%M:%S')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Read setting
setting={}
def read_setting():
    with open('{}/setting.json'.format(os.path.dirname(__file__)),'r',encoding='utf-8') as sf:
        temp = json.load(sf)['conn_info']
        for k,v in temp.items():
            setting[k]=v


read_setting()

# Functions below
def execute(query_string,values=None):
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
    if setting is None:
        logger.error('Setting required to build connection')
        return None

    conn_init = psycopg2.connect(
        host = setting['host'],
        port = setting['port'],
        database = setting['database'],
        user = setting['username'], 
        password = setting['password'])

    conn_init.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) 

    return conn_init

# Authentication related
def create_access(email,password):
    create_access_query="""INSERT INTO Access (email, password) VALUES (%s, %s)"""
    values = (email, password)
    execute(create_access_query,values)

def check_access():
    check_access_query=''
    pass



# Person related 
def get_friend_list():
    pass

def follow_friend():
    pass

def unfollow_friend():
    pass

def host_event():
    pass

def get_interested_events():
    pass

def get_friends_going():
    pass

def sign_up_event():
    pass



# Accout related
def create_account(account_name,first_name,last_name,email,gender,birthday,height,weight):
    create_account_query ="""INSERT INTO Account (account_name,first_name,last_name,email,gender,birthday,height,weight) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""" 
    values =(account_name,first_name,last_name,email,gender,birthday,height,weight)
    execute(create_account_query,values)
    info = 'Account: {} has been created sucessfully'.format(account_name)
    logger.info(info)
    print(info)

def get_account():
    sql_query ="""SELECT row_to_json(Account) FROM Account;""" 
    values = None
    result =execute(sql_query,values)
    for i in range(len(result)):
        print('Accounts: {}'.format(result[i]))

    return [orm_factory('Person',i[0]) for i in result]



# Food/meal related
def create_food(food_name,carb,protein,fat):
    create_food_query="""INSERT INTO Food (name,carb,protein,fat) VALUES (%s,%s,%s,%s)"""
    values = (food_name,carb,protein,fat)
    execute(create_food_query,values)
    info = 'Food: {} has been created sucessfully'.format(food_name)
    logger.info(info)

def get_food_list():
    get_food_list_query="""
        SELECT row_to_json(Food)
        FROM Food 
    """
    result = execute(get_food_list_query)
    return result

def create_meal(user_id, meal_time , meal_desc, intake=[]):
    print('create meal')
    print(user_id)
    create_meal_query="""
        WITH ins1 AS(
            INSERT INTO Meal (meal_time,meal_desc,intake)
            VALUES (%s,%s,%s) 
            RETURNING id AS meal_id 
        )
        UPDATE Account 
        SET meal = array_append(meal, ins1.meal_id)
        FROM ins1
        WHERE Account.uuid = %s
        RETURNING ins1.meal_id;"""
    values=(meal_time,meal_desc,intake,user_id)
    result = execute(create_meal_query,values)[0][0]   

    info = 'Meal: {} has been created sucessfully'.format(meal_desc)
    logger.info(info)

    return result

def add_food_to_meal(meal_id,food_id):
    add_food_to_meal_query="""
        UPDATE Meal
        SET inTake = array_append(inTake, %s)
        WHERE id = %s;
    """
    values=(food_id,meal_id)
    execute(add_food_to_meal_query,values)
    pass

def get_meals_in_interval():
    # get_meal_query="""SELECT """
    # execute(get_meal_query)
    pass

# Sports related
def get_sport_info():
    get_sport_info_query="""
    
    """
    execute(get_sport_info_query)


# ORM related
def orm_factory(target_class,info):
    if target_class =='Person':
        temp = class_person.Person()
        for k,v in info.items():
            if k in temp.__dict__:
                temp.__dict__[k]=v
        return temp
    
# Test below
def orm_test():
    sql_query ="""SELECT row_to_json(Account) FROM Account;""" 
    values = None
    result =execute(sql_query,values)
    for i in range(len(result)):
        print('Accounts: {}'.format(result[i]))

    return [orm_factory('Person',i[0]) for i in result]


