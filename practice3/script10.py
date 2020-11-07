items = {"apple": 100, "banana": 200, "orange": 400}
for item_name in items:
  print("---------------------------------------------")
  item_price = str(items[item_name])
  print(item_name + "は1個" + item_price + "円です")

  input_count = input("購入する"+item_name+"の個数を入力してください：")

  print("購入する"+ item_name + "の個数は" + input_count + "個です")

  count = int(input_count)
  total_price = items[item_name] * count
  print("支払い金額は" + str(total_price) + "円です")
