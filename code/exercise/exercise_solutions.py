max_points = 30


def show_possible_grades():
    print("possible grades")
    for x in range(1, 7):
        print("\t", x)


def calculate_grade(points):
    if points > max_points:
        print("the points can't be above the max_points of ", max_points)
        return
    your_grade = points / max_points * 5 + 1
    print("\nyour grade is: ", your_grade)
    if your_grade >= 4:
        print("well done")
    else:
        print("please learn more")


show_possible_grades()
calculate_grade(30)
