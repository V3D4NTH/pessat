import matplotlib.pyplot as plt
storage_file = open("answers.txt",'r')
srn = storage_file.readline()
answers = storage_file.readlines()
Reverse_Markers = [1,6,11,14,15]     #questions that have an ascending marking scheme
L=[True if x in Reverse_Markers else False for x in range(1,len(answers)+1)]
answers_zipped = list(zip(answers,L))
Attitude_questions = answers_zipped[:5]
Motivation_questions = answers_zipped[5:10]
Confidence_questions = answers_zipped[10:15]
Resilience_questions = answers_zipped[15:20]

def marks_awarded(questions):
    marks = 0
    for i in questions:
        if i[1] == False:
            if i[0] == "1\n":
                marks += 4
            elif i[0] == "2\n":
                marks += 3
            elif i[0] == "3\n":
                marks += 2
            elif i[0] == "4\n":
                marks += 1
        else:
            if i[0] == "1\n":
                marks += 1
            elif i[0] == "2\n":
                marks += 2
            elif i[0] =="3\n":
                marks += 3
            elif i[0] == "4\n":
                marks += 4
    return marks

def graph():
    Attitude_marks = marks_awarded(Attitude_questions)
    Motivation_marks = marks_awarded(Motivation_questions)
    Confidence_marks = marks_awarded(Confidence_questions)
    Resilience_marks = marks_awarded(Resilience_questions)
    left_coordinates=[1,2,3,4]
    heights=[Attitude_marks,Motivation_marks,Confidence_marks,Resilience_marks]
    bar_labels=["Attitude","Motivation","Confidence","Resilience"]
    plt.bar(left_coordinates,heights,tick_label=bar_labels,width=0.6,color=['light blue'])
    plt.xlabel('')
    plt.ylabel("Marks")
    plt.title("Aptitude Evaluation")
    plt.show()
storage_file.close()
