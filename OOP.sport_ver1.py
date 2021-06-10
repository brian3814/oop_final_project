Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

>>> # Hello World program in Python
#import numpy as np

indoorActivity = {  "YOGA": 0,
                    "BADMINTON" : 1,
                    "GMY": 2,
                    "INDOOREND": 3 #檢查array有沒有超過
}

outdoorActivity = {  "TENNIS": 0,
                    "BASEBALL" : 1,
                    "OUTDOOREND": 2
}

weightDic = {  "W40KG": 0,
                "W50KG" : 1,
                "W60KG": 2,
                "WEND": 3
}

#julia: need modify tables
#indoor calories table (per hour)
#              40kg |  50kg |  60kg
# Yoga      | 10040 | 10050 | 10060
# Badminton | 20040 | 20050 | 20060
# GYM       | 30040 | 30050 | 300kg
indoorCaloriesTable = [ [10040,10050,10060],
                        [20040,20050,20060],
                        [30040,30050,30060]
                        ]

#outdoor calories table (per hour)
#              40kg |  50kg |  60kg
# Tennis    | 40040 | 40050 | 40060
# Baseball  | 50040 | 50050 | 50060
outdoorCaloriesTable = [ [40040,40050,40060],
                        [50040,50050,50060],
                        ]

class Sport:
    #constructor
    def __init__(self, outdoor, activity, hour, weight):
        self.__isOutdoor = outdoor
        self.__activity = activity
        self.__hour = hour
        self.__weight = weight


    #API
    def __getCaloriesPerHour(self):
        if self.__isOutdoor == 'Outdoor':
            tmpActivity = outdoorActivity[self.__activity]
            tmpW = weightDic[self.__weight]
            return outdoorCaloriesTable[tmpActivity][tmpW]
        else:
            tmpActivity = indoorActivity[self.__activity]
            tmpW = weightDic[self.__weight]
            return indoorCaloriesTable[tmpActivity][tmpW]

    # fot outdoor / indoor
    def SetOutdoor(self, setOutdoor):
        self.__isOutdoor = setOutdoor

    def GetOutdoor(self):
        print('GetOutdoor() = ' + self.__isOutdoor)
        return self.__isOutdoor

    # for activity setting / getting
    def SetActivity(self, activity):
        self.__activity = activity

    def GetActivity(self):
        print('GetActivity() = ' + self.__activity)
        return self.__activity

    # for hour setting / getting
    def SetHour(self, hour):
        if hour < 0 and hour > 24:
            print('SetHour():hour time over range')
        else:
            self.__hour = hour

    def GetHour(self):
        print('GetHour() = ' + str(self.__hour))
        return self.__hour

    # for weight setting / getting
    def SetWeight(self, weight):
        if weight < 'W40KG':
            print('SetWeight(): weight error')
        else:
            self.__weight = weight

    def GetWeight(self):
        print('GetWeight() = ' + str(self.__weight))
        return self.__weight

    # for calories tables getting
    def GetIndoorCaloriesTable(self):
        if self.__isOutdoor == 'Indoor':
            return indoorCaloriesTable
        else:
            print('GetIndoorCaloriesTable() fail')

    def GetOutdoorCaloriesTable(self):
        if self.__isOutdoor == 'Outdoor':
            return outdoorCaloriesTable
        else:
            print('GetOutdoorCaloriesTable() fail')

    # for calories computing
    def GetConsumedCalories(self): #one activity
        burnedCalories = self.__hour * self.__getCaloriesPerHour()
        print(str(self.__hour) + ' * ' + str(self.__getCaloriesPerHour()) + ' = ' + str(burnedCalories))
        return burnedCalories
