from utils import *
from datetime import datetime

food_qrery = [
    {'name':'apple','carb':70,'protein':10,'fat':0.5},
    {'name':'banana','carb':90,'protein':2,'fat':0.1},
    {'name':'orange','carb':40,'protein':8,'fat':0},
    {'name':'burger','carb':60,'protein':20,'fat':10},
]
food_dict = {food['name']:Food(food['name'],food['carb'],food['protein'],food['fat']) for food in food_qrery}
print(food_dict)


meal_query = [
    {'name':'breakfirst','inTake':['apple','banana','orange'],'time':datetime.strptime('10-10-2020-08:30:30', '%m-%d-%Y-%H:%M:%S')},
    {'name':'lunch','inTake':['apple','banana','orange'],'time':datetime.strptime('10-10-2020-12:30:30', '%m-%d-%Y-%H:%M:%S')},
    {'name':'dinner','inTake':['burger','banana'],'time':datetime.strptime('10-10-2020-18:30:30', '%m-%d-%Y-%H:%M:%S')},
    {'name':'breakfirst','inTake':['apple','banana','orange'],'time':datetime.strptime('10-11-2020-08:30:30', '%m-%d-%Y-%H:%M:%S')},
    {'name':'lunch','inTake':['apple','banana','orange'],'time':datetime.strptime('10-11-2020-12:30:30', '%m-%d-%Y-%H:%M:%S')},
    {'name':'dinner','inTake':['apple','banana','burger'],'time':datetime.strptime('10-11-2020-18:30:30', '%m-%d-%Y-%H:%M:%S')},
    {'name':'breakfirst','inTake':['apple','orange'],'time':datetime.strptime('10-12-2020-08:30:30', '%m-%d-%Y-%H:%M:%S')},
    {'name':'lunch','inTake':['apple','banana','orange'],'time':datetime.strptime('10-12-2020-12:30:30', '%m-%d-%Y-%H:%M:%S')},
    {'name':'dinner','inTake':['apple','burger',],'time':datetime.strptime('10-12-2020-18:30:30', '%m-%d-%Y-%H:%M:%S')},
]

# {'2020-10-10': [Meal,Meal]}
meal_dict = {}
for data in meal_query:
    if meal_dict.get(data['time'],None) == None:
        meal_dict[data['time']]=[]
    inTake=[food_dict[food_n] for food_n in data['inTake']]
    meal_dict[data['time']].append(Meal(data['name'],data['time'],inTake))


# {'2020-10-10': Daily{date:,meals}}
dailyintake_dict = {}
for data in meal_query:
    if dailyintake_dict.get(data['time'].strftime('%m-%d-%Y'),None) == None:
        dailyintake_dict[data['time'].strftime('%m-%d-%Y')]=DailyIntakeCalories(data['time'])
    inTake=[food_dict[food_n] for food_n in data['inTake']]
    dailyintake_dict[data['time'].strftime('%m-%d-%Y')].add_meal(Meal(data['name'],data['time'],inTake))

print('\n\n====')
for time,meals in meal_dict.items():
    for meal in meals:
        print(time.date(),meal.name,meal.totalCalories,meal.inTake)

print('\n\n====')
for date, daliyintake in dailyintake_dict.items():
    print(date,daliyintake.total_intake_calories,daliyintake.meals)
