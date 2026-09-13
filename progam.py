import guizero as gz


grade_naer = {
    "A+": 90,
    "A": 85,
    "A-": 80,
    "B+": 75,
    "c": 60,
    "B-":65,
    "C+": 60,
    "B": 70,
    "C-": 50,
    "D": 45,
    "E": 0
}

def coe(vall,type:type):
    try:
        type(vall)
    except:
        return 0

    pass

def grade_calculation(grade: int,grade_total: int,waiting: float):
    grade = int(grade)
    grade_total = int(grade_total)
    waiting = float(waiting)

    if waiting > 1 or waiting <= 0:
        print("Impossible result was entered", waiting )
        return 0

    fraction_grade = grade / grade_total
    return fraction_grade * waiting


def grade_handling(grade):
    
    through_grade = 0
    for i in range(len(grade["grade"])):
        
        through_grade += grade_calculation(grade["grade"][i],grade["grade_total"][i],grade["waiting"][i])
    return through_grade, get_grade_naer(through_grade * 100)
    
def get_grade_naer(grade):
    resot = 0
    for i in grade_naer:
        
        if grade >= grade_naer[i] and resot < grade_naer[i]:
            
            resot  = grade_naer[i]
            
            #return i
    return(resot)


    
grade = {
        "grade": [],
        "grade_total": [],
        "waiting": []
    }

app = gz.App("s")




app.display()


print("-"*40)

print("Grade:",grade_handling(grade)[1],round(grade_handling(grade)[0] * 100))