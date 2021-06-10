#### Event class +
import datetime
import time
import calendar

# <1> 用各event直接區分,如下
yoga1 = {
    'genre': 'YOGA',
    'eventName': 'Yoga1',
    'host': 'Julia',
    'location': 'Taipei',
    'date': '2021-6-7',
    'time': '10:00',
    'duration': 1,
    'minPlayers': 5,
    'participantsNum': 0,
    'participants': [],
    'isOutdoor': 'indoor',
}
yoga2 = {
    'genre': 'YOGA',
    'eventName': 'Yoga2',
    'host': ' Luffy',
    'location': 'New World',
    'date': '2021-6-9',
    'time': '10:00',  # time 10:00~12:00
    'duration': 3,
    'minPlayers': 10,
    'participantsNum': 0,
    'participants': [],
    'isOutdoor': 'indoor',
}

yoga3 = {
    'genre': 'YOGA',
    'eventName': 'Yoga3',
    'host': ' Robin',
    'location': 'New Flower World',
    'date': '2021-6-9',
    'time': '10:00',  # time 10:00~12:00
    'duration': 3,
    'minPlayers': 10,
    'participantsNum': 0,
    'participants': [],
    'isOutdoor': 'indoor',
}
tennis1 = {
    'genre': 'TENNIS',
    'eventName': 'Tennis1',
    'host': ' Robin',
    'location': 'New Flower World',
    'date': '2021-6-9',
    'time': '10:00',  # time 10:00~12:00
    'duration': 3,
    'minPlayers': 10,
    'participantsNum': 0,
    'participants': [],
    'isOutdoor': 'indoor',
}
tennis2 = {
    'genre': 'TENNIS',
    'eventName': 'Tennis2',
    'host': ' Rex',
    'location': 'Hsinchu',
    'date': '2021-6-9',
    'time': '10:00',  # time 10:00~12:00
    'duration': 3,
    'minPlayers': 5,
    'participantsNum': 0,
    'participants': [],
    'isOutdoor': 'indoor',
}

Schedule = []  # initialize


# <2>build class
class Event:
    # constructor (variables)
    def __init__(self, username, eventname, host, location, date, time, duration, participantsnum, participants, minplayers,
                 genre, outdoor):
        self.__username = username
        self.__eventname = eventname
        self.__host = host
        self.__location = location
        self.__date = date
        self.__time = time
        self.__duration = duration
        self.__participantsnum = participantsnum
        self.__participants = participants
        self.__minplayers = minplayers
        self.__genre = genre
        self.__isOutdoor = outdoor

    # API
    def setUserName(self, username):
        self.__username = username

    # for eventname
    def Seteventname(self, eventname):
        self.__eventname = eventname

    def Geteventname(self):
        print('Geteventname () = ' + self.__eventname)
        return self.__eventname

    # for host
    def Sethost(self, host):
        self.__host = host

    def Gethost(self):
        print('Gethost () = ' + self.__host)
        return self.__host

    # for location
    def Setlocation(self, location):
        self.__location = location

    def Getlocation(self):
        print('Getlocation () = ' + self.__location)
        return self.__location

    # for date
    def Setdate(self, date):
        self.__date = date

    def Getdate(self):
        print('Getdate () = ' + self.__date)
        return self.__date

    # for time
    def Settime(self, time):
        self.__time = time

    def Gettime(self):
        print('Gettime () = ' + self.__time)
        return self.__time

    # for totalduration
    def Setduration(self, duration):
        self.__duration = duration

    def Getduration(self):
        print('Getduration () = ' + self.__duration)
        return self.__duration

    # for participantsnum #Need it?
    def SetparticipantsNum(self, participantsnum):
        self.__participantsnum = participantsnum

    def GetparticipantsNum(self):
        print('GetparticipantsNum () = ' + self.__participantsnum)
        return self.__participantsnum

    # for participants
    def Setparticipants(self, participants):
        self.__participants = participants

    def Getparticipants(self):
        print('Getparticipants () = ' + self.__participants)
        return self.__participants

    # for minplayers
    def Setminplayers(self, minplayers):
        self.__minplayers = minplayers

    def Getminplayers(self):
        print('Getminplayers () = ' + self.__minplayers)
        return self.__minplayers

    # for genre
    def Setgenre(self, genre):
        self.__genre = genre

    def Getgenre(self):
        print('Getgenre () = ' + self.__genre)
        return self.__genre

    # for outdoor
    def SetOutdoor(self, outdoor):
        self.__isOutdoor = outdoor

    def GetOutdoor(self):
        print('GetOutdoor () = ' + self.__isOutdoor)
        return self.__isOutdoor

    #從event看有誰參加
    def selectEvent(self, eventName):
        # append event to event list
        Schedule.append(eventName)
        # append user name to participant list
        tmpNameList = eventName.get('participants')
        tmpNameList.append(self.__username)
        # print('name list = ' + str(tmpNameList))
        # increase participant number
        # peopleNum = eventName['participantNum']
        # print(yoga1[genre])
        # print(peopleNum)
        # eventName.set('participantNum') = eventName.get('participantNum') + 1

    def deleteEvent(self, eventName):
        Schedule.remove(eventName)
        tmpNameList = eventName.get('participants')
        tmpNameList.remove(self.__username)

    def getEventList(self):
        return Schedule



