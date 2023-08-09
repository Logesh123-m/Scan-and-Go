from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

     #image1
        img=Image.open(r"College_images\imgd1.jpg")
        img=img.resize((500,250),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=55,width=500,height=250)
#image2
        img1=Image.open(r"College_images\img4.jpg")
        img1=img1.resize((500,250),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=55,width=500,height=250)
#image3
        img2=Image.open(r"College_images\img8.jpg")
        img2=img2.resize((500,250),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=55,width=500,height=250)

        #button
        b1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",35,"bold"),bg="dark blue",fg="white")
        b1.place(x=0,y=320,width=1500,height=60)

 # bottom image1
        img3=Image.open(r"College_images\imgd5.jpg")
        img3=img3.resize((500,250),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=0,y=400,width=500,height=250)
#image2
        img4=Image.open(r"College_images\img6.jpg")
        img4=img4.resize((500,250),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        f_lbl=Label(self.root,image=self.photoimg4)
        f_lbl.place(x=500,y=400,width=500,height=250)
#image3
        img5=Image.open(r"College_images\imgd3.jpg")
        img5=img5.resize((500,250),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        f_lbl=Label(self.root,image=self.photoimg5)
        f_lbl.place(x=1000,y=400,width=500,height=250)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #Gray scall image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #======================Train the classifier and  save=================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset Completed!!!!!")













if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()