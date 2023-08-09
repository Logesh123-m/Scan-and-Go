from tkinter import*
from tkinter import ttk
from turtle import up, update 
#from xml.etree.ElementPath import prepare_descendant
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import date, datetime
import cv2
import os
import numpy as np
import shutil
from pathlib import Path




class Face_Rocognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

 #image1
        img=Image.open(r"College_images\img9.jpg")
        img=img.resize((650,700),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=55,width=650,height=700)
#image2
        img1=Image.open(r"College_images\imgto1.jpg")
        img1=img1.resize((700,700),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=650,y=55,width=700,height=700)

#button
        b1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",15,"bold"),bg="red",fg="white")
        b1.place(x=250,y=590,width=200,height=40)


    #================================attendance=====================
    def mark_attendance(self,i,r,n,d):
        with open("Attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])

            if((i not in name_list) and (r not in name_list ) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%H:%M:%S")
                dtString=now.strftime("%d/%m/%Y")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},present")





 #=====================face recognition==================
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            #gray_image=cv2.cvtColor(img,cv2.COLOR_BAYER_BG2GRAY)
            #gray_image=cv2.cvtColor(img,cv2.COLOR_BayerGB2BGR)
            features=classifier.detectMultiScale(img,scaleFactor,minNeighbors) #%

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)  
                id,predict=clf.predict(img[y:y+h,x:x+w]) #%
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="logesh@052003",database="face_recognizer")
                my_curser=conn.cursor()

                my_curser.execute("select name from student where student_id="+str(id))
                n=my_curser.fetchone()
                n="+".join(n)

                my_curser.execute("select roll from student where student_id="+str(id))
                r=my_curser.fetchone()
                r="+".join(r)

                my_curser.execute("select dep from student where student_id="+str(id))
                d=my_curser.fetchone()
                d="+".join(d)

                my_curser.execute("select student_id from student where student_id="+str(id))
                i=my_curser.fetchone()
                i="+".join(i)




                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            # if cv2.waitKey(1)==13:
            
            if cv2.waitKey(1) & 0xFF==ord('q'):
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__=="__main__":
    root=Tk()
    obj=Face_Rocognition(root)
    root.mainloop()        
