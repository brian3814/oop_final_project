# <1> 用各event直接區分,如下
event1 = {
    'Pearson': 'UUID1',
    'EventName': 'YOGA + TENNIS', #string
    'Host': 'Julia',
    'Location': 'Taipei', #string
    'Date': '2021-6-7', #date
    'EventTime': '10:00', #time
    'TotalDuration': 3, #float, 0 <duration <24
    'MinPlayers': 5, #int 1<=minplayers
    'Participants': [],#list
    'ParticipantsNum': 0, #int -, sum
    'ActivityGenre': 'indoor & static + outdoor & dynamic', #indoor /static #string & table
}

event2 = {
    'Pearson': 'UUID2',
    'EventName': 'Wii + TENNIS + RUN',
    'Host': 'Paige',
    'Location': 'New Flower World',
    'Date': '2021-6-9',
    'EventTime': '10:00',
    'TotalDuration': 7,
    'MinPlayers': 10,
    'Participants': [],
    'ParticipantsNum': 0,
    'ActivityGenre': 'indoor & dynamic + outdoor & dynamic' + 'outdoor & dynamic',
}

import datetime
import time

class Event:
    # constructor
    def__init__(self, uuid, eventname, host, location, date, eventtime, duration, minplayers, participants, participantsnum, genre, calories)
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

    #API
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







