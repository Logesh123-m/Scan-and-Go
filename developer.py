from sqlite3 import Cursor
from tkinter import *
from tkinter import ttk
from turtle import up, update 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np




class Developer:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1530x790+0+0")
                self.root.title("Face Recognition System")

                title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="red")
                title_lbl.place(x=0,y=0,width=1530,height=45)

     #image1
                img=Image.open(r"College_images\developer.jpeg")
                img=img.resize((1500,700),Image.ANTIALIAS)
                self.photoimg=ImageTk.PhotoImage(img)

                f_lbl=Label(self.root,image=self.photoimg)
                f_lbl.place(x=0,y=55,width=1500,height=700)

#frame
                main_frame=Frame(f_lbl,bd=2)
                main_frame.place(x=900,y=0,width=445,height=600)

                img1=Image.open(r"College_images\img7.jpg")
                img1=img1.resize((200,200),Image.ANTIALIAS)
                self.photoimg1=ImageTk.PhotoImage(img1)

                f_lbl=Label(main_frame,image=self.photoimg1)
                f_lbl.place(x=300,y=0,width=200,height=200)

                #Developer label
                dev_label=Label(main_frame,text="OUR TEAM NAME IS LKS",font=("times new roman",20,"bold"),bg="white")
                dev_label.place(x=0,y=5)

                dev_label=Label(main_frame,text="We are full stack developers",font=("times new roman",20,"bold"),bg="white")
                dev_label.place(x=0,y=40)

                img2=Image.open(r"College_images\imgd6.jpg")
                img2=img2.resize((440,350),Image.ANTIALIAS)
                self.photoimg2=ImageTk.PhotoImage(img2)

                f_lbl=Label(main_frame,image=self.photoimg2)
                f_lbl.place(x=0,y=210,width=440,height=350)





if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()