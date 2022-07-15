initial_money = float(input())
change_money = round(initial_money * 100)
current_number_of_coins = 0
final_number_of_coins = 0

if change_money >= 200:
    current_number_of_coins = change_money // 200
    final_number_of_coins += current_number_of_coins
    change_money %= 200

if 100 <= change_money < 200:
    current_number_of_coins = change_money // 100
    final_number_of_coins += current_number_of_coins
    change_money %= 100

if 50 <= change_money < 100:
    current_number_of_coins = change_money // 50
    final_number_of_coins += current_number_of_coins
    change_money %= 50

if 20 <= change_money < 50:
    current_number_of_coins = change_money // 20
    final_number_of_coins += current_number_of_coins
    change_money %= 20

if 10 <= change_money < 20:
    current_number_of_coins = change_money // 10
    final_number_of_coins += current_number_of_coins
    change_money %= 10

if 5 <= change_money < 10:
    current_number_of_coins = change_money // 5
    final_number_of_coins += current_number_of_coins
    change_money %= 5

if 2 <= change_money < 5:
    current_number_of_coins = change_money // 2
    final_number_of_coins += current_number_of_coins
    change_money %= 2

if change_money == 1:
    current_number_of_coins = change_money // 1
    final_number_of_coins += current_number_of_coins
    change_money %= 1

print(final_number_of_coins)
