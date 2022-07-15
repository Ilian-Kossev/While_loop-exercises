needed_money = float(input())
available_money = float(input())
total_counter = 0
counter_spend = 0
while counter_spend < 5:
    action = input()
    new_sum = float(input())
    total_counter += 1
    if action == "spend":
        available_money -= new_sum
        counter_spend += 1
        if available_money < 0:
            available_money = 0
    if action == "save":
        available_money += new_sum
        counter_spend = 0
    if available_money >= needed_money:
        print(f"You saved the money for {total_counter} days.")
        break
if counter_spend == 5:
    print(f"You can't save the money.")
    print(total_counter)


