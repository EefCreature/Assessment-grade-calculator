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
    return through_grade
    

    
grade = {
        "grade": [],
        "grade_total": [],
        "waiting": []
    }
grade_inp = []
while True:
    inp = input("grade: ")

    if  inp:
        inp = int(inp)
        if inp >= 0:
            grade_inp.append(inp)
            
        else:
            grade
            print(False)
    else:
        break
grade["grade"] = grade_inp

grade_inp = []

for i in range(len(grade["grade"])):
    inp = ""
    while inp == "" and coe(inp,int) < grade["grade"][i]:
        inp = input("grade total: ")
    inp = int(inp)   
    grade_inp.append(inp)
    

grade["grade_total"] = grade_inp

grade_inp = []
for i in range(len(grade["grade"])):
    inp = ""
    
    while inp == "" and coe(inp,float) < 100 :
        inp = input("waiting: ")
        
    inp = float(inp) / 100
    grade_inp.append(inp)
grade["waiting"] = grade_inp

print("-"*40)
print(round(grade_handling(grade) * 100))
