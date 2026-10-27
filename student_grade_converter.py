import bisect
def convert_grade(score):
    point = [64,84,100]
    categories = ['Fail','Acceptable','Good','Outstanding']
    result = bisect.bisect(point,score)
    return categories[result]

student_scores = {"John": 90,"Edy": 68,"Marry": 88, "Ewan": 79,"Park": 62,}
for name in student_scores:
    student_scores[name] = convert_grade(student_scores[name])
print(student_scores)
