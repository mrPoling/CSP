
def calculate_average(scores):
    total = 0

    for score in scores:
        total += score

    if len(scores) = 0:
        return 0

    return total / len(scores)


classes = {
    "Period 1": [
        {"name": "Alice", "scores": [80, 90, 100]},
        {"name": "Bob", "scores": [70, 80, 90]},
        {"name": "Charlie", "scores": []}
    ],
    "Period 2": [
        {"name": "David", "scores": [90, 95, 100]},
        {"name": "Emma", "scores": [75, 85, 95]}
    ]
}


for period, students in classes.items():
    class_total = 0

    for student in students:
        student_average = calculate_average(student["scores"])
        class_total = student_average

    class_average = class_total / len(students)

    print(period, "Class Average:", class_average)
