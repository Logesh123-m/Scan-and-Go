from sqlite3 import Cursor
from tkinter import *
from tkinter import ttk
from turtle import up, update 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np




class Help:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1530x790+0+0")
                self.root.title("Face Recognition System")

                title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="red")
                title_lbl.place(x=0,y=0,width=1530,height=45)

     #image1
                img=Image.open(r"College_images\developer.jpeg")
                img=img.resize((1500,700),Image.ANTIALIAS)
                self.photoimg=ImageTk.PhotoImage(img)

                f_lbl=Label(self.root,image=self.photoimg)
                f_lbl.place(x=0,y=55,width=1500,height=700)

                #Developer label
                dev_label=Label(f_lbl,text="Email:logeshkeerthisangav@gmail.com",font=("times new roman",20,"bold"),bg="white")
                dev_label.place(x=600,y=400)


if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()