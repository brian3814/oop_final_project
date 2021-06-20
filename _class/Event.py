from datetime import datetime
#### Sport class +
caloriesTable = {'BowlingMorePeople':149,
            'YogaMorePeople':124,
            'BowlingSingle':149,
            'YogaSingle':124,
            'Badminton':224,
            'Dancing':238,
            'ShootingBaskets':224,
            'Trampoline':174,
            'GolfMorePeople' :224,
            'TaiChiMorePeople':199,
            'GolfSingle':224,
            'TaiChi':199,
            'Baseball':249,
            'RunMorePeople' :398,
            'BasketballSingle':398,
            'RockClimbing':547,
            'ActivityEND': 0,
            }

notBALL = 0b00000001  #1
isBALL = 0b00000010  #2
Pearson = 0b00000100  #4
Interactive = 0b00001000 #8
Dynamic = 0b00010000 #16
Static = 0b00100000 #32
Outdoor = 0b01000000 #64
Indoor = 0b10000000 #124

genreList = {'BowlingMorePeople': Indoor | Static | Interactive | isBALL,
             'YogaMorePeople'   : Indoor | Static | Interactive | notBALL,
             'BowlingSingle'    : Indoor | Static | Pearson | isBALL,
             'YogaSingle'       : Indoor | Static | Pearson | notBALL,
             'Badminton'        : Indoor | Dynamic | Interactive | isBALL,
             'Dancing'          : Indoor | Dynamic | Interactive | notBALL,
             'ShootingBaskets'  : Indoor | Dynamic | Pearson | isBALL,
             'Trampoline'       : Indoor | Dynamic | Pearson | notBALL,
             'GolfMorePeople'   : Outdoor | Static | Interactive | isBALL,
             'TaiChiMorePeople' : Outdoor | Static | Interactive | notBALL,
             'GolfSingle'       : Outdoor | Static | Pearson | isBALL,
             'TaiChi'           : Outdoor | Static | Pearson | notBALL,
             'Baseball'         : Outdoor | Dynamic | Interactive | isBALL,
             'RunMorePeople'    : Outdoor | Dynamic | Interactive | notBALL,
             'BasketballSingle' : Outdoor | Dynamic | Pearson | isBALL,
             'RockClimbing'     : Outdoor | Dynamic | Pearson | notBALL
            }

GenreTuples = (
    ('Indoor',Indoor,),
    ('Outdoor',Outdoor,), 
    ('Static',Static,),
    ('Dynamic',Dynamic,),
    ('Interactive',Interactive,), 
    ('Pearson',Pearson,),
    ('isBALL',isBALL,),
    ('notBALL',notBALL,)
    )

class Sport:
    # constructor
    def __init__(self, genre, activity, hour):
        self.__genre = genre
        self.__activity = activity
        self.__hour = hour

        self.basiccontinuoustime = 0
        self.carlories = 0

    # APIs
    def __getCaloriesPerHour(self):
        return caloriesTable[self.__activity]

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

    # for calories tables getting
    def GetCaloriesTable(self):
        return CaloriesTable

    # for calories computing, ConsumedInInterval for Event 計算用
    def GetConsumedCalories(self):
        burnedCalories = self.__hour * self.__getCaloriesPerHour()
        # print(str(self.__hour) + ' * ' + str(self.__getCaloriesPerHour()) + ' = ' + str(burnedCalories))
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
        # print(str(self.basiccontinuoustime) + ' * ' + str(self.__getCaloriesPerHour()) + ' = ' + str(basicconsumption))
        return basicconsumption



class Event:
    # constructor (variables)
    def __init__(self):
        self.__sport = Sport('Indoor', 'YogaSingle', 1)  # 引用class Sport &初始化
        self.__activityList = []
        self.__timeList = []  # dulluration
        self.__totalCalories = 0
        return

    # API
    # for calories computing
    def GetConsumedCalories(self, event):  # event=sport set
        # print(event)

        self.__activityList,self.__timeList = zip(*event)

        for index in range(len(tuple(event))):
            # print(' ---- ' + str(index))
            # print(self.__activityList[index])
            self.__sport.SetActivity(self.__activityList[index])  # 引入Class Sport裡面的SetActivity

            # print(self.__timeList[index])
            self.__sport.SetHour(self.__timeList[index])  # 引入Class Sport裡面的SetHour

            self.__totalCalories += self.__sport.GetConsumedCalories()
        return self.__totalCalories
    
    def get_genre(self):
        resurt = []
        genreStrList, recoverlist = zip(*GenreTuples)
        for activity in self.__activityList:
            genre_d = genreList[activity]
            for index in range(len(recoverlist)):
                if genre_d > recoverlist[index]:
                    genre_d = genre_d - recoverlist[index]
                    if genreStrList[index] not in resurt:
                        resurt.append(genreStrList[index])
        return resurt

#### Event class -


class DailyConsumeCalories:
    def __init__(self, date=None, events=[]):
        self.events = events
        self.date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self,i_date):
        if not isinstance(i_date,datetime): raise Exception("Date is not valid date")
        self.__date = i_date

    @property
    def events(self):
        return self.__events

    @events.setter
    def events(self,i_events):
            self.__events = i_events

    @property
    def total_consume_calories(self):
        return sum([event['totalCalories'] for event in self.events])

    def add_event(self,new_event):
        if isinstance(new_event,list):
            [self.__events.append(event) for event in new_event]
        else:
            self.__events.append(new_event)

    def remove_event(self,index):
        if not (isinstance(index,int) and index in range(len(self.__events))): IndexError("Index is not int or out of range")
        del self.__events[index]

    def empty_inTake(self):
        self.__is_init = True
        self.__events = []

    def event_summary(self):
        totalCalories = 0
        result={}
        for i,event in enumerate(self.events):
            result[i]={'totalCalories':event['totalCalories'],'sports':event['sports']}
            totalCalories += event['totalCalories']
        print('totalCalories: {}'.format(totalCalories))
        return result

    # def event_detail(self):
    #     return [{"event_name":meal.name,'totalCalories':meal.totalCalories,'food':meal.food_summamry()} for i,meal in enumerate(self.__events)]
