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
GenreList = {'BowlingMorePeople': Indoor | Static | Interactive | isBALL,
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
#print(GenreList)


def genre(genreFilter, filteredList):
    tmpActivity = list(GenreList.keys()) #Activity=sport
    tmpGenreList = list(GenreList.values())

    for index in range(len(GenreList)):
        if (tmpGenreList[index] & genreFilter == genreFilter):
            filteredList.append(tmpActivity[index])
            #print('filtered list = ' + str(filteredList))


