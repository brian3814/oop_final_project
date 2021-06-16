class Event:
    # constructor (variables)
    def __init__(self):
        self.__sport = Sport('Indoor', 'YogaSingle', 1, 'W40KG')  # 引用class Sport &初始化
        self.__activityList = []
        self.__timeList = []  # dulluration
        self.__totalCalories = 0
        return

    # API
    # for calories computing
    def GetConsumedCalories(self, weight, event):  # event=sport set
        print(event)

        self.__sport.SetWeight(weight)
        self.__activityList = list(event.keys())
        self.__timeList = list(event.values())

        for index in range(len(event)):
            print(' ---- ' + str(index))
            print(self.__activityList[index])
            self.__sport.SetActivity(self.__activityList[index])  # 引入Class Sport裡面的SetActivity

            print(self.__timeList[index])
            self.__sport.SetHour(self.__timeList[index])  # 引入Class Sport裡面的SetHour

            self.__totalCalories += self.__sport.GetConsumedCalories()
        return self.__totalCalories
#### Event class -







