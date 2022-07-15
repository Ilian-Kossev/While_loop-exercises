sum = float(input())
sum = int(sum * 100)
counter = 0
counter += sum // 200
sum %= 200
counter += sum // 100
sum %= 100
counter += sum // 50
sum %= 50
counter += sum // 20
sum %= 20
counter += sum // 10
sum %= 10
counter += sum // 5
sum %= 5
counter += sum // 2
sum %= 2
if sum == 1:
    counter += 1
print(counter)