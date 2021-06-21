#### Genre +
#Genretype:
notBALL = 0b00000001
isBALL = 0b00000010
Pearson = 0b00000100
Interactive = 0b00001000
Dynamic = 0b00010000
Static = 0b00100000
Outdoor = 0b01000000
Indoor = 0b10000000
#print(isBALL)

#activity=GenreList
GenreList = {'BowlingMorePeople': Indoor | Static | Interactive | isBALL,      #170
             'YogaMorePeople'   : Indoor | Static | Interactive | notBALL,     #169
             'BowlingSingle'    : Indoor | Static | Pearson | isBALL,          #166
             'YogaSingle'       : Indoor | Static | Pearson | notBALL,         #165
             'Badminton'        : Indoor | Dynamic | Interactive | isBALL,     #154
             'Dancing'          : Indoor | Dynamic | Interactive | notBALL,    #153
             'ShootingBaskets'  : Indoor | Dynamic | Pearson | isBALL,         #150
             'Trampoline'       : Indoor | Dynamic | Pearson | notBALL,        #149
             'GolfMorePeople'   : Outdoor | Static | Interactive | isBALL,     #106
             'TaiChiMorePeople' : Outdoor | Static | Interactive | notBALL,    #105
             'GolfSingle'       : Outdoor | Static | Pearson | isBALL,         #102
             'TaiChi'           : Outdoor | Static | Pearson | notBALL,        #101
             'Baseball'         : Outdoor | Dynamic | Interactive | isBALL,    #90
             'RunMorePeople'    : Outdoor | Dynamic | Interactive | notBALL,   #89
             'BasketballSingle' : Outdoor | Dynamic | Pearson | isBALL,        #86
             'RockClimbing'     : Outdoor | Dynamic | Pearson | notBALL        #85
            }
#print(GenreList)


def genre(genreFilter, filteredList):
    tmpActivity = list(GenreList.keys()) #Activity=sport
    tmpGenreList = list(GenreList.values())
    #print(tmpActivity)
    #print(tmpGenreList)

    for index in range(len(GenreList)):
        if (tmpGenreList[index] & genreFilter == genreFilter):
            print(tmpGenreList[index])
            print(genreFilter)
            filteredList.append(tmpActivity[index])
            #print('filtered list = ' + str(filteredList))
            
'''
#sample code
#for Genre
# case 1
activityFilteredList = []
genreFilter = isBALL
genre(genreFilter, activityFilteredList)
#print('filtered list = ' + str(activityFilteredList))
'''
print('\n')
# case 2
activityFilteredList = []
genreFilter = Indoor | Static
genre(genreFilter, activityFilteredList)
#print('filtered list = ' + str(activityFilteredList))
#### Genre -

