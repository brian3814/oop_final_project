from datetime import datetime
from _class.person import *
from _class.Intake import *
from _class.Genre import *
from _class.Event import *

if __name__ == '__main__':
    sport_dict = 

    sport = Sport('Indoor', 'YogaSingle', 1, 'W40KG')
    print('Hi')


# class Sport:
#     # constructor
#     def __init__(self, genre, activity, hour, weight):
#         self.__genre = genre
#         self.__activity = activity
#         self.__hour = hour
#         self.__weight = weight

# GenreList = {'BowlingMorePeople': Indoor | Static | Interactive | isBALL,
#              'YogaMorePeople'   : Indoor | Static | Interactive | notBALL,
#              'BowlingSingle'    : Indoor | Static | Pearson | isBALL,
#              'YogaSingle'       : Indoor | Static | Pearson | notBALL,
#              'Badminton'        : Indoor | Dynamic | Interactive | isBALL,
#              'Dancing'          : Indoor | Dynamic | Interactive | notBALL,
#              'ShootingBaskets'  : Indoor | Dynamic | Pearson | isBALL,
#              'Trampoline'       : Indoor | Dynamic | Pearson | notBALL,
#              'GolfMorePeople'   : Outdoor | Static | Interactive | isBALL,
#              'TaiChiMorePeople' : Outdoor | Static | Interactive | notBALL,
#              'GolfSingle'       : Outdoor | Static | Pearson | isBALL,
#              'TaiChi'           : Outdoor | Static | Pearson | notBALL,
#              'Baseball'         : Outdoor | Dynamic | Interactive | isBALL,
#              'RunMorePeople'    : Outdoor | Dynamic | Interactive | notBALL,
#              'BasketballSingle' : Outdoor | Dynamic | Pearson | isBALL,
#              'RockClimbing'     : Outdoor | Dynamic | Pearson | notBALL
#             }