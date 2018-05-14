#FIPPITHETECHIE

from Tkinter import *
import tkFont
from firebase import firebase
import random
import time



firebase = firebase.FirebaseApplication('https://healthmanagement-45328.firebaseio.com/')
master = Tk()

w = Label(master, text="WELCOME TO HEALTH MONITORING SYSTEM!", font=("Futura", 26), bg = "Gray")
w.pack()

bmi = 0

w3 = Label(master, text = 'BMI:', font=("Futura", 16))


i = 0
w6 = Label(master, text = '', font=("Futura",16))
w6.pack()

e = Entry(master)
e.pack()

e2 = Entry(master)
e2.pack()

e3 = Entry(master)
e3.pack()

w3.pack()
w5 = Label(master, text = 'You are:', font=("Futura",16))
w5.pack()
w4 = Label(master, text = 'Your Username is:', font=("Futura",16))
w4.pack()

           

master.title("HEALTH MONITORING SYSTEM")
master.geometry('800x480')


myFont = tkFont.Font(family = 'Futura', size = 18, weight = 'normal')

e.focus_set()
e.insert(0,"Name")
e2.insert(0,"Weight")
e2.focus_set()
e3.insert(0,"Height")

def pressed():
    #i = 1
    #bmi = 0
    #w3.pack()
    #if i == 1:
        #w3 = Label(master, text = 'BMI:'+(str(bmi)), font=("Futura", 16))
        #i = 0
    color = ''
    decs = ''
    name = e.get()
    add = str(random.randint(0,10000))
    finalname = e.get()+add
    weight = e2.get()
    height = e3.get()
    weight = float(weight)
    height = float(height)
    print(name)
    print(weight)
    print(height)
    bmi = float(weight/(height*height)*10000)
    bmi = round(bmi,2)
    #print(bmi)
    #print(e.get())
    #print(e2.get())
    #print(e3.get())
    e.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e.insert(0,"Name")
    e2.insert(0,"Weight")
    e3.insert(0,"Height")
    result = firebase.put('/users',finalname,{'BMI': str(bmi),'HEART RATE': 'rate'})
    print(bmi)
    if bmi < 18.50:
        desc = 'UNDERWEIGHT'
        color = 'Red'
    elif bmi > 18.50 and  bmi < 24.99:
        desc = 'HEALTHY'
        color = 'Green'
    elif bmi > 25.00 and  bmi < 29.99:
        desc = 'OVERWEIGHT'
        color = 'Red'
    elif bmi > 30:
        desc = 'OBESE'
        color = 'Red'
        
    #time.sleep(0.1)
    #if i == 0:
        #w3 = Label(master, text = 'BMI:'+(str(bmi)), font=("Futura", 16))
    w3.pack()
    w3.config(text = name+' :- BMI:'+(str(bmi)))
    w4.pack()
    w4.config(text = 'Your Username is: '+finalname)
    w5.pack()
    w5.config(text = 'You are: '+desc, fg = color)

    
    #i = 1
    
            
   
    
#def handleEvent(e, event):
#    print("I'm handling an event")


def ba(event):
    e3.delete(0,END)

def back(event):
    e2.delete(0,END)
    

def callback(event):
    #print "clicked at", event.x, event.y
    print("EDITING STARTED")
    color='Black'
    e.delete(0,END)
    w3.pack()
    w3.config(text='BMI:',)
    w4.pack()
    w4.config(text='Your Username is:')
    w5.pack()
    w5.config(text='You are: ', fg = color)
    #if i == 1:
        #w3.pack()
        #w3.config(text = 'BMI:')
    
    
    
def exitProgram():
    print("Exit Button pressed")
    #GPIO.cleanup()
    master.destroy()	

#frame = Frame(master, width=480, height=800)
e.bind("<Button-1>", callback)
e.pack()
e2.bind("<Button-1>",back)
e2.pack()
e3.bind("<Button-1>",ba)
e3.pack()

b = Button(master, text="CALCULATE",font = myFont, width=10, command=pressed)
b.pack()


exitButton  = Button(master, text = "Exit", font = myFont, command = exitProgram, height =2 , width = 6) 
exitButton.pack(side = BOTTOM)



master.mainloop()





















#e.bind('Button-1', handleEvent)

#master.protocol("WM_DELETE_WINDOW", exit)



#e = Entry(master, width=50)
#e.pack()
#e2 = Entry(master, width=50)
#e2.pack()

#text = e.get()
#def makeentry(parent, caption, width=None, **options):
#    Label(parent, text=caption).pack(side=LEFT)
#    entry = Entry(parent, **options)
#        entry.config(width=width)
#        entry.pack(side=LEFT)
#    return entry

#user = makeentry(parent, "User name:", 10)
#password = makeentry(parent, "Password:", 10, show="*")
#content = StringVar()
#entry = Entry(parent, text=caption, textvariable=content)

#text = content.get()
#content.set(text)
