unsatisfactory_grades = int(input())
problem_name = input()
last_problem_name = ""
total_grade = 0
counter_bad_grades = 0
total_counter = 0
average_score = 0
while problem_name != "Enough":
    last_problem_name = problem_name
    condition = True
    grade = int(input())
    total_grade += grade
    total_counter += 1
    average_score = total_grade / total_counter
    if grade <= 4:
        counter_bad_grades += 1
        if counter_bad_grades == unsatisfactory_grades:
            print(f"You need a break, {unsatisfactory_grades} poor grades.")
            break
    problem_name = input()
if problem_name == "Enough":
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {total_counter}")
    print(f"Last problem: {last_problem_name}")



