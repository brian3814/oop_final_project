import os,sys
import datetime


class Food():
    def __init__(self,name,carb=None,protein=None,fat=None):
        # Consider matching the food api for ORM
        self.__is_init = True
        self.name = name
        self.__carb = None
        self.__protein = None
        self.__fat = None
        self.calories = None
        if not [x for x in (carb, protein, fat) if x is None]: self.set_composition(carb,protein,fat)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,input_name):
        if self.__is_init == False: raise Exception('You cannot change item name')
        self.__is_init = False
        self.__name = str(input_name)

    @property
    def calories(self):
        if self.__calories == None: raise Exception('Have not set the calories yet')
        return self.__calories

    @calories.setter
    def calories(self,i_calories):
        self.__calories = i_calories

    def get_composition(self):
        if bool([True for x in (self.__carb, self.__protein, self.__fat) if x is None]): 
            raise Exception('Have not set the composition yet')
        return {'carb':self.__carb,'protein':self.__protein,'fat':self.__fat}
 
    def set_composition(self,carb,protein,fat):
        if not [x for x in (carb, protein, fat) if x is None or (not isinstance(x,int) and not isinstance(x,float))]:
            self.__carb = carb
            self.__protein = protein
            self.__fat = fat
            self.__calories = float(carb*4 + protein*4 + fat*9)
    
class Meal:
    def __init__(self, name, time=None, inTake=[]):
        self.name = str(name)
        self.__is_init = True
        self.inTake = inTake 
        self.time = time 
        self.totalCalories = None
    
    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self,meal_time):
        if not isinstance(meal_time,datetime.datetime): raise Exception("meal time is not valid datetime")
        if self.__is_init == False: raise Exception('You cannot change meal time')
        self.__is_init = False
        self.__time = meal_time

    @property
    def inTake(self):
        return {i:food.name for i,food in enumerate(self.__inTake)}

    @inTake.setter
    def inTake(self,i_inTake):
        if i_inTake == []: 
            if self.__is_init == False: raise Exception('You cannot empty the inTake list, plz use empty_inTake()')
            self.__inTake = []
        else:
            if not (isinstance(i_inTake,list) and self._is_food(i_inTake)): raise TypeError('The type of the input is not allowed')
            self.__inTake = i_inTake
        self._update_toallCalories()

    @property
    def totalCalories(self):
        return self.__totalCalories

    @totalCalories.setter
    def totalCalories(self,__):
        if self.__is_init == True:
            self.__totalCalories = sum([food.calories for food in self.__inTake])
            self.__is_init == False

    @staticmethod
    def _is_food(input):
        if isinstance(input,list): return bool([True for food in input if isinstance(food,Food)])
        elif isinstance(input,Food): return True
        else: return False
    
    def add_food(self,new_food):
        if not self._is_food(new_food): raise Exception("Passed in non-meal type")
        if isinstance(new_food,list):
            [self.__inTake.append(food) for food in new_food]
        else: 
            self.__inTake.append(new_food)
        self._update_toallCalories()

    def remove_food(self,index):
        if not (isinstance(index,int) and index in range(len(self.__inTake))): IndexError("Index is not int or out of range")
        del self.__inTake[index]
        self._update_toallCalories()

    def empty_inTake(self):
        self.__is_init = True
        self.inTake = []

    def _update_toallCalories(self):
        self.__is_init == True
        self.__totalCalories = sum([food.calories for food in self.__inTake])
        self.__is_init == False


class DailyIntakeCalories:
    def __init__(self, date=None, meals=[]):
        self.__is_init = True
        self.meals = meals
        self.date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self,i_date):
        if not isinstance(i_date,datetime.date): raise Exception("Date is not valid date")
        if self.__is_init == False: raise Exception('You cannot change Date')
        self.__is_init = False
        self.__date = i_date

    @property
    def meals(self):
        return {i:{meal.name:meal.totalCalories} for i,meal in enumerate(self.__meals)}

    @meals.setter
    def meals(self,i_meals):
        if i_meals == []: 
            if self.__is_init == False: raise Exception('You cannot empty the meal list, plz use empty_meals()')
            self.__meals = []
        else:
            if not (isinstance(i_meals,list) and self._is_food(i_meals)): raise TypeError('The type of the input is not allowed')
            self.__meals = i_meals

    @property
    def total_intake_calories(self):
        _sum = 0.0
        for _ , meal in self.meals.items():
            _sum += sum([v for k,v in meal.items()])
        return _sum

    @staticmethod
    def _is_meal(input):
        if isinstance(input,list): return bool([True for meal in input if isinstance(meal,Meal)])
        elif isinstance(input,Meal): return True
        else: return False

    def add_meal(self,new_meal):
        if not self._is_meal(new_meal): raise Exception("Passed in non-meal type")
        if isinstance(new_meal,list):
            [self.__meals.append(meal) for meal in new_meal]
        else:
            self.__meals.append(new_meal)

    def remove_meal(self,index):
        if not (isinstance(index,int) and index in range(len(self.__meals))): IndexError("Index is not int or out of range")
        del self.__meals[index]

    def empty_inTake(self):
        self.__is_init = True
        self.__meals = []



#===============
print("\n[[Food]]")
apple = Food('apple')
print(apple.name)
# print('apple {}'.format(apple.calories))  #Error
# apple.name = 'AAA'  # Error
# print(apple.get_composition()) # Error
apple.set_composition(1,2,3)
print(apple.get_composition())
print('apple {}'.format(apple.calories))

banana = Food('banana',2,3,4)
print('banana {}'.format(banana.calories))

#===============
print("\n[[Meal]]")
meal = Meal('Lunch',datetime.datetime.today())
print('meal {}'.format(meal.totalCalories))
meal.add_food(apple)
print('add food {}'.format(meal.totalCalories))
meal.add_food(banana)
print('add food {}'.format(meal.totalCalories))
meal.empty_inTake()
print('empty food {}'.format(meal.totalCalories))
meal.add_food([apple,banana])
print('add food {}'.format(meal.totalCalories))

meal2 = Meal('Diner',datetime.datetime.today(),[apple,apple,apple])
print('Diner {}'.format(meal2.totalCalories))

#===============
print("\n[[DailyIntakeCalories]]")
today = DailyIntakeCalories(datetime.date.today())
today.add_meal(meal)
print('add meal {}'.format(today.total_intake_calories))
today.add_meal(meal2)
print('add meal {}'.format(today.total_intake_calories))
today.empty_inTake()
print('empty meal {}'.format(today.total_intake_calories))

today.add_meal([meal,meal2])
print('meal {}'.format(today.total_intake_calories))

#===============
print('End')
