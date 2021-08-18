import tkinter
from tkinter import *
import wikipedia as wk     # we want to import it as wk

window = Tk()      # tkinter window
window.title("MY MINI WIKIPEDIA")
window.config(bg="black")
f1_heading = Frame(window)
f2_frame = Feame(window)
f3_result = Frame(window)

Label(f1_heading,text="My Mini Wikipedia",font=("Times",30,"bold"),bg="lightgreen").pack(side=TOP)

Label(f2_frame,text="Search Here",font=("Arial",20,"bold"),bg="yellow").pack(side=LEFT)

Label(f3_result,text="Searched Results: ",font=("Arial",25,"bold"),bg="lightpink").pack(side=LEFT)

# input box
entry_box = Entry(f2_frame,width=40,font=("Arial",20,"bold"))
entry_box.pack(side=LEFT ,fill=BOTH,expand=5)
entry_box.focus_set()

query = ' '
text= Text(window,fnt=("Arial",17,"bold"),bg="lightblue",padx=55,pady=10)

def text_search():
    global query
    query = entry_box.get()
    try:
        txt_summary = wk.summary(query)
        text.insert('1.0',text_summary)
    except:
        text.insert('1.0','No Results Found')

button1 = Button(f2_frame,text="Search",font=("Arial",15,"bold"),bg="red",fg="white",command=text_search)
button1.pack(side=RIGHT)

f1_heading.pack()
f2_frame.pack(side=TOP)
f3_result.pack(side=TOP,pady=20,padx=50)
text.pack()

window.mainloop()
