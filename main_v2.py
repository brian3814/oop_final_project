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
        '1': ('tell me totally intake-kcal',selffunc1),
        '2': ('xxx',print,(self.person.name)),
        '3': ('Bye',exit,(1))
        }

    def func1(self):
        get_total_kcal_with_time(self.person)

    def get_total_kcal_with_time(person,start=None,end=None):
        _start = start if start!=None else input('Enter your start day')
        _end = end if end!=None else input('Enter your start day')
        result = person.caloiesIntakeCal(_start,_end)
        print('共消耗 {} kcal'.format(result['result']))
        for date, daily in result['dailyIntakes'].items():
            print(date)
            [print(data) for data in daily.meal_detail()]

    def run(self):
        while(not self.isEnd):
            choice = input(self.choice.keys())
            if choice not in self.choice.keys():
                "nonono"
            else:
                txt,action,args = self.choice[choice]
                print(txt)
                action(*args)
 
if __name__ == "__main__":
    name = loginger().run()
    data = DataCollecter()
    person = data.give_me_a_person_with_data()
    Options(person).run()
    get_total_kcal_with_time(person,'2020-10-11','2020-10-12')
    print('Bye')

