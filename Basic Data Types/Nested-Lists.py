# Given the names and grades for each student in a class of N students,
#  store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade,
#  order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Sort the students list based on scores
    students.sort(key=lambda x: x[1])

    # Find the second lowest grade
    second_lowest_grade = sorted(list(set([score for name, score in students])))[1]

    # Print the names of students with the second lowest grade
    for name, score in sorted(students):
        if score == second_lowest_grade:
            print(name)