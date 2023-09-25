from tkinter import *
import tkinter.font as font
import os
import random
from time import sleep
from PIL import ImageTk

root=Tk()
root.title("Rock Paper Scissor")
root.geometry('400x300')
root.config(bg='black')
count=0

def randomer():
    randomer=random.randint(0,2)
    return randomer
    
def checkbox():
    text1=''
    j=randomer()
    if j==0:
        label1.config(text='rock')
        return 'rock'
    elif j==1:
        label1.config(text='paper')
        return 'paper'
    elif j==2:
        label1.config(text='scissor')
        return 'scissor'

def score():
    pass

myfont=font.Font(size=20)
#image1=ImageTk.PhotoImage('lol.png',master='window')

label1=Label(root,text='',anchor=CENTER,pady=10,height=5,width=42)

label2=Label(root,text='0',anchor=CENTER,pady=10,height=5,width=2,bg="black",fg='white')
label3=Label(root,text='Score',anchor=CENTER,pady=10,height=5,width=2,bg='black',fg='white')

label4=Label(root,text='0',anchor=CENTER,pady=10,height=5,width=2,bg='black',fg='white')
label5=Label(root,text='Score',anchor=CENTER,pady=10,height=5,width=2,bg='black',fg='white')

rock=Button(root,text='Rock', bg='#952bff',fg='white',height=5,width=12,command=checkbox)
paper=Button(root,text='Paper', bg='#952bff',fg='white',height=5,width=12,command=checkbox)
scissor=Button(root,text='Scissor', bg='#952bff',fg='white',height=5,width=12,command=checkbox)

label1.grid(row=0,column=1,columnspan=3)

label2.grid(row=1,column=0)
label3.grid(row=1,column=3)

label4.grid(row=1,column=3)
label5.grid(row=1,column=3)

rock.grid(row=1,column=1,padx=5,pady=5)
paper.grid(row=1,column=2,padx=5,pady=5)
scissor.grid(row=1,column=3,padx=5,pady=5)



root.mainloop()
