unsatisfactory_grades = int(input())
problem_name = input()
last_problem_name = ""
total_grade = 0
counter_bad_grades = 0
total_counter = 0
average_score = 0
has_failed = True


while counter_bad_grades < unsatisfactory_grades:
    grade = int(input())
    counter_bad_grades += 1

