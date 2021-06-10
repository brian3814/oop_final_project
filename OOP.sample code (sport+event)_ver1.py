''' for Class Sport
# main(): sample code
UserSport = Sport('Indoor', 'YOGA', 1, 'W40KG')
UserSport.GetActivity()

UserSport.SetHour(5)
UserSport.GetHour()

UserSport.SetWeight('W40KG')
UserSport.GetWeight()

tableCheck = UserSport.GetIndoorCaloriesTable()
print('\nIndoor array = ' + str(tableCheck[:]))

UserSport.SetOutdoor('Outdoor')
tableCheck = UserSport.GetOutdoorCaloriesTable()
print('\nOutdoor array = ' + str(tableCheck[:]))

print('\n');
UserSport.SetOutdoor('Indoor')
UserSport.SetActivity('BADMINTON')
UserSport.GetActivity()
UserSport.GetConsumedCalories()

UserSport.SetOutdoor('Outdoor')
UserSport.SetActivity('TENNIS')
UserSport.SetWeight('W60KG')
UserSport.GetConsumedCalories()
'''


#for class Event
# main(): sample code
#UserSport = Sport('Indoor', 'YOGA', 1, 'W40KG')
UserEvent = Event('Ryder', 'yoga1', 'Julia', 'Taipei', '2021-06-07', '10:00', '1hr', 0, [], 5, 'YOGA', 'Indoor')
#(username, eventname, host, location, date, time, duration, participantsnum, participants, minplayers,genre, outdoor)

#print(Schedule)
UserEvent.selectEvent(yoga1)
UserEvent.selectEvent(yoga2)

#UserEvent.deleteEvent(yoga2)
#print(Schedule)

# get event list
tmpList = UserEvent.getEventList()
#print(tmpList)
'''
# compute burned calories according to event list
totalCalories = 0;
for i in tmpList:
    UserSport.SetActivity(i.get('genre'))
    UserSport.SetHour(i.get('duration'))
    totalCalories += UserSport.GetConsumedCalories()
    print('\n' + str(i))
    print('totalCalories = ' + str(totalCalories))
'''
print('\n---- just for participants list test --------')
UserEvent2 = Event('Apple','yoga2', 'Luffy', 'New World', '2021-06-09', '10:00', '3hr', 0, [], 10, 'YOGA', 'Indoor')
UserEvent2.selectEvent(yoga2)
tmpList = UserEvent.getEventList()
print(tmpList)
tmpList = UserEvent2.getEventList()
print(tmpList)
####