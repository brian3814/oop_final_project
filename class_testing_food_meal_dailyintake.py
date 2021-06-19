
from datetime import datetime
from _class.person import *
from _class.Intake import *
from _class.Genre import *
from _class.Event import *
datetime_string_type = '%Y-%m-%d-%H:%M:%S'
date_string_type = '-'.join(datetime_string_type.split('-')[0:3])


if __name__ == '__main__':
    #===============
    print("\n[[Food]]")
    apple = Food('apple')
    print(apple.name)
    apple.set_composition(1,2,3)
    print(apple.get_composition())
    print('apple {}'.format(apple.calories))
    banana = Food('banana',2,3,4)
    print('banana {}'.format(banana.calories))

    #===============
    print("\n[[Meal]]")
    meal = Meal('Lunch',datetime.today())
    print('meal {}'.format(meal.totalCalories))
    meal.add_food(apple)
    print('add food {}'.format(meal.totalCalories))
    meal.add_food(banana)
    print('add food {}'.format(meal.totalCalories))
    meal.empty_inTake()
    print('empty food {}'.format(meal.totalCalories))
    meal.add_food([apple,banana])
    print('add food {}'.format(meal.totalCalories))
    meal2 = Meal('Diner',datetime.today(),[apple,apple,apple])
    print('Diner {}'.format(meal2.totalCalories))

    #===============
    print("\n[[DailyIntakeCalories]]")
    today = DailyIntakeCalories(datetime.today())
    today.add_meal(meal)
    print('add meal {}'.format(today.total_intake_calories))
    today.add_meal(meal2)
    print('add meal {}'.format(today.total_intake_calories))
    today.empty_inTake()
    print('empty meal {}'.format(today.total_intake_calories))
    today.add_meal([meal,meal2])
    print('meal {}'.format(today.total_intake_calories))

    #===============
    print('End')


    # paige = Person('Paige', 0, 'premium', 25, 1.62, 54, 'female', 'yoga')
    # paige.showInfo()
    # paige.FollowFriend('julia')
    # paige.showFriendList()
    # paige.RemoveFriend('Julia')

    person_query = {'uuid':'qaz2wsx3edc','name':'AAAA','level':'Gold','birthday':datetime.strptime('2000-10-12-18:30:30', datetime_string_type),'height':1.56, 'weight':45, 'gender':'female', 'hobbies':'yoga'}
    person = Person(person_query['name'], person_query['uuid'], person_query['level'], person_query['birthday'], person_query['height'], person_query['weight'], person_query['gender'], person_query['hobbies'])
    person.showInfo()

    new_meal_info = {'name':'breakfirst','inTake':['apple','banana','orange'],'time':datetime.strptime('2020-10-10-08:30:30', datetime_string_type)}
    meal = Meal(name=new_meal_info['name'], time=new_meal_info['time'])
    meal.add_food(new_meal_info['inTake'])
    print(meal.food_summamry())

    # new_meal_info to new dailyintake_dict
    print('\nnew_meal_info to new dailyintake_dict')
    dailyintake_dict = OrderedDict()
    for data in [new_meal_info]:
        if dailyintake_dict.get(data['time'].strftime(date_string_type),None) == None:
            dailyintake_dict[data['time'].strftime(date_string_type)]=DailyIntakeCalories(data['time'])
        new_meal=Meal(data['name'],data['time'])
        new_meal.add_food(new_meal_info['inTake'])
        dailyintake_dict[data['time'].strftime(date_string_type)].add_meal(new_meal)

    print('===tak a look===')
    for date, daliyintake in dailyintake_dict.items():
        print(date,daliyintake.total_intake_calories)
        print(daliyintake.meal_summary())

    # new_meal_info to existed dailyintake_dict
    print('\nnew_meal_info to existed dailyintake_dict')
    new_meal_info_2 = {'name':'breakfirst','inTake':['apple','orange'],'time':datetime.strptime('2020-10-10-10:30:30', datetime_string_type)}
    for data in [new_meal_info_2]:
        if dailyintake_dict.get(data['time'].strftime(date_string_type),None) == None:
            dailyintake_dict[data['time'].strftime(date_string_type)]=DailyIntakeCalories(data['time'])
        new_meal=Meal(data['name'],data['time'])
        new_meal.add_food(new_meal_info['inTake'])
        dailyintake_dict[data['time'].strftime(date_string_type)].add_meal(new_meal)

    print('===tak a look===')
    for date, daliyintake in dailyintake_dict.items():
        print(date,daliyintake.total_intake_calories)
        print(daliyintake.meal_summary())
    

