Students={
    "Ali":85,
    "Ahmad":72,
    "sara":90,
    "Ayesha":35,
    "usaman":40
}
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    elif marks >= 40:
        return "pass"
    else:
        return "fail"
for name, marks in Students.items():
    grade = calculate_grade(marks)
    print(f"Name:{name}, Marks:{marks}, Grade:{grade}")
def count_passedstudents(students_dict):
    count = 0
    for marks in students_dict.values():
        if marks >= 40:
            count += 1

    return count   