from _class.person import *
from _class.Intake import *
from _class.Genre import *
from _class.Event import *
from datetime import datetime
from collections import OrderedDict
from  _data_config import *

#####################################################################################################################
###############################   API   #############################################################################
#####################################################################################################################


# # api query the info from date to date
class Options():
    def __init__(self,person):
        self.isEnd = False
        self.person = person
        self.choice = {
        '1': ('tell me totally intake-kcal',self.func1),
        '2': ('xxx',self.func2),
        '3': ('Bye',self.func3)
        }

    def func1(self):
        start_d = input('Enter start date (yyyy-mm-dd) >')
        end_d = input('Enter end date (yyyy-mm-dd) >')
        self.get_total_kcal_with_time(self.person,start_d,end_d)

    def func2(self):
        print(self.person.name)

    def func3(self):
        exit(1)

    def get_total_kcal_with_time(self,person,start=None,end=None):
        _start = start if start!=None else input('Enter your start day')
        _end = end if end!=None else input('Enter your start day')
        result = person.caloiesIntakeCal(_start,_end)
        print('共消耗 {} kcal'.format(result['result']))
        for date, daily in result['dailyIntakes'].items():
            print(date)
            [print(data) for data in daily.meal_detail()]

    def run(self):
        opts = list(zip(self.choice.keys(),[i[0] for i in self.choice.values()]))
        
        while(not self.isEnd):
            print('\nWhat do you want to do?')
            for opt in opts:
                print(opt)
            choice = input('\nPlease choose by number:>')
            if choice not in self.choice.keys():
                "nonono"
            else:
                txt,action = self.choice[choice]
                print(txt)
                action()
 
if __name__ == "__main__":
    login = loginger()
    dc,basic_dict = login.run()
    person = dc.give_me_a_person_with_data()
    Options(person).run()
    # get_total_kcal_with_time(person,'2020-10-11','2020-10-12')
    print('Bye')

