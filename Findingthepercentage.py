if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    personal_score= student_marks[query_name]
    personal_mean= ((sum(personal_score))/(3))
    corrected_mean= f"{personal_mean:.2f}"
print(corrected_mean)
    