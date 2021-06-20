from _class.person import *
from _class.Intake import *
from _class.Genre import *
from _class.Event import *
from datetime import datetime
from collections import OrderedDict
from _class.data_config import *
import time

#####################################################################################################################
###############################   API   #############################################################################
#####################################################################################################################


# # api query the info from date to date
class Options():
    def __init__(self,person,dc):
        self.isEnd = False
        self.person = person
        self.dc = dc
        self.choice = {
        '1': ('Tell me total intake-kcal',self.func1),
        '2': ('Add new meal',self.func2),
        '3': ('Remove meal',self.func3),
        '4': ('Tell me total consumed-kcal',self.func4),
        '5': ('Add new event',self.func5),
        '9': ('Bye',self.func9)
        }

    def func1(self):
        start_d = input('Enter start date (yyyy-mm-dd)> ')
        end_d = input('Enter end date (yyyy-mm-dd)> ')
        self.person.get_total_kcal_with_time(start_d,end_d)

    def func2(self):
        time = input('Enter datetime (yyyy-mm-dd-HH:MM:SS)> ')
        name = input('Enter meal name > ')
        print('======= food list =======')
        _col = 0
        txt = ''
        for food in self.dc.food_dict.keys():
            txt += '{}, '.format(food)
            _col += 1
            if _col >= 3:
                print(txt)
                txt = ''
                _col = 0
        if _col > 0:
            print(txt)
        inTake = input('Enter inTake (a,b,c,...) > ').split(',')
        inTake = [self.dc.food_dict.get(item) for item in inTake]
        self.person.add_new_meal({'name':name,'time':time,'inTake':inTake})

    def func3(self):
        daily_dict = self.person.get_dailyIntakes()
        for date, daliyintake in daily_dict.items():
            print()
            print(date,daliyintake.total_intake_calories)
            print(daliyintake.meal_summary())
        date_str = input('Enter the date (yyyy-mm-dd)> ')
        index = input('Enter the meal index > ')
        self.person.remove_meal_by_index(date_str,int(index))

    def func4(self):
        start_d = input('Enter start date (yyyy-mm-dd)> ')
        end_d = input('Enter end date (yyyy-mm-dd)> ')
        self.person.get_totally_consumed_kcal_with_time(start_d,end_d)

    def func5(self):
        time = input('Enter datetime (yyyy-mm-dd-HH:MM:SS)> ')
        _col = 0
        txt = ''
        for food in self.dc.sport_list:
            txt += '{}, '.format(food)
            _col += 1
            if _col >= 3:
                print(txt)
                txt = ''
                _col = 0
        if _col > 0:
            print(txt)
        sports = input('Enter (sport,duration/sport,duration/...) > ').split('/')
        sports = [{'sport':sport.split(',')[0],'duration':float(sport.split(',')[1])} for sport in sports]
        self.person.add_new_event({'sports':sports,'time':time})

    def func9(self):
        exit(0)

    def run(self):
        opts = list(zip(self.choice.keys(),[i[0] for i in self.choice.values()]))
        while(not self.isEnd):
            print('\nWhat do you want to do?')
            for opt in opts:
                print(opt)
            choice = input('Please choose by number:> ')
            if choice not in self.choice.keys():
                "nonono"
            else:
                txt,action = self.choice[choice]
                print('=================================')
                print(txt)
                action()
 
if __name__ == "__main__":
    login = loginger()
    dc,basic_dict = login.run()
    person = dc.give_me_a_person_with_data()
    Options(person,dc).run()
    print('Bye')

