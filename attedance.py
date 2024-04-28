from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector  
import cv2

class Attendance_Screen:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance")

        self.canvas = Canvas(self.root, width=1530, height=790)
        self.canvas.pack()

        self.title = Label(self.root, text="Attendance", font=("times new roman", 45, "bold"), bg="light blue", fg="black")
        self.title.place(x=0, y=0, width=1530, height=100)

        # Icon
        img = Image.open("attendance2.png")
        img = img.resize((200, 200))
        self.photoimg = ImageTk.PhotoImage(img)
        lbl = Label(self.root, image=self.photoimg)
        lbl.place(x=300, y=120, width=200, height=200)

        # Label and Combobox for Department
        label3=Label(self.canvas,text="Department",font=("Poppins",12,"bold"),fg="black")
        label3.place(x=200,y=350)
        department = ttk.Combobox(self.canvas, font=("Poppins",10), width=17,state="readonly")
        department["values"]=("Select Department","Computer Science","Electrical Eng","BBA")
        department.current(0)
        department.place(x=200, y=380) 

        # Label and Combobox for Courses
        label4=Label(self.canvas,text="Courses",font=("Poppins",12,"bold"),fg="black")
        label4.place(x=400,y=350)
        courses = ttk.Combobox(self.canvas, font=("Poppins",10), width=17,state="readonly")
        courses["values"]=("Select Course","PF","OOP","ICT")
        courses.current(0)
        courses.place(x=400, y=380) 

        # Label and Combobox for Section
        label1=Label(self.canvas,text="Section",font=("Poppins",12,"bold"),fg="black")
        label1.place(x=200,y=450)
        Section = ttk.Combobox(self.canvas, font=("Poppins",10), width=17,height=28,state="readonly")
        Section["values"]=("Select Section","A","B","C")
        Section.current(0)
        Section.place(x=200,y=480)

        # Label and Combobox for Batch
        label2=Label(self.canvas,text="Batch",font=("Poppins",12,"bold"),fg="black")
        label2.place(x=400,y=450)
        Batch = ttk.Combobox(self.canvas, font=("Poppins",10), width=17,height=28,state="readonly")
        Batch["values"]=("Select Batch","FA21","SP22","FA23","SP23","FA23","SP24")
        Batch.current(0)
        Batch.place(x=400,y=480)

        # Check Attendance Button
        checkbtn=Button(self.canvas,text="Check Attendance",font=("times new roman",13,"bold"),width=15,bg="light blue",fg="black")  
        checkbtn.place(x=280,y=550)

        # Frame on the right side
        frame = Frame(self.root, bd=2, relief=SOLID)
        frame.place(x=770, y=100, width=750, height=690)  # Adjusted coordinates

        # Add scrollbar
        scrollbar_x = Scrollbar(frame, orient=HORIZONTAL)
        scrollbar_y = Scrollbar(frame, orient=VERTICAL)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        scrollbar_y.pack(side=RIGHT, fill=Y)

        # Configure scrollbar with frame
        canvas = Canvas(frame,  bd=0, xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)
        scrollbar_x.config(command=canvas.xview)
        scrollbar_y.config(command=canvas.yview)

        # Make the canvas the scrollable region
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create another frame inside the canvas
        inner_frame = Frame(canvas, bg="white")
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")

        # Column Headers
        columns = ["Student Name", "Student ID", "Course Name", "Date", "Time", "Status"]
        for i, column in enumerate(columns):
            label = Label(inner_frame, text=column, font=("Poppins", 12, "bold"), fg="black", padx=25, pady=10, relief=RIDGE)
            label.grid(row=0, column=i, sticky="nsew")
            inner_frame.columnconfigure(i, weight=1)  # Stretch column to frame width

if __name__ == "__main__":
    root = Tk()
    obj = Attendance_Screen(root)
    root.mainloop()
