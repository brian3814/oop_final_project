import os,sys,json,shutil
import psycopg2
import logging
from _class.person import *
from _class.Intake import *
from _class.Genre import *
from _class.Event import *
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


# Set logger
logging.basicConfig(filename='PgConnLog.log',
                    level = logging.DEBUG,
                    format = '%(asctime)s [%(levelname)s] %(message)s (%(filename)s %(lineno)d)',
                    datefmt='%Y%m%d %H:%M:%S')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Datetime format
datetime_string_type_with_time = '%Y-%m-%dT%H:%M:%S'
datetime_string_type_without_time = '%Y-%m-%d'


# Read setting
setting={}
def read_setting():
    with open('{}/setting.json'.format(os.path.dirname(__file__)),'r',encoding='utf-8') as sf:
        temp = json.load(sf)['conn_info']
        for k,v in temp.items():
            setting[k]=v

read_setting()

def execute(query_string,values=None):
    conn = build_connection_with_db()

    if conn==None:
        return None

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

def build_connection_with_server():
    if setting is None:
        logger.error('Setting required to build connection')
        return None

    try:
        conn_init = psycopg2.connect(
            host = setting['host'],
            port = setting['port'],
            user = setting['username'], 
            password = setting['password'])

        conn_init.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) 

    except:
        logger.error("Failed to build connection with server:{}".format(setting))
        return None 

    return conn_init

def build_connection_with_db():
    if setting is None:
        logger.error('Setting required to build connection')
        return None

    try:
        conn_init = psycopg2.connect(
            host = setting['host'],
            port = setting['port'],
            database = setting['database'],
            user = setting['username'], 
            password = setting['password'])

        conn_init.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) 
    except:
        logger.error("Failed to build connection with database:{}".format(setting))
        return None 

    return conn_init

def init_db():
    if not check_db_exist(setting['database']):
        
        with open('{}/CreateSqlTable.sql'.format(os.path.dirname(__file__)),'r',encoding='utf-8') as create_table_sql:
            conn1= build_connection_with_server()
            cur1 = conn1.cursor()
            cur1.execute("""CREATE DATABASE {};""".format(setting['database']));
            conn1.commit()

            conn2 =build_connection_with_db()
            cur2 = conn2.cursor()
            cur2.execute(create_table_sql.read())

        logger.info('Database created:{}'.format(setting))

def check_db_exist(db_name):
    conn = build_connection_with_server()
    cur= conn.cursor()
    cur.execute("""SELECT datname FROM pg_database;""")
    result = cur.fetchall()
    db_list = [ d[0] for d in result]
    conn.commit()
    return db_name in db_list


# Authentication related
def create_access(level,email,password):
    create_access_query="""INSERT INTO Access (email, password, level) VALUES (%s, %s, %s) RETURNING id"""
    values = (email, password,level)
    result =  execute(create_access_query,values)
    return result[0][0]

def check_access(email,password):
    check_access_query="""
        SELECT json_build_object(
            'id',account.id,
            'name',account.first_name
        ) 
        FROM Account
        LEFT JOIN Access 
        ON Access.id = Account.id
        WHERE Access.email = %s
        AND Access.password = %s
    """
    values =(email,password)
    result = execute(check_access_query,values)
    return result[0][0] if result !=None and len(result)==1 else None

# Accout related
def create_account(account_type,first_name,last_name,gender,birthday,height,weight):
    create_account_query ="""
        INSERT INTO Account (accout_type,first_name,last_name,gender,birthday,height,weight) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s) 
        RETURNING row_to_json(Account)   
    """ 
    values =(account_type,first_name,last_name,gender,birthday,height,weight)
    result = execute(create_account_query,values)
    info = 'Account: {} has been created sucessfully'.format(result[0])
    logger.info(info)
    return result[0]

def get_accounts():
    sql_query ="""SELECT row_to_json(Account) FROM Account;""" 
    values = None
    result =execute(sql_query,values)
    for i in range(len(result)):
        print('Accounts: {}'.format(result[i]))

    return [orm_factory('Person',i[0]) for i in result]



# Person related 
def get_person(access_id):
    get_person_query="""
        SELECT row_to_json(row)
        FROM(
            SELECT a.id AS uuid,
                CONCAT(a.first_name, ' ', a.last_name) as name,
                l.level_desc as level,
                a.birthday,
                a.height,
                a.weight,
                a.gender,
                a.hobbies
            FROM Account a
            LEFT JOIN Access AS b
            ON a.id = b.id
            LEFT JOIN Level AS l
            ON b.level = l.level_no
            WHERE a.id = %s
        ) row
    """
    values = (access_id,)
    result= execute(get_person_query,values)
    for p in result:
        p[0]['birthday'] = datetime.strptime(p[0]['birthday'],datetime_string_type_without_time) 
    logger.info('Returned person:{}'.format(result))
    return result[0][0]

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


# Food/meal related
def create_food(food_name,carb,protein,fat):
    create_food_query="""INSERT INTO Food (food_name,carb,protein,fat) VALUES (%s,%s,%s,%s)"""
    values = (food_name,carb,protein,fat)
    execute(create_food_query,values)
    info = 'Food: {} has been created sucessfully'.format(food_name)
    logger.info(info)

