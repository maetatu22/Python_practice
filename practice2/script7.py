apple_price = 200
money = 1000

input_count = input("購入するりんごの個数を入力してください：")


count = int(input_count)
total_price = apple_price * count

print('購入するりんごの個数は' + str(count) + '個です')
print('支払い金額は' + str(total_price) + '円です')

if money > total_price:
  print("りんごを"+input_count+"個買いました")
  balance = money - total_price
  print("残金は"+str(balance)+"円です")
elif money == total_price:
  print("りんごを"+input_count+"個書いました")
  print("財布が空になりました")
elif money < total_price:
  print("お金が足りません")
  print("りんごを買えませんでした")