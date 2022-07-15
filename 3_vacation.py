needed_money_for_trip = float(input())
available_money = float(input())
counter_spend = 0
total_counter_days = 0

while available_money < needed_money_for_trip:
    operation_type = input()
    new_sum = float(input())
    total_counter_days += 1
    if operation_type == "spend":
        counter_spend += 1
        available_money -= new_sum
        if available_money < 0:
            available_money = 0
        if counter_spend == 5:
            print(f"You can't save the money.")
            print(total_counter_days)
            break
    elif operation_type == "save":
        available_money += new_sum
        counter_spend = 0
if available_money >= needed_money_for_trip:
    print(f"You saved the money for {total_counter_days} days.")





