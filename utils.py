from datetime import datetime

##########################################################################
############### Andy ####################################################
##########################################################################
class Food:
    def __init__(self,name,carb=None,protein=None,fat=None):
        # Consider matching the food api for ORM
        self.__is_init = True
        self.name = name
        self.__carb = None
        self.__protein = None
        self.__fat = None
        self.calories = None
        if not [x for x in (carb, protein, fat) if x is None]: self.set_composition(carb,protein,fat)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,input_name):
        if self.__is_init == False: raise Exception('You cannot change item name')
        self.__is_init = False
        self.__name = str(input_name)

    @property
    def calories(self):
        if self.__calories == None: raise Exception('Have not set the calories yet')
        return self.__calories

    @calories.setter
    def calories(self,i_calories):
        self.__calories = i_calories

    def get_composition(self):
        if bool([True for x in (self.__carb, self.__protein, self.__fat) if x is None]): 
            raise Exception('Have not set the composition yet')
        return {'carb':self.__carb,'protein':self.__protein,'fat':self.__fat}
 
    def set_composition(self,carb,protein,fat):
        if not [x for x in (carb, protein, fat) if x is None or (not isinstance(x,int) and not isinstance(x,float))]:
            self.__carb = carb
            self.__protein = protein
            self.__fat = fat
            self.__calories = float(carb*4 + protein*4 + fat*9)
    
class Meal:
    def __init__(self, name, time=None, inTake=[]):
        self.name = str(name)
        self.__is_init = True
        self.inTake = inTake 
        self.time = time 
        self.totalCalories = None
    
    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self,meal_time):
        if not isinstance(meal_time,datetime): raise Exception("meal time is not valid datetime")
        if self.__is_init == False: raise Exception('You cannot change meal time')
        self.__is_init = False
        self.__time = meal_time

    @property
    def inTake(self):
        return {i:food.name for i,food in enumerate(self.__inTake)}

    @inTake.setter
    def inTake(self,i_inTake):
        if i_inTake == []: 
            if self.__is_init == False: raise Exception('You cannot empty the inTake list, plz use empty_inTake()')
            self.__inTake = []
        else:
            if not (isinstance(i_inTake,list) and self._is_food(i_inTake)): raise TypeError('The type of the input is not allowed')
            self.__inTake = i_inTake
        self._update_toallCalories()

    @property
    def totalCalories(self):
        return self.__totalCalories

    @totalCalories.setter
    def totalCalories(self,__):
        if self.__is_init == True:
            self.__totalCalories = sum([food.calories for food in self.__inTake])
            self.__is_init == False

    @staticmethod
    def _is_food(input):
        if isinstance(input,list): return bool([True for food in input if isinstance(food,Food)])
        elif isinstance(input,Food): return True
        else: return False
    
    def add_food(self,new_food):
        if not self._is_food(new_food): raise Exception("Passed in non-meal type")
        if isinstance(new_food,list):
            [self.__inTake.append(food) for food in new_food]
        else: 
            self.__inTake.append(new_food)
        self._update_toallCalories()

    def remove_food(self,index):
        if not (isinstance(index,int) and index in range(len(self.__inTake))): IndexError("Index is not int or out of range")
        del self.__inTake[index]
        self._update_toallCalories()

    def empty_inTake(self):
        self.__is_init = True
        self.inTake = []

    def _update_toallCalories(self):
        self.__is_init == True
        self.__totalCalories = sum([food.calories for food in self.__inTake])
        self.__is_init == False

class DailyIntakeCalories:
    def __init__(self, date=None, meals=[]):
        self.__is_init = True
        self.meals = meals
        self.date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self,i_date):
        if not isinstance(i_date,datetime): raise Exception("Date is not valid date")
        if self.__is_init == False: raise Exception('You cannot change Date')
        self.__is_init = False
        self.__date = i_date

    @property
    def meals(self):
        return {i:{meal.name:meal.totalCalories} for i,meal in enumerate(self.__meals)}

    @meals.setter
    def meals(self,i_meals):
        if i_meals == []: 
            if self.__is_init == False: raise Exception('You cannot empty the meal list, plz use empty_meals()')
            self.__meals = []
        else:
            if not (isinstance(i_meals,list) and self._is_food(i_meals)): raise TypeError('The type of the input is not allowed')
            self.__meals = i_meals

    @property
    def total_intake_calories(self):
        _sum = 0.0
        for _ , meal in self.meals.items():
            _sum += sum([v for k,v in meal.items()])
        return _sum

    @staticmethod
    def _is_meal(input):
        if isinstance(input,list): return bool([True for meal in input if isinstance(meal,Meal)])
        elif isinstance(input,Meal): return True
        else: return False

    def add_meal(self,new_meal):
        if not self._is_meal(new_meal): raise Exception("Passed in non-meal type")
        if isinstance(new_meal,list):
            [self.__meals.append(meal) for meal in new_meal]
        else:
            self.__meals.append(new_meal)

    def remove_meal(self,index):
        if not (isinstance(index,int) and index in range(len(self.__meals))): IndexError("Index is not int or out of range")
        del self.__meals[index]

    def empty_inTake(self):
        self.__is_init = True
        self.__meals = []


##########################################################################
############### Paige ####################################################
##########################################################################
class Account():
    def __init__(self, uuid, name, level):
        self.uuid = uuid
        self.name = name
        self.level = level

