from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")

        img = Image.open(r"C:\Users\Fahad Ashfaq\Downloads\AMS.jpeg")
        img = img.resize((1530, 790))  # Resize the image to fit window
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        title_lbl=Label(self.root, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"), bg="light blue", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #student button
        img = Image.open(r"C:\Users\Fahad Ashfaq\Downloads\student.jpg")
        img = img.resize((220, 220))  # Resize the image to fit window
        self.photoimg = ImageTk.PhotoImage(img)

        b1= Button(bg_img,image=self.photoimg,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220) 

        
        b1= Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman", 15, "bold"), bg="light blue", fg="black")
        b1.place(x=200,y=300,width=220,height=40) 


        
         #Detect Face button
        img2 = Image.open(r"C:\Users\Fahad Ashfaq\Downloads\faceDetect.jpg")
        img2 = img2.resize((220, 220))  # Resize the image to fit window
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1= Button(bg_img,image=self.photoimg2,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220) 

        
        b1= Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman", 15, "bold"), bg="light blue", fg="black")
        b1.place(x=500,y=300,width=220,height=40) 


        #Attendance button
        img3 = Image.open(r"C:\Users\Fahad Ashfaq\Downloads\attendance.png")
        img3 = img3.resize((220, 220))  # Resize the image to fit window
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1= Button(bg_img,image=self.photoimg3,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220) 

        
        b1= Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman", 15, "bold"), bg="light blue", fg="black")
        b1.place(x=800,y=300,width=220,height=40) 


         #help button
        img4 = Image.open(r"C:\Users\Fahad Ashfaq\Downloads\help.png")
        img4 = img4.resize((220, 220))  # Resize the image to fit window
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1= Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220) 

        
        b1= Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman", 15, "bold"), bg="light blue", fg="black")
        b1.place(x=1100,y=300,width=220,height=40)


         #Train button
        img5 = Image.open(r"C:\Users\Fahad Ashfaq\Downloads\trainData.png")
        img5 = img5.resize((220, 220))  # Resize the image to fit window
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1= Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220) 

        
        b1= Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman", 15, "bold"), bg="light blue", fg="black")
        b1.place(x=200,y=580,width=220,height=40) 


        #Photos button
        img6 = Image.open(r"C:\Users\Fahad Ashfaq\Downloads\photos.png")
        img6 = img6.resize((220, 220))  # Resize the image to fit window
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1= Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220) 

        
        b1= Button(bg_img,text="Photos",cursor="hand2",font=("times new roman", 15, "bold"), bg="light blue", fg="black")
        b1.place(x=500,y=580,width=220,height=40) 


        #Developer button
        img7 = Image.open(r"C:\Users\Fahad Ashfaq\Downloads\developer.jpg")
        img7 = img7.resize((220, 220))  # Resize the image to fit window
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1= Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220) 

        
        b1= Button(bg_img,text="Developer",cursor="hand2",font=("times new roman", 15, "bold"), bg="light blue", fg="black")
        b1.place(x=800,y=580,width=220,height=40) 


         #Exit button
        img8 = Image.open(r"C:\Users\Fahad Ashfaq\Downloads\exit.jpg")
        img8 = img8.resize((220, 220))  # Resize the image to fit window
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1= Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220) 

        
        b1= Button(bg_img,text="Exit",cursor="hand2",font=("times new roman", 15, "bold"), bg="light blue", fg="black")
        b1.place(x=1100,y=580,width=220,height=40) 





if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
