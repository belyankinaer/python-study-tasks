student_scores = [10, 40, 33, 50, 15]

min_student_score = float('inf')
first_min_score = min_student_score
second_min_score = min_student_score
third_min_score = min_student_score

for student_score in student_scores:

    if student_score < first_min_score:
        third_min_score = second_min_score
        second_min_score = first_min_score
        first_min_score = student_score
    elif student_score < second_min_score:
        third_min_score = second_min_score
        second_min_score = student_score
    elif student_score < third_min_score:
        third_min_score = student_score

print(f"1: {first_min_score}")
print(f"2: {second_min_score}")
print(f"3: {third_min_score}")
