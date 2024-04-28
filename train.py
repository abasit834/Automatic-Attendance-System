from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector  
import cv2
import os
import numpy as np



class train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train data set")

        self.title = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 45, "bold"), bg="#088F8F", fg="white")
        self.title.place(x=0, y=0, width=1530, height=100)

        btn1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",15,"bold"),width=12,bg="#088F8F",fg="white")  
        btn1.place(x=0,y=380,width=1530,height=60)



    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

       # ===Train classifiwe==
        clf = cv2.face.LBPHFaceRecognizer_create()

        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!")


        

if __name__ == "__main__":
    root = Tk()
    obj = train(root)
    root.mainloop()