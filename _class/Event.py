#### Sport class +
Activity = {"YOGA": 0,
            "BADMINTON": 1,
            "GMY": 2,
            "TENNIS": 3,
            "BASEBALL": 4,
            "ACTIVITYEND": 5
            }

weightDic = {"W40KG": 0,
             "W50KG": 1,
             "W60KG": 2,
             "WEND": 3
             }

# calories table (per hour)
#              40kg |  50kg |  60kg
# Yoga      | 10040 | 10050 | 10060
# Badminton | 20040 | 20050 | 20060
# GYM       | 30040 | 30050 | 30060
# Tennis    | 40040 | 40050 | 40060
# Baseball  | 50040 | 50050 | 50060

CaloriesTable = [[10040, 10050, 10060],
                 [20040, 20050, 20060],
                 [30040, 30050, 30060],
                 [40040, 40050, 40060],
                 [50040, 50050, 50060]
                ]


class Sport:
    # constructor
    def __init__(self, genre, activity, hour, weight):
        self.__genre = genre
        self.__activity = activity
        self.__hour = hour
        self.__weight = weight

        self.basiccontinuoustime = 0
        self.filepath = []
        self.carlories = 0

    # APIs
    # julia
    def __getCaloriesPerHour(self):
        tmpActivity = Activity[self.__activity]
        tmpW = weightDic[self.__weight]
        return CaloriesTable[tmpActivity][tmpW]

    # fot genre
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

    # for calories compute
    def GetConsumedCalories(self):
        burnedCalories = self.__hour * self.__getCaloriesPerHour()
        print(str(self.__hour) + ' * ' + str(self.__getCaloriesPerHour()) + ' = ' + str(burnedCalories))
        return burnedCalories


    #user設定要達到運動效果
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
        basicconsumption = self.__weight * self.basiccontinuoustime * self.__getCaloriesPerHour()
        print(str(self.__weight) + ' * ' + str(self.basiccontinuoustime) + ' * ' + str(self.__getCaloriesPerHour()) + ' = ' + str(basicconsumption))
        return basicconsumption



class Event:
    # constructor (variables)

    def __init__(self):
        self.__sport = Sport('Indoor', 'YOGA', 1, 'W40KG')  # 引用class Sport &初始化
        self.__activityList = []  # yoga
        self.__timeList = []  # dulluration
        self.__totalCalories = 0
        return

    # for calories compute

    def GetConsumedCalories(self, weight, event):  # event=sport set
        print(event)

        self.__sport.SetWeight(weight)
        self.__activityList = list(event.keys())
        self.__timeList = list(event.values())

        for index in range(len(event)):
            print(' ---- ' + str(index))  # inder=0
            print(self.__activityList[index])  # GYM
            self.__sport.SetActivity(self.__activityList[index])  # 引入Class Sport裡面的SetActivity

            print(self.__timeList[index])  # 5
            self.__sport.SetHour(self.__timeList[index])  # 引入Class Sport裡面的SetHour

            self.__totalCalories += self.__sport.GetConsumedCalories()
        return self.__totalCalories
#### Event class -