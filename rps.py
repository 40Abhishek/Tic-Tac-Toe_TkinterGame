from tkinter import *
import tkinter.font as font
import os

root=Tk()
root.title("Tic Tac Toe")
#root.geometry('1250*1250')
root.config(bg='black')
count=0

#color butt1= #ff007a and #952bff

def click1():
    global count
    if count%2==0:
        butt_1['text']='@'
    else:
        butt_1['text']='#'
    count+=1
    if butt_1['text']==butt_2['text']==butt_3['text']:
        butt_1['text']=butt_1['text']+' Won'
    elif butt_1['text']==butt_4['text']==butt_7['text']:
        butt_1['text']=butt_1['text']+' Won'
    elif butt_1['text']==butt_5['text']==butt_9['text']:
        butt_1['text']=butt_1['text']+' Won'

def click2():
    global count
    if count%2==0:
        butt_2['text']='@'
    else:
        butt_2['text']='#'
    count+=1
    if butt_2['text']==butt_1['text']==butt_3['text']:
        butt_2['text']=butt_2['text']+' Won'
    elif butt_2['text']==butt_5['text']==butt_8['text']:
        butt_2['text']=butt_2['text']+' Won'

def click3():
    global count
    if count%2==0:
        butt_3['text']='@'
    else:
        butt_3['text']='#'
    count+=1
    if butt_3['text']==butt_2['text']==butt_1['text']:
        butt_3['text']=butt_3['text']+' Won'
    elif butt_3['text']==butt_5['text']==butt_7['text']:
        butt_3['text']=butt_3['text']+' Won'
    elif butt_3['text']==butt_6['text']==butt_9['text']:
        butt_3['text']=butt_3['text']+' Won'

def click4():
    global count
    if count%2==0:
        butt_4['text']='@'
    else:
        butt_4['text']='#'
    count+=1
    if butt_4['text']==butt_5['text']==butt_6['text']:
        butt_4['text']=butt_4['text']+' Won'
    elif butt_4['text']==butt_1['text']==butt_7['text']:
        butt_4['text']=butt_4['text']+' Won'

def click5():
    global count
    if count%2==0:
        butt_5['text']='@'
    else:
        butt_5['text']='#'
    count+=1
    if butt_5['text']==butt_2['text']==butt_8['text']:
        butt_5['text']=butt_5['text']+' Won'
    elif butt_5['text']==butt_4['text']==butt_6['text']:
        butt_5['text']=butt_5['text']+' Won'
    elif butt_5['text']==butt_3['text']==butt_7['text']:
        butt_5['text']=butt_5['text']+' Won'
    elif butt_5['text']==butt_1['text']==butt_9['text']:
        butt_5['text']=butt_5['text']+' Won'

def click6():
    global count
    if count%2==0:
        butt_6['text']='@'
    else:
        butt_6['text']='#'
    count+=1
    if butt_6['text']==butt_9['text']==butt_3['text']:
        butt_6['text']=butt_6['text']+' Won'
    elif butt_6['text']==butt_4['text']==butt_5['text']:
        butt_6['text']=butt_6['text']+' Won'
        
def click7():
    global count
    if count%2==0:
        butt_7['text']='@'
    else:
        butt_7['text']='#'
    count+=1
    if butt_7['text']==butt_8['text']==butt_9['text']:
        butt_7['text']=butt_7['text']+' Won'
    elif butt_7['text']==butt_4['text']==butt_1['text']:
        butt_7['text']=butt_7['text']+' Won'
    elif butt_7['text']==butt_5['text']==butt_3['text']:
        butt_7['text']=butt_7['text']+' Won'

def click8():
    global count
    if count%2==0:
        butt_8['text']='@'
    else:
        butt_8['text']='#'
    count+=1
    if butt_8['text']==butt_2['text']==butt_5['text']:
        butt_8['text']=butt_8['text']+' Won'
    elif butt_8['text']==butt_9['text']==butt_7['text']:
        butt_8['text']=butt_8['text']+' Won'

def click9():
    global count
    if count%2==0:
        butt_9['text']='@'
    else:
        butt_9['text']='#'
    count+=1
    if butt_9['text']==butt_8['text']==butt_7['text']:
        butt_9['text']=butt_9['text']+' Won'
    elif butt_9['text']==butt_6['text']==butt_3['text']:
        butt_9['text']=butt_9['text']+' Won'
    elif butt_9['text']==butt_5['text']==butt_1['text']:
        butt_9['text']=butt_9['text']+' Won'

def restart():
    root.destroy()
    os.startfile(r'C:\Users\Abhishek Yadav.DESKTOP-L69K4KO\Desktop\Mypython\Tictactoe.py')

myfont=font.Font(size=20)

butt_1=Button(root,text=' ', bg='#952bff',fg='white',height=5,width=7,command=click1)
butt_2=Button(root,text=' ', bg='#952bff',fg='white',padx=50,pady=50,command=click2)
butt_3=Button(root,text=' ', bg='#952bff',fg='white',padx=50,pady=50,command=click3)

butt_4=Button(root,text=' ', bg='#952bff',fg='white',padx=50,pady=50,command=click4)
butt_5=Button(root,text=' ', bg='#952bff',fg='white',padx=50,pady=50,command=click5)
butt_6=Button(root,text=' ', bg='#952bff',fg='white',padx=50,pady=50,command=click6)

butt_7=Button(root,text=' ', bg='#952bff',fg='white',padx=50,pady=50,command=click7)
butt_8=Button(root,text=' ', bg='#952bff',fg='white',padx=50,pady=50,command=click8)
butt_9=Button(root,text=' ', bg='#952bff',fg='white',padx=50,pady=50,command=click9)

butt_re=Button(root,text='Restart',bg='#ff007a',padx=160,pady=30,command=restart)

butt_1['font']=myfont
butt_2['font']=myfont
butt_3['font']=myfont

butt_4['font']=myfont
butt_5['font']=myfont
butt_6['font']=myfont

butt_7['font']=myfont
butt_8['font']=myfont
butt_9['font']=myfont

butt_re['font']=myfont

butt_1.grid(row=0,column=0,padx=5,pady=5)
butt_2.grid(row=0,column=1,padx=5,pady=5)
butt_3.grid(row=0,column=2,padx=5,pady=5)

butt_4.grid(row=1,column=0,padx=5,pady=5)
butt_5.grid(row=1,column=1,padx=5,pady=5)
butt_6.grid(row=1,column=2,padx=5,pady=5)

butt_7.grid(row=2,column=0,padx=5,pady=5)
butt_8.grid(row=2,column=1,padx=5,pady=5)
butt_9.grid(row=2,column=2,padx=5,pady=5)

butt_re.grid(row=3,column=0,columnspan=3,padx=5,pady=5)


root.mainloop()
