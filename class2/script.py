class MenuItem: 
  def info(self):
    print("メニューの名前と値段が表示されます")


menu_item1 = MenuItem()
menu_item1.name = "サンドイッチ"
menu_item1.price = 500

menu_item1.info()

menu_item2 = MenuItem()
menu_item2.name = 'チョコケーキ'
menu_item2.price = 400

menu_item2.info()
