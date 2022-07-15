sum_steps = 0
additional_steps = 0
while sum_steps < 10000:
    command = input()
    if command == "Going home":
        additional_steps = int(input())
        break
    else:
        number_steps = int(command)
        sum_steps += number_steps
final_number_steps = sum_steps + additional_steps
if final_number_steps >= 10000:
    steps_over_goal = final_number_steps - 10000
    print(f"Goal reached! Good job!")
    print(f"{steps_over_goal} steps over the goal!")
else:
    steps_below_goal = 10000 - final_number_steps
    print(f"{steps_below_goal} more steps to reach goal.")

