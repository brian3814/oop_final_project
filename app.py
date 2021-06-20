from _class.person import *
from _class.Intake import *
from _class.Genre import *
from _class.Event import *
from datetime import datetime
from flask import Flask,jsonify,request
from collections import OrderedDict
from flask_cors import CORS,cross_origin
from PgEngine import *

datetime_string_type = '%Y-%m-%d-%H:%M:%S'
date_string_type = '-'.join(datetime_string_type.split('-')[0:3])

food_qrery = [
    {'name':'apple','carb':70,'protein':10,'fat':0.5},
    {'name':'banana','carb':90,'protein':2,'fat':0.1},
    {'name':'orange','carb':40,'protein':8,'fat':0},
    {'name':'burger','carb':60,'protein':20,'fat':10},
]
food_dict = {food['name']:Food(food['name'],food['carb'],food['protein'],food['fat']) for food in food_qrery}
print(food_dict)


meal_query = [
    {'name':'breakfirst','inTake':['apple','banana','orange'],'time':datetime.strptime('2020-10-10-08:30:30', datetime_string_type)},
    {'name':'lunch','inTake':['apple','banana','orange'],'time':datetime.strptime('2020-10-10-12:30:30', datetime_string_type)},
    {'name':'dinner','inTake':['burger','banana'],'time':datetime.strptime('2020-10-10-18:30:30', datetime_string_type)},
    {'name':'breakfirst','inTake':['apple','banana','orange'],'time':datetime.strptime('2020-10-11-08:30:30', datetime_string_type)},
    {'name':'lunch','inTake':['apple','banana','orange'],'time':datetime.strptime('2020-10-11-12:30:30', datetime_string_type)},
    {'name':'dinner','inTake':['apple','banana','burger'],'time':datetime.strptime('2020-10-11-18:30:30', datetime_string_type)},
    {'name':'breakfirst','inTake':['apple','orange'],'time':datetime.strptime('2020-10-12-08:30:30', datetime_string_type)},
    {'name':'lunch','inTake':['apple','banana','orange'],'time':datetime.strptime('2020-10-12-12:30:30', datetime_string_type)},
    {'name':'dinner','inTake':['apple','burger',],'time':datetime.strptime('2020-10-12-18:30:30', datetime_string_type)},
]

# {'2020-10-10': [Meal,Meal]}
meal_dict = OrderedDict()
for data in meal_query:
    if meal_dict.get(data['time'],None) == None:
        meal_dict[data['time']]=[]
    inTake=[food_dict[food_n] for food_n in data['inTake']]
    meal_dict[data['time']].append(Meal(data['name'],data['time'],inTake))


# {'2020-10-10': Daily{date:,meals}}
dailyintake_dict = OrderedDict()
for data in meal_query:
    if dailyintake_dict.get(data['time'].strftime(date_string_type),None) == None:
        dailyintake_dict[data['time'].strftime(date_string_type)]=DailyIntakeCalories(data['time'])
    inTake=[food_dict[food_n] for food_n in data['inTake']]
    dailyintake_dict[data['time'].strftime(date_string_type)].add_meal(Meal(data['name'],data['time'],inTake))

print('\n\n====')
for time,meals in meal_dict.items():
    for meal in meals:
        print(time.date(),meal.name,meal.totalCalories,meal.inTake)

print('\n\n====')
for date, daliyintake in dailyintake_dict.items():
    print(date,daliyintake.total_intake_calories,daliyintake.meals)




person_query = {'uuid':'qaz2wsx3edc','name':'AAAA','level':'Gold','birthday':datetime.strptime('2000-10-12-18:30:30', datetime_string_type),'height':1.56, 'weight':45, 'gender':'female', 'hobbies':'yoga'}
person = Person(person_query['name'], person_query['uuid'], person_query['level'], person_query['birthday'], person_query['height'], person_query['weight'], person_query['gender'], person_query['hobbies'])
person.showInfo()
person.update_dailyIntakes(dailyintake_dict)

person.CaloiesIntakeCal('2020-10-11','2020-10-12',date_string_type,date_string_type)



# sport_query = [
#     {'genre':[]},
#     ]

#     def __init__(self, genre, activity, hour, weight):
# #### Genre +
# #Genretype:
# notBALL = 0b00000001
# isBALL = 0b00000010
# Pearson = 0b00000100
# Interactive = 0b00001000
# Dynamic = 0b00010000
# Static = 0b00100000
# Outdoor = 0b01000000
# Indoor = 0b10000000
# #print(isBALL)


# # print(BALL)
# # print(STATIC)
# # print(INDOOR)

# #activity=GenreList
# GenreList = {'BowlingMorePeople': Indoor | Static | Interactive | isBALL,
#             'YogaMorePeople'    : Indoor | Static | Interactive | notBALL,
#             'BowlingSingle'     : Indoor | Static | Pearson | isBALL,
#             'YogaSingle'        : Indoor | Static | Pearson | notBALL,
#             'Badminton'         : Indoor | Dynamic | Interactive | isBALL,
#             'Dancing'           : Indoor | Dynamic | Interactive | notBALL,
#             'ShootingBaskets'   : Indoor | Dynamic | Pearson | isBALL,
#             'Trampoline'        : Indoor | Dynamic | Pearson | notBALL,
#             'GolfMorePeople'    : Outdoor | Static | Interactive | isBALL,
#             'TaiChiMorePeople'  : Outdoor | Static | Interactive | notBALL,
#             'GolfSingle'        : Outdoor | Static | Pearson | isBALL,
#             'TaiChi'            : Outdoor | Static | Pearson | notBALL,
#             'Baseball'          : Outdoor | Dynamic | Interactive | isBALL,
#             'RunMorePeople'     : Outdoor | Dynamic | Interactive | notBALL,
#             'BasketballSingle'  : Outdoor | Dynamic | Pearson | isBALL,
#             'RockClimbing'      : Outdoor | Dynamic | Pearson | notBALL
#             }
# print(GenreList)



app = Flask(__name__)

# Get api list
@app.route('/api', methods = ['GET'])          
def get_api_list():             #view
    routes = []
    for rule in app.url_map.iter_rules():
        route = rule.rule.replace('<','&lt').replace('>' ,'&gt')
        routes.append(route)
    result = "<h4>{}</h4>".format('</h4><h4>'.join(routes[:-1]))
    return result 

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/caloiesIntakeCal")
def caloiesIntakeCal():
    result = person.CaloiesIntakeCal('2020-10-11','2020-10-12',date_string_type,date_string_type)
    dailyIntake_dict= OrderedDict()
    for date, daily in result['dailyIntakes'].items():
        dailyIntake_dict[date]=daily.meal_detail()
    return {
        "name":person.name,
        "period": '{} to {}'.format('2020-10-11','2020-10-12'),
        "CaloiesIntakeCal":result['result'],
        "Intakes":dailyIntake_dict
        }

@app.route('/checkaccess',methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def loginPage():
    data= request.get_json()
    email = data.get('email')
    password = data.get('password')
    print(email,password)
    access = check_access(email,password)
    print(access)
    response = {'success':False} if access==None else{'success':True,'info':access} 

    return response



if __name__ == "__main__":
    app.run(host="0.0.0.0")
