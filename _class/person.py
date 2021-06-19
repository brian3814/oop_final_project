from datetime import datetime
from dateutil.relativedelta import relativedelta
from _class.Event import *

class Account():
    def __init__(self, uuid, name, level):
        self.__uuid = uuid
        self.__name = name
        self.__level = level

    @property
    def uuid(self):
        return self.__uuid
    
    @uuid.setter
    def uuid(self,uuid):
        pass

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        pass

    @property
    def level(self):
        return self.__level
    
    @level.setter
    def level(self,level):
        pass


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

    def __init__(self, name, uuid, level, birthday, height, weight, gender, hobbies):
        super().__init__(uuid, name, level)
        #https://stackoverflow.com/questions/4436957/pythonic-difference-between-two-dates-in-years
        self.__age = relativedelta(datetime.now(), birthday).years
        self.__height = height  # cm
        self.__weight = weight  # kg
        self.__gender = gender
        self.__hobbies = hobbies

        # calculate bmi
        self.bmi = round(weight / (height/100)**2, 2)

        # calculate gmr
        gmr_table = {
                        'male':13.7 * weight + 5.0 * height - 6.8 * self.__age + 66,
                        'female':9.6 * weight + 3.8 * height - 4.7 * self.__age + 655,
                    }
        self.gmr = gmr_table[gender] if gmr_table.get(gender) else -1
        if self.gmr != -1:
            # print("基礎代謝率(大卡)：", self.gmr)
            pass
        else:
            Exception('{} is not in the allowed list [{}]'.format(gender,gmr_table.keys()))
        self.eventList = []  # stores hosted events & joined events
        self.friendsList = []
        self.__dailyIntakes = {}
        self.__dailyEvents = {}


    def showInfo(self):
        print("User Info:")
        print("name: ", self.name)
        print("age: ", self.__age)
        print("height: ", self.__height)
        print("weight: ", self.__weight)


    def update_dailyIntakes(self,inTakes):
        self.__dailyIntakes = inTakes

    def update_dailyEvents(self,events):
        self.__dailyEvents = events

    # ===============
    # calories
    def caloiesIntakeCal(self,start_d,end_d,i_format='%Y-%m-%d',t_format='%Y-%m-%d'):
        # __dailyIntakes = {'2020-10-10': Daily{date:,meals},}
        t_formats = t_format.split(t_format[2])
        index = [t_formats.index('%Y') if '%Y' in t_formats else None,t_formats.index('%m') if '%m' in t_formats else None,t_formats.index('%d') if '%d' in t_formats else None]
        if None in index: raise Exception('{} fails to contian %Y %m %d'.format(t_format))
        # datetime_string_type = '%Y-%m-%d
        start = datetime.strptime(start_d, i_format).strftime(t_format).split(t_format[2])
        end = datetime.strptime(end_d, i_format).strftime(t_format).split(t_format[2])

        between_dict = {}
        for date in self._Person__dailyIntakes.keys():
            year, mouth, day = date.split(t_format[2])
            if all([start[index[0]]<= year <=end[index[0]],start[index[1]]<= mouth <=end[index[1]],start[index[2]]<= day <=end[index[2]]]) == True:
                between_dict[date]=self._Person__dailyIntakes[date]
        
        result = sum([daily.total_intake_calories for __,daily in between_dict.items()])
        print('{} Intake {} Caloies from {} to {}'.format(self.name,result,start_d,end_d))
        return {'result':result,"dailyIntakes":between_dict}

    def caloiesConsumeCal(self,start_d,end_d,i_format='%Y-%m-%d',t_format='%Y-%m-%d'):
        # __dailyIntakes = {'2020-10-10': Daily{date:,meals},}
        t_formats = t_format.split(t_format[2])
        index = [t_formats.index('%Y') if '%Y' in t_formats else None,t_formats.index('%m') if '%m' in t_formats else None,t_formats.index('%d') if '%d' in t_formats else None]
        if None in index: raise Exception('{} fails to contian %Y %m %d'.format(t_format))
        # datetime_string_type = '%Y-%m-%d
        start = datetime.strptime(start_d, i_format).strftime(t_format).split(t_format[2])
        end = datetime.strptime(end_d, i_format).strftime(t_format).split(t_format[2])

        between_dict = {}
        for date in self._Person__dailyEvents.keys():
            year, mouth, day = date.split(t_format[2])
            if all([start[index[0]]<= year <=end[index[0]],start[index[1]]<= mouth <=end[index[1]],start[index[2]]<= day <=end[index[2]]]) == True:
                between_dict[date]=self._Person__dailyEvents[date]
        
        result = sum([daily.total_consume_calories for __,daily in between_dict.items()])
        print('{} Consume {} Caloies from {} to {}'.format(self.name,result,start_d,end_d))
        return {'result':result,"dailyEvents":between_dict}

    # ===============
    # friens follow & unfollow

    def FollowFriend(self, friend):
        if not friend in self.friendsList:
            self.friendsList.append(friend)
            print("followed", friend)

        return self.name

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
