student_scores = [10, 40, 33, 50, 15]

max_student_score = float('-inf')

for student_score in student_scores:
    if student_score > max_student_score:
        max_student_score = student_score

print(max_student_score)
