def print_hand(hand, name='ゲスト'):
    # 変数handsに、複数の文字列を要素に持つリストを代入
    hands = ["グー", "チョキ", "パー"]
    
    # リストhandsを用いて、選択した手が出力されるように書き換え
    print(name + 'は' + hands[hand] + 'を出しました')

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
# 「何を出しますか？（0: グー, 1: チョキ, 2: パー）」と出力
print("何を出しますか？（0: グー, 1: チョキ, 2: パー）")
player_hand = input("数字で入力してください：")




if player_name == '':
    
    print_hand(player_hand)
else:
    
    print_hand(int(player_hand), player_name)