def print_hand(hand, name="ゲスト"):
  print(name + "は" + hand + "を出しました")

print("じゃんけんをはじめます")

player_name = input("名前を入力してください：")

if player_name == "":
  print_hand("グー")
else: 
  print_hand("グー", player_name)