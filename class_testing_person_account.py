from datetime import datetime
from _class.person import *
from _class.Intake import *
from _class.Genre import *
from _class.Event import *

if __name__ == '__main__':
    UserEvent = Event()
    event = (('YogaMorePeople', 3), ('ShootingBaskets', 5))  # sport: time
    totalCalories = UserEvent.GetConsumedCalories(event)
    totalgenres = UserEvent.get_genre()
    print(totalCalories)
    print(totalgenres)

