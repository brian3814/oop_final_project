#### Sport class +
Activity = {'BowlingMorePeople': 0,
            'YogaMorePeople': 1,
            'BowlingSingle': 2,
            'YogaSingle': 3,
            'Badminton': 4,
            'Dancing': 5,
            'ShootingBaskets': 6,
            'Trampoline': 7,
            'GolfMorePeople' : 8,
            'TaiChiMorePeople': 9,
            'GolfSingle': 10,
            'TaiChi': 11,
            'Baseball': 12,
            'RunMorePeople' : 13,
            'BasketballSingle': 14,
            'RockClimbing' : 15,
            'ActivityEND' : 16
            }

weightDic = {"W40KG": 0,
             "W50KG": 1,
             "W60KG": 2,
             "WEND": 3
             }

# calories table (per hour,大卡)
#                       40kg | 50kg |  60kg
# BowlingMorePeople  |   149 |  161 |  173  #0
# YogaMorePeople     |   124 |  134 |  144  #1
# BowlingSingle      |   149 |  161 |  173  #2
# YogaSingle         |   124 |  134 |  144  #3
# Badminton          |   224 |  242 |  260  #4
# Dancing            |   238 |  257 |  276  #5
# ShootingBaskets    |   224 |  242 |  260  #6
# Trampoline         |   174 |  188 |  202  #7
# GolfMorePeople     |   224 |  242 |  260  #8
# TaiChiMorePeople   |   199 |  215 |  231  #9
# GolfSingle         |   224 |  242 |  260  #10
# TaiChi             |   199 |  215 |  231  #11
# Baseball           |   249 |  269 |  288  #12
# RunMorePeople      |   398 |  430 |  462  #13
# BasketballSingle   |   398 |  430 |  462  #14
# RockClimbing       |   547 |  591 |  635  #15


CaloriesTable = [[149,161,173], #0
                 [124,134,144], #1
                 [149,161,173], #2
                 [124,134,144], #3
                 [224,242,260], #4
                 [238,257,276], #5
                 [224,242,260], #6
                 [174,188,202], #7
                 [224,242,260], #8
                 [199,215,231], #9
                 [224,242,260], #10
                 [199,215,231], #11
                 [249,269,288], #12
                 [398,430,462], #13
                 [398,430,462], #14
                 [547,591,635], #15
                ]


class Sport:
    # constructor
    def __init__(self, genre, activity, hour, weight):
        self.__genre = genre
        self.__activity = activity
        self.__hour = hour
        self.__weight = weight

        self.basiccontinuoustime = 0
        self.carlories = 0

    # APIs
    def __getCaloriesPerHour(self):
        tmpActivity = Activity[self.__activity]
        tmpW = weightDic[self.__weight]
        return CaloriesTable[tmpActivity][tmpW]

    # for genre
    def SetGenre(self, genre):
        self.__genre = genre

    def GetGenre(self):
        print('GetGenre() = ' + self.__genre)
        return self.__genre

    # for activity=sportname setting / getting
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

    # for hour setting / getting
    def SetWeight(self, weight):
        if weight < 'W40KG':
            print('SetWeight(): weight error')
        else:
            self.__weight = weight

    def GetWeight(self):
        print('GetWeight() = ' + str(self.__weight))
        return self.__weight

    # for calories tables getting
    def GetCaloriesTable(self):
        return CaloriesTable

    # for calories computing, ConsumedInInterval for Event 計算用
    def GetConsumedCalories(self):
        burnedCalories = self.__hour * self.__getCaloriesPerHour()
        print(str(self.__hour) + ' * ' + str(self.__getCaloriesPerHour()) + ' = ' + str(burnedCalories))
        return burnedCalories

    #user設定要達到運動效果
    #user最少需要多少時間
    def SetbasicContinuousTime(self, basiccontinuoustime):
        if basiccontinuoustime < 0 and basiccontinuoustime > 24:
            print('SetbasicContinuousTime():hour time over range')
        else:
            self.basiccontinuoustime = basiccontinuoustime

    def GetbasicContinuousTime(self):
        print('GetbasicContinuousTime() = ' + str(self.basiccontinuoustime))
        return self.basiccontinuoustime

    # user設定運動效果用
    def GetbasicConsumption(self):  # one activity
        basicconsumption = self.basiccontinuoustime * self.__getCaloriesPerHour()
        print(str(self.basiccontinuoustime) + ' * ' + str(self.__getCaloriesPerHour()) + ' = ' + str(basicconsumption))
        return basicconsumption
