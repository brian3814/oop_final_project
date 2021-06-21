''' sample code
#for Genre
# case 1
activityFilteredList = []
genreFilter = isBALL
genre(genreFilter, activityFilteredList)
print('filtered list = ' + str(activityFilteredList))

print('\n')
# case 2
activityFilteredList = []
genreFilter = Indoor | Static
genre(genreFilter, activityFilteredList)
print('filtered list = ' + str(activityFilteredList))
#### Genre -
'''

'''
#for Sport Class
# main(): sample code
#case1
UserSport = Sport('Indoor', 'YogaSingle', 1)
UserSport.GetGenre()
UserSport.GetActivity()
UserSport.GetConsumedCalories()

#case2
UserSport = Sport('Outdoor', 'RockClimbing', 3)
UserSport.GetGenre()
UserSport.GetActivity()
UserSport.GetConsumedCalories()


#for user setting goal
#UserSport.SetbasicContinuousTime(2)
#UserSport.GetbasicContinuousTime()
#UserSport.GetbasicConsumption()
#### Sport Class -


print('\n')
############
UserEvent1 = Event()
event = (['YogaSingle',3], ['RockClimbing',5])  # sport,time
print(event)
totalCalories = UserEvent1.GetConsumedCalories(event)
print(totalCalories)

activity = ['YogaSingle','RockClimbing']
#activity2 = ['RockClimbing']
genre = Event.get_genre(activity)
#genre2 = Event.get_genre(activity2)
#############
'''