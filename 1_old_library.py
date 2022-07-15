needed_book = input()
counter = 0
command = input()
while command != "No More Books":
    if command == needed_book:
        print(f"You checked {counter} books and found it.")
        break
    counter += 1
    command = input()
if command == "No More Books":
    print(f"You checked {counter} books.")
    print(f"The book you search is not here!")


