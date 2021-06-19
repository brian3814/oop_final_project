from collections import OrderedDict
from datetime import datetime


food_qrery = [
    {'name':'apple','carb':70,'protein':10,'fat':0.5},
    {'name':'banana','carb':90,'protein':2,'fat':0.1},
    {'name':'orange','carb':40,'protein':8,'fat':0},
    {'name':'burger','carb':60,'protein':20,'fat':10},
]

##########################################################################
############### Andy ####################################################
##########################################################################
class Food:
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
    def __init__(self, name, time=None, inTake=[],food_dict={}):
        self.name = str(name)
        self.__is_init = True
        self.inTake = inTake 
        self.time = time 
        self.totalCalories = None
        self.food_table = {food['name']:Food(name=food['name'],carb=food['carb'],protein=food['protein'],fat=food['fat']) for food in food_qrery}
        # self.food_table = food_dict
        
    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self,meal_time):
        if not isinstance(meal_time,datetime): raise Exception("meal time is not valid datetime")
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
    
    #可以吃 [Food,Food]、Food、['food','food']
    def add_food(self,new_food):
        if not self._is_food(new_food): 
            if isinstance(new_food,list) and all([True if food in self.food_table.keys() else False for food in new_food]):
                [self.__inTake.append(self.food_table[food]) for food in new_food]
                self._update_toallCalories()
            else: raise Exception("Passed in non-meal type")
        else:
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

    def food_summamry(self):
        return [{"food.name":food.name,"calories":food.calories} for food in self.__inTake]


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
        if not isinstance(i_date,datetime): raise Exception("Date is not valid date")
        if self.__is_init == False: raise Exception('You cannot change Date')
        self.__is_init = False
        self.__date = i_date

    @property
    def meals(self):
        return self.__meals

    @meals.setter
    def meals(self,i_meals):
        if i_meals == []: 
            if self.__is_init == False: raise Exception('You cannot empty the meal list, plz use empty_meals()')
            self.__meals = []
        else:
            if not (isinstance(i_meals,list) and self._is_meal(i_meals)): raise TypeError('The type of the input is not allowed')
            self.__meals = i_meals

    @property
    def total_intake_calories(self):
        return sum([meal.totalCalories for meal in self.meals])

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

    def meal_summary(self):
        return {i:{meal.name:meal.totalCalories} for i,meal in enumerate(self.__meals)}

    def meal_detail(self):
        return [{"meal_name":meal.name,'totalCalories':meal.totalCalories,'food':meal.food_summamry()} for i,meal in enumerate(self.__meals)]

