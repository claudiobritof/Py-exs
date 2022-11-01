#Average grades (using defs)

from statistics import mean

infos_students = list()


def get_name():
    return input("Student grade: \n")


def get_grades(student_name):
    grades = list()
    counter = 1
    grades.append(student_name)
    while counter < 3:
        grade = int(input(f"{counter}ª grade: \n"))
        grades.append(grade)
        counter += 1
    infos_students.append(grades)
    return infos_students


def display_infos():
    return infos_students


while True:
    get_grades(get_name())
    question = input("Want to add another student? \n").lower()
    if question[0] == "n":
        # print(display_infos())
        break

def calculate_mean(students_infos):
    students_means = list()
    new_infos = list()  # bad naming

    for item in students_infos:
        students_means.append(item[0])
        students_means.append(mean(item[1:]))
        new_infos.append(students_means)
        del students_means
        students_means = list()

    return new_infos

def display_school_report():
    pass

print(calculate_mean(display_infos()))