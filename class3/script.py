from food import Food 
from drink import Drink

food1 = Food("サンドイッチ", 500)
print(food1.info())

drink1 = Drink("コーヒー", 300)
print(drink1.info())

food1.calorie = 330
food1.calorie_info()