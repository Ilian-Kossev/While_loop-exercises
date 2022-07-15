initial_money = float(input())
change_money = round(initial_money * 100)
current_number_of_coins = 0
final_number_of_coins = 0

while change_money != 0:
    if change_money >= 200:
        current_number_of_coins = change_money // 200
        final_number_of_coins += current_number_of_coins
        change_money %= 200
        continue
    elif 100 <= change_money < 200:
        current_number_of_coins = change_money // 100
        final_number_of_coins += current_number_of_coins
        change_money %= 100
        continue
    elif 50 <= change_money < 100:
        current_number_of_coins = change_money // 50
        final_number_of_coins += current_number_of_coins
        change_money %= 50
        continue
    elif 20 <= change_money < 50:
        current_number_of_coins = change_money // 20
        final_number_of_coins += current_number_of_coins
        change_money %= 20
        continue
    elif 10 <= change_money < 20:
        current_number_of_coins = change_money // 10
        final_number_of_coins += current_number_of_coins
        change_money %= 10
        continue
    elif 5 <= change_money < 10:
        current_number_of_coins = change_money // 5
        final_number_of_coins += current_number_of_coins
        change_money %= 5
        continue
    elif 2 <= change_money < 5:
        current_number_of_coins = change_money // 2
        final_number_of_coins += current_number_of_coins
        change_money %= 2
        continue
    elif change_money == 1:
        current_number_of_coins = change_money // 1
        final_number_of_coins += current_number_of_coins
        change_money %= 1
        continue
print(final_number_of_coins)
