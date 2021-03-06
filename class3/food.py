from menu_item import MenuItem 

class Food(MenuItem):
  def info(self):
    return self.name + ': ¥' + str(self.price) + ' (' + str(self.calorie) + 'kcal)'

  def calorie_info(self):
    print(str(self.calorie) + 'kcalです')

  def __init__(self, name, price, calorie):
    super().__init__(name, price)
    self.calorie = calorie