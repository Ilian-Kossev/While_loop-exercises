sum = float(input())
sum = int(sum * 100)
counter = 0
while sum > 0:
    counter += 1
    if sum - 200 >= 0:
        sum -= 200
        continue
    elif sum - 100 >= 0:
        sum -= 100
        continue
    elif sum - 50 >= 0:
        sum -= 50
        continue
    elif sum - 20 >= 0:
        sum -= 20
        continue
    elif sum - 10 >= 0:
        sum -= 10
        continue
    elif sum - 5 >= 0:
        sum -= 5
        continue
    elif sum - 2 >= 0:
        sum -= 2
        continue
    else:
        sum -= 1
print(counter)