class Person(Account):
    """
    Person can do:

    +follow friends
    +unfollow friends
    +check friend list

    +host events
    +check interested events by hobbies
    +check events friends going to
    +sign up events

    +check daily intake calories (search by date)
    +check daily consumed calories (search by date)

    """

    def __init__(self, name, uuid, level, age, height, weight, gender, hobbies):
        super().__init__(name, uuid, level)
        self.age = age
        self.height = height  # cm
        self.weight = weight  # kg
        self.gender = gender
        self.hobbies = hobbies

        # calculate bmi
        self.bmi = round(weight / (height/100)**2, 2)

        # calculate gmr
        if gender == '男':
            self.gmr = 13.7 * weight + 5.0 * height - 6.8 * age + 66
        elif gender == '女':
            self.gmr = 9.6 * weight + 3.8 * height - 4.7 * age + 655
        else:
            self.gmr = -1
        if self.gmr != -1:
            print("基礎代謝率(大卡)：", self.gmr)

        self.eventList = []  # stores hosted events & joined events
        self.friendsList = []
        self.dailyLog = []

    def showInfo(self):

        print("User Info:")
        print("name: ", self._name)
        print("age: ", self._age)
        print("height: ", self._height)
        print("weight: ", self._weight)

    # ===============
    # friens follow & unfollow

    def FollowFriend(self, friend):
        if not friend in self.friendsList:
            self.friendsList.append(friend)
            print("followed", friend)

        return self._name

    def RemoveFriend(self, friend):
        if friend in self.friendsList:
            self.friendsList.remove(friend)
            print("unfollowed ", friend)
        else:
            print('unale to unfollow')

    def requestFriendList(self):
        # 以uuid跟db拿取friend資訊
        pass

    def showFriendList(self):
        print("Your friend list: ", self.friendsList)


    # ===============
    # event

    def hostEvent(self):
        # connect db from here
        eventName = input("enter event name: ")
        location = input("enter event location: ")
        self.eventList.append
        print("Successfully hosted the event: ", eventName)
        return [eventName, location]

    def GetPotentialInterestEvent(self, hobbies):
        # make sure user will not find past events
        now = datetime.timestamp(datetime.now())
        if Event.timestamp >= now:
            print("Potential interested events: ", Event.eventlist)
        # consider getting event by tag 'hobbies'
        # consider getting data form database with time and hobbies
        return None

    def GetFriendGoingEvent(self, friend):
        print(friend, Person.showFriendList)
        return 0
        # consider getting data form database with uuid and eventList

    def SignUpEvent(self):
        # adding uuid into participant list
        Event.participants.append(self.uuid)
        # adding eventName into eventList
        self.eventList.append(Event.eventname)
        print('Signed up the event ', Event.eventname)


    # ===============
    # calories

    def CaloiesIntakeCal():
      # consider getting data form csv
      # return DailyIntakeCalories.total_intake_calories
      pass


    # ===============
##########################################################################
############### Julia ####################################################
##########################################################################
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

class Event:
    # constructor
    def __init__(self, uuid, eventname, host, location, date, eventtime, duration, minplayers, participants, participantsnum, genre, calories):
        self.__uuid = uuid
        self.__eventname = eventname
        self.__host = host
        self.__location = location
        self.__date = date #date的格式
        self.__eventtime = eventtime #time的格式
        self.__duration = duration #數字
        self.__minplayers = minplayers =0 #int
        self.__participants = [] #list
        self.__participantsnum = 0 #int,len[]
        self.__genre = genre #table,using list


        self.__calories = 0

    # API
    # for uuid setting & getting
    @property
    def Pearson(self):
        print('Pearson() = ' + seld.__uuid)
        return self.__uuid

    @Pearson.setter
    def Pearson(self, uuid):
        self.__uuid = uuid

    #for eventname setting & getting
    @property
    def EventName(self):
        print('EventName() = ' + self.__eventname)
        return self.__eventname

    @EventName.setter
    def EventName(self, eventname):
        self.__eventname = eventname

    # for host setting & getting
    @property
    def Host(self):
        print('Host() = ' + self.__host)
        return self.__host

    @Host.setter
    def Host(self, host):
        self.__host = host

    # for location setting & getting
    @property
    def Location(self):
        print('location() = ' + self.__location)
        return self.__location

    @Location.setter
    def Location(self, location):
        self.__location = location

    # for date setting & getting
    @property
    def Date(self):
        print('Date() = ' + self.__date)
        return self.__date

    @Date.setter
    def Date(self, host):
        self.__date = date

    # for date setting & getting
    @property
    def Eventtime(self):
        print('Eventtime() = ' + self.__eventtime)
        return self.__date

    @Eventtime.setter
    def Eventtime(self, host):
        self.__eventtime = eventtime

    # for minplayers setting & getting
    @property
    def Minplayers(self):
        print('Minplayers() = ' + int(self.__minplayers))
        return self.__minplayers

    @Minplayers.setter
    def Minplayers(self, minplayers):
        self.__minplayers = int(minplayers)

    # for participants setting / getting
    @property
    def Participants(self):
        print('Participants() : ' , + self.__participants)
        return self.__participants

    @Participants.setter
    def Participants(self, participants):
        self.__Participants = [participants]

    # for participantsnum setting / getting
    @property
    def ParticipantsNum(self):
        self.__participantsnum = len(participants)
        print('ParticipantsNum() : ', + len(participants))
        return self.__participantsnum

    @ParticipantsNum.setter
    def ParticipantsNum(self, participants):
        self.__participantsnum = len(participants)

    # for genre setting/ getting
    @property
    def ActivityGenre(self):
        print('ActivityGenre() =' + self__genre)
        return self.__genre

    @ActivityGenre.setter
    def ActivityGenre(self, genre):
        self.__genre = genre

    #for calories setting/ getting
    @property
    def Calories(self):
        print('Calories() =' + self__calories)
        return self.__calories

    @Calories.setter
    def Calories(self, calories):
        self.__calories = calories