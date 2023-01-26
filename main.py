from tkinter import *
from tkinter import messagebox
#creating a window to put form on
root = Tk()
root.geometry("400x400")
#creating a list of all the questions so that we dont have to keep creating the same old buttons a million times
questions_total = ["My current academic program does not excite me",
"What I am learning now aligns with my future aspirations",
"I am conscious about the value of  my education",
"I sincerely work towards achieving  my academic goals I set for myself ",
"I study because I´m interested in learning",
"When the topics are difficult, I either give up or study the easy parts",
"I set goals for the grades I want in my classes",
"Even If I do not like an assignment, I can get myself to work on it",
"I make good use of the time I invest in studying",
"Despite complaining much about my work, I still do it",
"I do not have noticeable achievements that I am proud of",
"I feel that virtually any topic can be interesting once I get into it",
"I am not scared when I have to say NO in any situation ",
"I have difficulty in making friends ",
"I am not confident when I have to speak in public",
"Whenever I see that my initial plans do not lead to success in my studies, I improvise",
"In a difficult spot, my immediate action would be to put things right",
"I’m good at finding solutions to problems.",
"I've been made stronger and better by tough experiences",
"I see difficulties as temporary and expect to overcome them"]

#opening a file to write the responses into
storage_file = open("answers.txt",'w')


def get_srn():
    global srn_label
    global e
    global sub
    srn_label = Label(root, text = "Enter your SRN: ")
    srn_label.grid(row = 0)
    e = Entry(root)
    e.grid(row = 0, column = 2)
    #storage_file.write(str(e.get())+"\n")
    sub = Button(root, text = "Submit", command = clear)
    sub.grid(row = 4)
    

def call_first():   
    create_label(next(a))
    create_options()
    create_submit()
    
    

def clear():
    storage_file.write(str(e.get())+"\n")
    srn_label.grid_forget()
    e.grid_forget()
    sub.grid_forget()
    call_first()
get_srn()

#creating the radio button variable
var = IntVar()
#using iter to send the questions to the display window as it is easier this way than to implement with loops for having one question at a time on screen

a = iter(questions_total)
#i acts as a count variable
i = 0

#this function will change the question on screen without having to close and open a new root window
def update_q():
    global i
#grid_forget() function just removes the widget from the screen
    ql.grid_forget()
    if i<len(questions_total)-1:
        create_label(next(a))
    else:
        root.destroy()
        messagebox.showinfo("End","You have reached the end")
    i+=1
    selection()
#this function adds a question to the screen
def create_label(question):
    global ql
    ql = Label(root,text = question)
    
    ql.grid(row = 0)
#here is where we write into a file to store responses
def selection():
    #print(var.get())
    storage_file.write(str(var.get())+"\n")
def create_options():
    option1 = Radiobutton(root,text = "Strongly Agree", variable = var, value = 1)
    option2 = Radiobutton(root,text = "Agree", variable = var, value = 2)
    option3 = Radiobutton(root,text = "Disagree", variable = var, value = 3)
    option4 = Radiobutton(root,text = "Strongly Disagree", variable = var, value = 4)

    option1.grid(row = 2,sticky = W)
    option2.grid(row = 4,sticky = W)
    option3.grid(row = 6,sticky = W)
    option4.grid(row = 8,sticky = W)
def create_submit():
    submit = Button(text = "Submit",command = update_q)
    submit.grid(row = 10,sticky = W)

def call_first():   
    create_label(next(a))
    create_options()
    create_submit()


root.mainloop()
storage_file.close()

import graph
graph.graph()
# messagebox.showinfo("End","You have reached the end")
 
