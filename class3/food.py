from menu_item import MenuItem 

class Food(MenuItem):
  def calorie_info(self):
    print(str(self.calorie) + 'kcalです')