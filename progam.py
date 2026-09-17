"""
    Title: Grey calculator
    Description: I calculate what inputs your grade and it waiting that give you a result in telling you if you pass or failed
    Author: Ethan

"""

import guizero as gz


    
grade_dic = {
        "grade": [],
        "grade_total": [],
        "waiting": []
    }

grade_list = {
        "grade": [],
        "grade_total": [],
        "waiting": []
    }

grade_letter = {
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

def grade_calculation(grade: float,grade_total: float,waiting: float):
    """
    Performance the calculation of grade \n
    Total grade: cannot be greater than 0 \n
    weight: have to be less than 1 as usual enter for percentages

    """
    grade = float(grade)
    grade_total = float(grade_total)
    waiting = float(waiting)

    if grade > grade_total and grade != grade_total:
        gz.error(title="error",text=("Error grade is prot sed grade total" ))
        return 0
    # Cheques if grade_total is  isn't  0 As  cannot divide by zero
    if grade_total != 0:
        fraction_grade = grade / grade_total
    else:
        fraction_grade =0
    return fraction_grade * waiting


def grade_handling(grade_dic ):
    """
    Count up the total grade and give out the result and the grey letter\n
    The 1st result is grade 2nd result is the letter of the Great\n
    The input grade is a dictionary requiring {"grade", "grade_total", "waiting"}

    """
    through_grade = 0
    for i in range(len(grade_dic["grade"])):
        
        through_grade += grade_calculation(grade_dic["grade"][i],grade_dic["grade_total"][i],grade_dic["waiting"][i])
    #
    return through_grade, get_grade_letter(through_grade * 100)
    
def get_grade_letter(grade):
    
    resot = 0
    for i in grade_letter:
        # Checking if the curtain letter does not fit inside of the range so it can be updated to a better fit
        if grade >= grade_letter[i] and resot < grade_letter[i]:
            resot  = grade_letter[i]
            
    for i in grade_letter:
        #Fining printing out the letter
        if grade_letter[i] == resot:
            return(i)

"""
--------------------------------------------
UI development segment
--------------------------------------------
"""
def exit():
    """
    **Close down the app**
    """

    app.destroy()
    pass


def button_calculate():
    """
    Do the complete calculation
    """
    global grade_dic
    global grade_list
    
    grade_dic = {
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
                
                gz.error(title="error",text=("Error " + str(gr)+": "+ str(s)+" not a number" ))
                return
            if s < 0:
                gz.error(title="error",text=("Error " + str(gr)+": "+ str(s)+" cannot have a negative number" ))
                return
            
            grade_dic[gr].append(s)

    #Cheques if all of the weightings equals to 100 and Converts all the values into integers
    waiting_toll =0
    #Converts all the values into integers
    for i in range( len(grade_dic["waiting"])):
        if grade_dic["waiting"][i] != 0 :
            grade_dic["waiting"][i] /= 100
        waiting_toll +=grade_dic["waiting"][i]
    #Exit if it does not equal
    if waiting_toll != 1:
        gz.error(title="error",text=("Error wast is not eqill 100" ))
        return

    #Prints out the great
    grade_text.value = str("grade:" + "%"+ str( round(grade_handling(grade_dic)[0] * 100,2)))
    #Prints out the letter
    letter_text.value = str("letter:" + str( grade_handling(grade_dic)[1]))
    #Says if you pass or fail
    if  grade_handling(grade_dic)[0] * 100 >= 50:
        past_text.value = "Result: Pass"
    else:
        past_text.value = "Result: Failed "
        gz.info(text="Require grade to pass %" +str( round(50-grade_handling(grade_dic)[0]* 100,2) ) ,title="Pop up")
    
    
"""
Setting up other UI
"""
app = gz.App("s")

app.bg = "#083ED1"

#Curating all the grids and boxes
man_box = gz.Box(app,width="fill",border=True,layout="grid")
inpot_box = gz.Box(man_box,border=True,layout="grid",width="fill",height="fill",grid=[0, 0])
apit_box = gz.Box(man_box,border=False,layout="grid",width="fill",height="fill",grid=[0, 1],align="left")
bot_box = gz.Box(man_box,border=True,layout="grid",width="fill",height=100,grid=[0, 2],align="left",)

#Adding feels to the input
gz.Text(inpot_box,text="Marks  ",grid=[1, 0],  size=10)
gz.Text(inpot_box,text="Marks max",grid=[2, 0],  size=10)
gz.Text(inpot_box,text="Weight",grid=[3, 0],  size=10)

#Adding the result fields
grade_text =gz.Text(apit_box, width="fill", grid=[0, 0], text='grade: ---',align="left") 
letter_text =gz.Text(apit_box, width="fill", grid=[1, 0], text='letter: --',align="left") 
past_text = gz.Text(apit_box, width="fill", grid=[2, 0], text='Result: ------',align="left")

#Filling out all of the great fields by ittering through it
for i in range(4):
    text = str("Course:" + str(i+1))
    gz.Text(inpot_box, text=text, grid=[0, i+1], align="left", size=10)

    grade_list["grade"].append(gz.TextBox(inpot_box, width=5, grid=[1, i+1], text='0') )
    grade_list["grade_total"].append(gz.TextBox(inpot_box, width=5, grid=[2, i+1], text='0') )
    grade_list["waiting"].append(gz.TextBox(inpot_box, width=5, grid=[3, i+1], text='0') )

#Adding the Calculate button
submit_button = gz.PushButton(
    bot_box, text="Calculate",  grid=[0, 0], align='left',command=button_calculate, padx=5, pady=5)

#Adding the exit button
exit_button = gz.PushButton(
    bot_box, text="Exit", grid=[1, 0], align='right',command=exit, padx=5, pady=5)

app.display()



