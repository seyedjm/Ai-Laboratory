n = int(input())
students = []
for _ in range(n):
    name = input()
    score = float(input())
    students.append([name, score])


scores = sorted(set([score for name, score in students]))
second_lowest_score = scores[1]


second_lowest_students = sorted([name for name, score in students if score == second_lowest_score])


for student in second_lowest_students:
    print(student)
