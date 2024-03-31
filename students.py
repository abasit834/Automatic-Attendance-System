from tkinter import *
from tkinter import ttk

class Students_Screen:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Students Enrollment")

        self.canvas = Canvas(self.root, width=1530, height=790)
        self.canvas.pack()

    
        self.canvas.configure(bg="#FAF9F6")

        self.title = Label(self.root, text="Student Enrollment", font=("Poppins", 45, "bold"), bg="#088F8F", fg="white")
        self.title.place(x=0, y=0, width=1530, height=100)

        label1=Label(self.canvas,text="Department",font=("Poppins",12,"bold"),fg="black")
        label1.place(x=200,y=120)
        textField = ttk.Combobox(self.canvas, font=("Poppins",10), width=17)
        textField.place(x=200, y=150) 

        label2=Label(self.canvas,text="Courses",font=("Poppins",12,"bold"),fg="black")
        label2.place(x=400,y=120)
        textField = ttk.Combobox(self.canvas, font=("Poppins",10), width=17)
        textField.place(x=400, y=150) 

        label3=Label(self.canvas,text="Batch",font=("Poppins",12,"bold"),fg="black")
        label3.place(x=200,y=220)
        textField = ttk.Combobox(self.canvas, font=("Poppins",10), width=17)
        textField.place(x=200, y=250) 

        label4=Label(self.canvas,text="Semester",font=("Poppins",12,"bold"),fg="black")
        label4.place(x=400,y=220)
        textField = ttk.Combobox(self.canvas, font=("Poppins",10), width=17)
        textField.place(x=400, y=250) 

if __name__ == "__main__": 
    root = Tk()
    obj = Students_Screen(root)
    root.mainloop()
