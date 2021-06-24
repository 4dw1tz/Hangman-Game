#Hangman Game
from tkinter import *
import random
from turtle import *
speed(11)

def Draw(Lives):
    global Word
    penup()
    width(10)
    if Lives==10:
        setpos(0,-150)
        pendown()
        forward(150)
    elif Lives==9:
        setpos(150,-150)
        left(90)
        pendown()
        forward(300)
    elif Lives==8:
        setpos(150, 150)
        left(90)
        pendown()
        forward(100)
    elif Lives==7:
        setpos(50, 150)
        left(90)
        pendown()
        forward(50)
    elif Lives==6:
        setpos(50, 100)
        right(90)
        fillcolor("red")
        begin_fill()
        circle(25)
        end_fill()
        left(90)
    elif Lives==5:
        setpos(50,50)
        pendown()
        color("red")
        forward(100)
    elif Lives==4:
        setpos(50,35)
        pendown()
        left(45)
        forward(50)
    elif Lives==3:
        setpos(50,35)
        pendown()
        right(90)
        forward(50)
        left(45)
    elif Lives==2:
        setpos(50,-50)
        pendown()
        left(45)
        forward(75)
    elif Lives==1:
        setpos(50,-50)
        pendown()
        right(90)
        forward(75)
        left(45)
    elif Lives==0:
        setpos(40,75)
        color("black")
        pendown()
        write("X")
        penup()
        setpos(60,75)
        pendown()
        write("X")
        penup()
        setpos(60,60)
        pendown()
        width(5)
        right(180)
        circle(10,180)
        Main.config(text="You were HUNG!!!", bg="red")
        Display.config(text=Word, bg="red")
        EnterB['state']='disabled'
        root.mainloop()

#Setting up the main window
root=Screen()
root.setup(width=500, height=500)
root.title("Hangman by Witty_Coding")

#Bank of words to be used
File=open("nounlist.txt", "r")
List=File.readlines()
Main=Label(text="Guess a Letter", font="ArielBold 25", bg="light green")
Main.pack()

#Random word chosen
Word=random.choice(List)
Word=Word.replace("\n", "")
#print(Word)
global Lives
Lives=11
Output=[]
Output.extend("_"*len(Word))

def Play():
    Enter.delete(0, END)
    String=((str(Output).replace("', '"," ")).replace("['", "")).replace("']", "")
    Display.config(text=String)
    if String.replace(" ", "")==Word:
        Main.config(text="Weldone! You WIN!!!")
        EnterB['state']='disabled'
    root.mainloop()
    
def Pressed():
        global Lives
        Guess=Enter.get()
        if len(Guess)!=1:
            Main.config(text="Please guess 1 character!", bg="red")
            Play()
        else:
            Main.config(text="Guess a Letter", bg="light green")
        Found=False
        pos=0
        for Letter in Word:
            if Guess==Letter:
                Found=True
                Output[pos]=Guess
            pos+=1
        if Found==False:
            Lives-=1
            penup()
            setpos(-100, Lives*25-150)
            pendown()
            write(Guess, font=("Ariel",20,"normal"))
            Draw(Lives)
        Play()

String=((str(Output).replace("', '"," ")).replace("['", "")).replace("']", "")
Display=Label(text=String, font="ArielBold 30", bg="light green")
Display.pack()
Enter=Entry()
Enter.pack()
EnterB=Button(text="Enter", height=2, width=10, command=Pressed)
EnterB.pack()
Play()

root.mainloop()
