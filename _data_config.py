from datetime import datetime
from _class.person import *
from _class.Intake import *
from _class.Genre import *
from _class.Event import *
from PgEngine import *

datetime_string_type_with_time = '%Y-%m-%d-%H:%M:%S'
date_string_type = '-'.join(datetime_string_type_with_time.split('-')[0:3])


class loginger:

    # Declare as global variable to solve issue of query still empty after initilize 
    # if declared globally because loginger assigns to varaiable as local variable 
    # within local namesapace
    global food_query 
    global meal_query 
    global person_query 
    global event_query 


    def __init__(self):
        self.__success = False
        self.__account_info =None

    def logging(self,email,password):
        access = check_access(email,password)
        return (True, access) if access!=None else (False,access)

    def run(self):
        print('Hello, my friend. Stay awhile and listen ')
        times = 1

        init_db()

        while(not self._loginger__success and times<=3):
            email = input("Enter your email:")
            password = input("Enter your password:")
            self.__success, self.__account_info = self.logging(email,password)
            if self.__success == False: print('Too bad!\n\nPlease try again')
            times += 1

        if times > 3: 
            print('Bye')
            exit(1)

        print('\n\n\n')
        print('****** Welcome {} ******'.format(self.__account_info['name']))

        food_query=get_food_list()
        meal_query=get_account_all_meals(self.__account_info['id'])
        person_query = get_person(self.__account_info['id'])
        event_query =get_events()
        return DataCollecter(food_query,meal_query,event_query,person_query),{'food_list':food_query}


class DataCollecter:
    def __init__(self,food_query,meal_query,event_query,person_query):
        self.__food_dict = self.query_food_info(food_query)
        self.__dailyintake_dict = self.query_meal_info(meal_query)
        self.__dailyEvents_dict = self.query_event_info(event_query)
        self.__sport_list = self.query_sport_info()
        self.__person = self.query_person_info(person_query)

    @property
    def food_dict(self):
        return self.__food_dict

    @property
    def sport_list(self):
        return self.__sport_list

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
    def query_food_info(self,food_query):
        food_dict = {food['name']:Food(food['name'],food['carb'],food['protein'],food['fat']) for food in food_query}
        return food_dict

    def query_meal_info(self,meal_query):
        # {'2020-10-10': Daily{date:,meals}}
        dailyintake_dict = OrderedDict()
        for data in meal_query:
            if dailyintake_dict.get(data['time'].strftime(date_string_type),None) == None:
                dailyintake_dict[data['time'].strftime(date_string_type)]=DailyIntakeCalories(data['time'])
            inTake=[self.food_dict[food_n] for food_n in data['intake']]
            dailyintake_dict[data['time'].strftime(date_string_type)].add_meal(Meal(data['name'],data['time'],inTake))
        return dailyintake_dict

    def query_event_info(self,event_query):
        dailyEvents_dict = OrderedDict()
        for event in event_query:
            if dailyEvents_dict.get(event['time'].strftime(date_string_type),None) == None:
                dailyEvents_dict[event['time'].strftime(date_string_type)]=DailyConsumeCalories(event['time'],[])
            events = [(sport_dict['sport'],sport_dict['duration']) for sport_dict in event['sports']]
            UserEvent = Event()
            totalCalories = UserEvent.GetConsumedCalories(events)
            totalgenres = UserEvent.get_genre()
            dailyEvents_dict[event['time'].strftime(date_string_type)].add_event({'sports':events,'totalCalories':totalCalories,'totalgenres':totalgenres})
        return dailyEvents_dict

    def query_person_info(self,person_query):
        person = Person(person_query['name'], person_query['uuid'], person_query['level'], person_query['birthday'], person_query['height'], person_query['weight'], person_query['gender'], person_query['hobbies'])
        return person

    def query_sport_info(self):
        return  ['BowlingMorePeople',
                'YogaMorePeople',
                'BowlingSingle',
                'YogaSingle',
                'Badminton',
                'Dancing',
                'ShootingBaskets',
                'Trampoline',
                'GolfMorePeople',
                'TaiChiMorePeople',
                'GolfSingle',
                'TaiChi',
                'Baseball',
                'RunMorePeople',
                'BasketballSingle',
                'RockClimbing'
                ]

    def give_me_a_person_with_data(self):
        self.__person.update_dailyIntakes(self.__dailyintake_dict)
        self.__person.update_dailyEvents(self.__dailyEvents_dict)
        self.__person.add_food_info(self.__food_dict)
        return self.__person