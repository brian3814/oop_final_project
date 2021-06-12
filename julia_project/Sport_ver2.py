#class ActivityGenre:


class Sport:
    #constructor

    def __init__(self, genre, sportname, caloriesperhour, basiccontinuoustime, hour):
        self.__genre = genre #outdoor/static
        self.__sportname = sportname #yoga/tennis
        self.__caloriesperhour = caloriesperhour
        self.__basiccontinuoustime = basiccontinuoustime
        self.__hour = hour

    #API

    @property
    def ActivityGenre(self):
        print('ActivityGenre() =' + self__genre)
        return self.__genre

    @ActivityGenre.setter
    def ActivityGenre(self, genre):
        self.__genre = genre

    @property
    def Sportname(self):
        print('GetSportname() =' + self.__sportname)
        return self.__sportname

    @Sportname.setter
    def Sportname(self, sportname):
        self.__sportname = sportname

    @property
    def caloriesBurnedPerHour(self):
        print('caloriesBurnedPerHour() =' + float(self.__caloriesperhour))

    @caloriesBurnedPerHour.setter
    def caloriesBurnedPerHour(self, caloriesperhour): #unit for each sport
        self.__caloriesperhour = caloriesperhour

    # for user judging min time
    @property
    def basicContinousTime(self):
        print("basicContinousTime() =" + self.__asiccontinuoustime)
        return Self.__basiccontinuoustime

    def basicContinuousTime(self, basiccontinuoustime):
       if basiccontinuoustime < 0 and basiccontinuoustime > 24:
            print('basicContinuousTime (): basiccontinuoustime over range')
       else:
            self.__basiccontinuoustime = basiccontinuoustime

    # hour setting / getting for computing ConsumedInInterval
    @property
    def Hour(self):
        print('Hour() = ' + float(self.__hour))
        return self.__hour

    @Hour.setter
    def Hour(self, hour):
        if hour < 0 and hour > 24:
            print('SetHour():hour over range')
        else:
            self.__hour = hour

    # for calories computing (per sport for user setting goals of calories)
    @property
    def basicConsumption(self):  # one activity
        basicconsumption = self.__caloriesperhour * self.__caloriesperhour()
        print(float(self.__caloriesperhour) + ' * ' + float(self.__caloriesPerHour()) + ' = ' + float(burnedCalories))
        return basicconsumption

    # for calories computing (per sport for user checking unit sport)
    @property
    def ConsumedInInterval(self):
        consumedininterval = self.__hour * self.__caloriesperhour()
        print(float(self.__hour) + ' * ' + float(self.__caloriesperhour()) + ' = ' + float(consumedininterval))
        return burnedCalories


