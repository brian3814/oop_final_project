''' for Genre
# case 1
activityFilteredList = []
genreFilter = isBALL
genre(genreFilter, activityFilteredList)
print('filtered list = ' + str(activityFilteredList))

# case 2
activityFilteredList = []
genreFilter = Indoor | Static
genre(genreFilter, activityFilteredList)
print('filtered list = ' + str(activityFilteredList))
#### Genre -
'''


''' for Sport Class
# main(): sample code
UserSport = Sport('Indoor', 'YogaSingle', 1, 'W40KG')
UserSport.GetActivity()

UserSport.SetHour(5)
UserSport.GetHour()

UserSport.SetWeight('W40KG')
UserSport.GetWeight()

tableCheck = UserSport.GetCaloriesTable()
print('\narray = ' + str(tableCheck[:]))
print('\n');
#case1
UserSport.SetGenre('Indoor')
UserSport.SetActivity('Badminton')
UserSport.GetActivity()
UserSport.GetConsumedCalories()

#case2
UserSport.SetGenre('Outdoor')
UserSport.SetActivity('RockClimbing')
UserSport.GetActivity()
UserSport.SetWeight('W60KG')
UserSport.GetConsumedCalories()

#for user setting goal
UserSport.SetbasicContinuousTime(10)
UserSport.GetbasicContinuousTime()
UserSport.GetbasicConsumption()
#### Sport Class -
'''


'''for Event Class
#### main: user sample code +
UserEvent = Event()
event = {'YOGA': 3, 'GMY': 5}  # sport: time
totalCalories = UserEvent.GetConsumedCalories('W40KG', event)
print(totalCalories)
#### Event Class -
'''
