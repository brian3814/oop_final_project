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
UserSport = Sport('Indoor', 'YOGA', 1, 'W40KG')
UserSport.GetActivity()

UserSport.SetHour(5)
UserSport.GetHour()

UserSport.SetWeight('W40KG')
UserSport.GetWeight()

tableCheck = UserSport.GetCaloriesTable()
print('\narray = ' + str(tableCheck[:]))

#UserSport.SetOutdoor('Outdoor')
#tableCheck = UserSport.GetOutdoorCaloriesTable()
#print('\nOutdoor array = ' + str(tableCheck[:]))

print('\n');
UserSport.SetGenre('Indoor')
UserSport.SetActivity('BADMINTON')
UserSport.GetActivity()
UserSport.GetConsumedCalories()

UserSport.SetGenre('Outdoor')
UserSport.SetActivity('TENNIS')
UserSport.SetWeight('W60KG')
UserSport.GetConsumedCalories()
#### Sport class -
'''


'''for Event Class
event = {'YOGA': 3, 'GMY': 5}  # sport: time
totalCalories = UserEvent.GetConsumedCalories('W40KG', event)
print(totalCalories)
#### main: user sample code -
'''
