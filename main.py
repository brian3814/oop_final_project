from _class.person import *
from _class.Intake import *
from _class.Genre import *
from _class.Event import *
from datetime import datetime
from flask import Flask,jsonify
from collections import OrderedDict


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


#####################################################################################################################
###############################   API   #############################################################################
#####################################################################################################################

# api query the info from date to date
def caloiesIntakeCal():
    result = person.CaloiesIntakeCal('2020-10-11','2020-10-12',date_string_type,date_string_type)
    dailyIntake_dict= OrderedDict()
    for date, daily in result['dailyIntakes'].items():
        dailyIntake_dict[date]=daily.meal_detail()
    return OrderedDict([
        ("name",person.name),
        ("period",'{} to {}'.format('2020-10-11','2020-10-12')),
        ("CaloiesIntakeCal",result['result']),
        ("Intakes",dailyIntake_dict)
    ])
print(caloiesIntakeCal())


