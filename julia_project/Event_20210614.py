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

#### main: user sample code +
UserEvent = Event()






