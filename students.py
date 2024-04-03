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
        department = ttk.Combobox(self.canvas, font=("Poppins",10), width=17,state="readonly")
        department["values"]=("Select Department","Computer Science","Electrical Eng","BBA")
        department.current(0)
        department.place(x=200, y=150) 

        label2=Label(self.canvas,text="Courses",font=("Poppins",12,"bold"),fg="black")
        label2.place(x=400,y=120)
        courses = ttk.Combobox(self.canvas, font=("Poppins",10), width=17,state="readonly")
        courses["values"]=("Select Course","PF","OOP","ICT")
        courses.current(0)
        courses.place(x=400, y=150) 

        label3=Label(self.canvas,text="Batch",font=("Poppins",12,"bold"),fg="black")
        label3.place(x=200,y=220)
        batch = ttk.Combobox(self.canvas, font=("Poppins",10), width=17,state="readonly")
        batch["values"]=("Select Batch","FA21","SP22","FA23","SP23","FA23","SP24")
        batch.current(0)
        batch.place(x=200, y=250) 

        label4=Label(self.canvas,text="Semester",font=("Poppins",12,"bold"),fg="black")
        label4.place(x=400,y=220)
        semester = ttk.Combobox(self.canvas, font=("Poppins",10), width=17,state="readonly")
        semester["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        semester.current(0)
        semester.place(x=400, y=250) 

        # Student Information

        id_label=Label(self.canvas,text="Roll No",font=("Poppins",12,"bold"),fg="black")
        id_label.place(x=200,y=320)

        idText=ttk.Entry(self.canvas,width=20,font=("Poppins",13))
        idText.place(x=200,y=350)

        name_label=Label(self.canvas,text="Student Name",font=("Poppins",12,"bold"),fg="black")
        name_label.place(x=500,y=320)

        nameText=ttk.Entry(self.canvas,width=20,font=("Poppins",13),)
        nameText.place(x=500,y=350)

        dob_label=Label(self.canvas,text="DOB",font=("Poppins",12,"bold"),fg="black")
        dob_label.place(x=200,y=420)

        dobText=ttk.Entry(self.canvas,width=20,font=("Poppins",13))
        dobText.place(x=200,y=450)
        

        label5=Label(self.canvas,text="Gender",font=("Poppins",12,"bold"),fg="black")
        label5.place(x=500,y=420)
        gender = ttk.Combobox(self.canvas, font=("Poppins",10), width=25,height=28,state="readonly")
        gender["values"]=("Select Gender","Male","Female")
        gender.current(0)
        gender.place(x=500,y=450)


        # Buttons

        savebtn=Button(self.canvas,text="Save",font=("Poppins",13,"bold"),width=12,bg="#088F8F",fg="white")  
        savebtn.place(x=400,y=550)

        picbtn=Button(self.canvas,text="Take Picture",font=("Poppins",13,"bold"),width=12,bg="#088F8F",fg="white")  
        picbtn.place(x=200,y=550)


if __name__ == "__main__": 
    root = Tk()
    obj = Students_Screen(root)
    root.mainloop()
