from datetime import datetime


class Account():
    def __init__(self, uuid, name, level):
        self.uuid = uuid
        self.name = name
        self.level = level


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


class Person(Account):

    def __init__(self, name=None, uuid=None, level=None, age=None, height=None, weight=None, gender=None, hobbies=None):
        super().__init__(name, uuid, level)
        self.age = age
        self.height = height  # cm
        self.weight = weight  # kg
        self.gender = gender
        self.hobbies = hobbies

        # calculate bmi
        self.bmi = round(weight / (height/100)**2, 2) if weight!= None and height!=None else None

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
        print("name: ", self.name)
        print("age: ", self.age)
        print("height: ", self.height)
        print("weight: ", self.weight)

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
# calories

    def CaloiesIntakeCal():
      # consider getting data form csv
      # return DailyIntakeCalories.total_intake_calories
      pass


        # ===============
paige = Person('Paige', 0, 'premium', 25, 1.62, 54, 'female', 'yoga')
paige.showInfo()
paige.FollowFriend('julia')
paige.showFriendList()
paige.RemoveFriend('Julia')
