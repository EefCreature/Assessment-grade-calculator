

def grade_calculation(grade: int,grade_total: int,waiting: float):
    grade = int(grade)
    grade_total = int(grade_total)
    waiting = float(waiting)

    if waiting < 1 or waiting >= 0:
        print("Impossible result was entered", waiting )
        return 0

    fraction_grade = grade / grade_total
    return fraction_grade * waiting


print(grade_calculation(input("grade: "),input("grade total: "),input("waiting: ")))

