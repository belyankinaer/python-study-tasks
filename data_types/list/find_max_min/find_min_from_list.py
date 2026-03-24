student_scores = [10, 40, 33, 50, 15]

min_student_score = float('inf')

for student_score in student_scores:
    if student_score < min_student_score:
        min_student_score = student_score

print(min_student_score)