def get_food_list():
    get_food_list_query="""
        SELECT json_build_object(
            'name',f.food_name,
            'carb',f.carb,
            'protein',f.protein,
            'fat',f.fat
        )
        FROM food f
    """

    result = [r[0] for r in execute(get_food_list_query)]
    logger.info(result)
    return result

def get_food_index_by_name(food_name):
    get_food_index="""
        SELECT f.id
        FROM Food f
        WHERE f.food_name= %s
    """
    values = (food_name,)
    result=execute(get_food_index,values)
    return result[0][0]

def create_meal(user_id, meal_time , meal_desc, intake=[]):
    intake = [get_food_index_by_name(f) if type(f)!= int else f for f in intake]

    create_meal_query="""
        WITH ins1 AS(
            INSERT INTO Meal (account_id,meal_time,meal_desc,intake)
            VALUES (%s,%s,%s,%s) 
            RETURNING id AS meal_id 
        )
        UPDATE Account 
        SET meals = array_append(meals, ins1.meal_id)
        FROM ins1
        WHERE Account.id = %s
        RETURNING ins1.meal_id;"""
    values=(user_id,meal_time,meal_desc,intake,user_id)
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

def get_account_all_meals(access_id):
    get_account_all_meals = """
        SELECT row_to_json(row)
        FROM (
            SELECT m.id,
                m.account_id ,
                m.meal_desc AS name,
                m.meal_time AS time,
                Array(
                    SELECT f.food_name
                    From unnest(m.inTake) WITH ORDINALITY AS a(id, ord)
                    LEFT JOIN Food f ON f.id =  a.id
                ) AS inTake
            FROM Meal AS m
            WHERE m.account_id = %s
        ) row
        
    """

    values=(access_id,)
    result = execute(get_account_all_meals,values)
    logger.info('Meals of account fetched:{}'.format(result))
        
    for m in result:
        m[0]['time'] = datetime.strptime(m[0]['time'],datetime_string_type_with_time)
    return [m[0] for m in result]

def get_all_meals():
    get_all_meals="""
        SELECT row_to_json(row)
        FROM (
            SELECT m.id,
                m.account_id ,
                m.meal_desc AS name,
                m.meal_time AS time,
                Array(
                    SELECT f.food_name
                    From unnest(m.inTake) WITH ORDINALITY AS a(id, ord)
                    LEFT JOIN Food f ON f.id =  a.id
                ) AS inTake
            FROM Meal AS m
        ) row 
    """
    result = execute(get_account_all_meals)
    logger.info('All meals fetched:{}'.format(result))
    return [m[0] for m in result]

def get_daily_intake(user_id, start_date, end_date):
    #get_meal_query="""SELECT """
    #execute(get_meal_query)
    pass

# Events/Sports related
def get_events():
    get_events_query="""
        SELECT row_to_json(event)
        FROM (
            SELECT e.event_name AS name,
                CONCAT(a.first_name,' ',a.last_name) As host,
                e.location AS location,
                e.time AS time,
                e.min_participants AS required_participants,
                ARRAY(
                    SELECT json_build_object(
                        'sport', s.sport_name,
                        'duration', EXTRACT(epoch FROM ev.duration)/3600
                    ) 
                    FROM UNNEST(e.event_contents) WITH ORDINALITY AS ec(ec_id,ord)
                    LEFT JOIN Event_content ev
                    ON ec.ec_id = ev.content_id
                    LEFT JOIN Sport s
                    ON s.sport_id = ev.sport_id
                ) AS sports
            FROM Event e
            LEFT JOIN Account a
            ON a.id = e.host
        ) event
    """
    
    result = execute(get_events_query)
    for e in result:
        e[0]['time'] = datetime.strptime(e[0]['time'],datetime_string_type_without_time)
        

    return [e[0] for e in result]

def create_genre(genre_desc):
    create_genre="""INSERT INTO Genre (description) 
        VALUES (%s)
        RETURNING row_to_json(Genre)
    """
    values=(genre_desc,)
    result=execute(create_genre,values)
    info = 'Genre: {} has been created sucessfully'.format(genre_desc)
    logger.info(info)
    return result

def get_genre(genre_id):
    get_genre="""
        SELECT row_to_json(Genre) FROM Genre
        WHRER id = %s
    """
    values = (genre_id)
    result = execute(get_genre)
    return result

def create_sport(sport_name,calories_burned_per_hr,basic_continuous_time,genre=[]):
    create_sport="""
        WITH ins1 AS(
            INSERT INTO Sport (sport_name,calories_burned_per_hr,basic_continuous_time)
            VALUES (%s,%s,%s)
            RETURNING id AS sport_id
        )
        INSERT INTO SportsGenre (sport_id, genre_id)
        SELECT ins1.sport_id, %s
        FROM ins1
    """
    values = (sport_name,calories_burned_per_hr,basic_continuous_time,genre)
    execute(create_sport,values)

def get_sport_genre():
    pass

'''
# ORM related
def orm_factory(target_class,info):
    if target_class =='Person':
        temp = Person()
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
'''

