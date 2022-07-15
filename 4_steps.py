command = input()
sum_steps = 0
while command != "Going home":
    number_steps = int(command)
    sum_steps += number_steps
    if sum_steps >= 10000:
        steps_over_goal = sum_steps - 10000
        print(f"Goal reached! Good job!")
        print(f"{steps_over_goal} steps over the goal!")
        break
    command = input()
if command == "Going home":
    command = input()
    number_steps = int(command)
    sum_steps += number_steps
    if sum_steps >= 10000:
        steps_over_goal = sum_steps - 10000
        print(f"Goal reached! Good job!")
        print(f"{steps_over_goal} steps over the goal!")
    else:
        steps_below_goal = 10000 - sum_steps
        print(f"{steps_below_goal} more steps to reach goal.")

