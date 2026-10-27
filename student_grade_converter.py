
student_scores = {"John": 90,"Edy": 68,"Marry": 88, "Ewan": 79,"Park": 62,}
for name in student_scores:
    student_scores[name] = convert_grade(student_scores[name])
print(student_scores)
