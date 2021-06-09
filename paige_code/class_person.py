class Person():

    def __init__(self, name, age, height, weight, gender, hobbies):
        #self.uuid = uuid
        self.name = name
        self.age = age
        self.height = height  # 公尺
        self.weight = weight  # 公斤
        self.gender = gender
        self.hobbies = hobbies

        self.bmi = round(weight / height**2, 2)

        self.bmi = None
        self.baseMetabolic = None

        self.eventList = []

        self.friendsList = []

        self.dailyLog = []

    def showInfo(self):
        print("User Info:")
        print("name: ", self.name)
        print("age: ", self.age)
        print("height: ", self.height)
        print("weight: ", self.weight)

    def FollowFriend(self, account):
        if not account in self.friendsList:
            self.friendsList.append(account)
            print("followed", account)
        return ({self.name: [self.age, self.height, self.weight, self.gender, self.bmi]}, self.eventList)

    def RemoveFriend(self, account):
        if account in self.friendsList:
            self.friendsList.remove(account)
            print("unfollowed ", account)

    def showFriendList(self):
        print("Your friend list: ", self.friendsList)
