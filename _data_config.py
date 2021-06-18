
from datetime import datetime
from _class.person import *
from _class.Intake import *
from _class.Genre import *
from _class.Event import *


datetime_string_type = '%Y-%m-%d-%H:%M:%S'
date_string_type = '-'.join(datetime_string_type.split('-')[0:3])

food_qrery = [
    {'name':'apple','carb':70,'protein':10,'fat':0.5},
    {'name':'banana','carb':90,'protein':2,'fat':0.1},
    {'name':'orange','carb':40,'protein':8,'fat':0},
    {'name':'burger','carb':60,'protein':20,'fat':10},
]

event_query = [
    {'sports':[{'sport':'YogaMorePeople','duration':3},{'sport':'GolfMorePeople','duration':1.5}],'time':datetime.strptime('2020-10-10-18:30:30', datetime_string_type)},
    {'sports':[{'sport':'Baseball','duration':1},{'sport':'ShootingBaskets','duration':1.5}],'time':datetime.strptime('2020-10-11-18:30:30', datetime_string_type)},
    {'sports':[{'sport':'GolfMorePeople','duration':2}],'time':datetime.strptime('2020-10-12-12:30:30', datetime_string_type)},
    {'sports':[{'sport':'YogaMorePeople','duration':1.5}],'time':datetime.strptime('2020-10-12-18:30:30', datetime_string_type)},
]

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

person_query = {'uuid':'qaz2wsx3edc','name':'AAAA','level':'Gold','birthday':datetime.strptime('2000-10-12-18:30:30', datetime_string_type),'height':156, 'weight':45, 'gender':'female', 'hobbies':'yoga'}

access_query = [
    {'name':'Andy','email':'Andy@email.com','password':'Andy'},
    {'name':'Peige','email':'Peige@email.com','password':'Peige'},
    {'name':'Julia','email':'Julia@email.com','password':'Julia'},
    {'name':'Guest','email':'Guest@email.com','password':'Guest'},
    ]

class loginger:
    def __init__(self):
        self.__access_dict = access_query
        self.__success = False

    def logging(self,email,password):
        result = False
        self.name = None
        for data in self._loginger__access_dict:
            if (email == data['email'] and password == data['password']):
                result = True
                self.name = data['name']
        # return result
        return True

    def run(self):
        print('Hello, my friend. Stay awhile and listen ')
        times = 1
        while(not self._loginger__success and times<=3):
            email = input("Enter your email:")
            password = input("Enter your password:")
            self.__success = self.logging(email,password)
            if self.__success == False: print('Too bad!\n\nPlease try again')
            times += 1

        if times > 3: 
            print('Bye')
            exit(1)

        print('\n')
        print('Hi {}'.format(self.name))
        return self.name

class DataCollecter:
    def __init__(self):
        self.__food_dict = self.query_food_info(food_qrery)
        self.__dailyintake_dict = self.query_meal_info(meal_query)
        self.__dailyEvents_dict = self.query_event_info(event_query)
        self.__person = self.query_person_info(person_query)

    @property
    def food_dict(self):
        return self.__food_dict

    @property
    def dailyintake_dict(self):
        return self.__dailyintake_dict

    @property
    def dailyEvents_dict(self):
        return self.__dailyEvents_dict

    @property
    def person(self):
        return self.__person


    #################
    def query_food_info(self,food_qrery):
        food_dict = {food['name']:Food(food['name'],food['carb'],food['protein'],food['fat']) for food in food_qrery}
        return food_dict

    def query_meal_info(self,meal_query):
        # {'2020-10-10': Daily{date:,meals}}
        dailyintake_dict = OrderedDict()
        for data in meal_query:
            if dailyintake_dict.get(data['time'].strftime(date_string_type),None) == None:
                dailyintake_dict[data['time'].strftime(date_string_type)]=DailyIntakeCalories(data['time'])
            inTake=[self.food_dict[food_n] for food_n in data['inTake']]
            dailyintake_dict[data['time'].strftime(date_string_type)].add_meal(Meal(data['name'],data['time'],inTake))
        return dailyintake_dict

    def query_event_info(self,event_query):
        dailyEvents_dict = OrderedDict()
        for event in event_query:
            if dailyEvents_dict.get(event['time'].strftime(date_string_type),None) == None:
                dailyEvents_dict[event['time'].strftime(date_string_type)]=DailyConsumeCalories(event['time'])
            events = [(sport_dict['sport'],sport_dict['duration']) for sport_dict in event['sports']]
            UserEvent = Event()
            totalCalories = UserEvent.GetConsumedCalories(events)
            totalgenres = UserEvent.get_genre()
            dailyEvents_dict[event['time'].strftime(date_string_type)].add_event({'sports':events,'totalCalories':totalCalories,'totalgenres':totalgenres})
        return dailyEvents_dict

    def query_person_info(self,person_query):
        person = Person(person_query['name'], person_query['uuid'], person_query['level'], person_query['birthday'], person_query['height'], person_query['weight'], person_query['gender'], person_query['hobbies'])
        return person

    def give_me_a_person_with_data(self):
        self.__person.update_dailyIntakes(self.__dailyintake_dict)
        self.__person.update_dailyEvents(self.__dailyEvents_dict)
        return self.__person