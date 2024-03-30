from tkinter import *
from tkinter import ttk

class Automatic_Attendance_System :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Automatic Attendance System")


if __name__ == "__main__":
    root=Tk()
    obj=Automatic_Attendance_System(root)
    root.mainloop()