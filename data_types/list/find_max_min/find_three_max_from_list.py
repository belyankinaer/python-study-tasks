student_scores = [10, 40, 33, 50, 15]

max_student_score = float('-inf')
first_max_score = max_student_score
second_max_score = max_student_score
third_max_score = max_student_score

for student_score in student_scores:

    if student_score > first_max_score:
        third_max_score = second_max_score
        second_max_score = first_max_score
        first_max_score = student_score
    elif student_score > second_max_score:
        third_max_score = second_max_score
        second_max_score = student_score
    elif student_score > third_max_score:
        third_max_score = student_score

print(f"1: {first_max_score}")
print(f"2: {second_max_score}")
print(f"3: {third_max_score}")
