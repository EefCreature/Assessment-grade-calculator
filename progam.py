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
    for i in grade_naer:
        if grade_naer[i] == resot:
            return(i)



    
grade = {
        "grade": [],
        "grade_total": [],
        "waiting": []
    }

grade_list = {
        "grade": [],
        "grade_total": [],
        "waiting": []
    }

def cale():
    global grade
   
    
    grade = {
        "grade": [],
        "grade_total": [],
        "waiting": []
    }
    for gr in grade_list:
        for i in grade_list[gr]:
            
            s = i.value
            try :
                s = float(s)
            except:
                print(False)
                return
            grade[gr].append(s)
    
    print("-"*40)
    print("Grade:",grade_handling(grade)[1],round(grade_handling(grade)[0] * 100))



app = gz.App("s")

man_box = gz.Box(app,width="fill",border=True,layout="grid")
inpot_box = gz.Box(man_box,border=True,layout="grid",width="fill",height="fill",grid=[0, 0])
bot_box = gz.Box(man_box,border=True,layout="grid",width="fill",height=100,grid=[0, 1],align="left")

gz.Text(inpot_box,text="Marks  ",grid=[1, 0],  size=10)
gz.Text(inpot_box,text="Marks max",grid=[2, 0],  size=10)
gz.Text(inpot_box,text="Weight",grid=[3, 0],  size=10)



for i in range(4):
    text = str("Course:" + str(i+1))
    gz.Text(inpot_box, text=text, grid=[0, i+1], align="left", size=10)

    grade_list["grade"].append(gz.TextBox(inpot_box, width=5, grid=[1, i+1], text='0') )
    grade_list["grade_total"].append(gz.TextBox(inpot_box, width=5, grid=[2, i+1], text='0') )
    grade_list["waiting"].append(gz.TextBox(inpot_box, width=5, grid=[3, i+1], text='0') )


submitPushButton = gz.PushButton(
    bot_box, text="Calculate",  grid=[0, 0], align='left',command=cale, padx=5, pady=5)
exitPushButton = gz.PushButton(
    bot_box, text="Exit", grid=[1, 0], align='right', padx=5, pady=5)

app.display()



