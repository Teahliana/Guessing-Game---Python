from tkinter import *
from tkinter import font
from tkinter import messagebox
from random import randint

root = Tk()
root.geometry("500x500")
root.title("Number Guessing")

def generateNumber():
    global randomNumber
    upperBounds = upperBound.get()
    upperBounds = int(upperBounds)
    randomNumber = randint(1,upperBounds)
    messagebox.showinfo ("Generated","Random Number Generated")

def guessTheNumber():
    global randomNumber
    guessNumbers = guessNumber.get()
    guessNumbers = int(guessNumbers)
    
    if guessNumbers > randomNumber:
        resultLabel.config(text="Entered Number Higher than the Number",fg="red")
        guessNumber.delete(0,"end")
    elif guessNumbers < randomNumber:
        resultLabel.config(text="Entered Number Lower than the Number",fg="red")
        guessNumber.delete(0,"end")
    else:
        resultLabel.config(text="You Entered the Correct Number",fg="green")
        guessNumber.delete(0,"end")


headingTitle = Label(root,text="Number Guessing",font = ("Arial",30)).pack()

mainFrame = Frame(root)
mainFrame.pack(pady=50)

guessNumberLabel = Label(mainFrame, text="Type a number for an upper bound: ", font=("Arial",20)).pack()

upperBound = Entry(mainFrame,font=("Arial",16))
upperBound.pack(pady=10)

generateBtn = Button(mainFrame,text="Generate Number",width=16,background="Dodgerblue",font=("Arial",18),command=generateNumber)
generateBtn.pack()

NumberLabel = Label(mainFrame, text="Type your number below: ", font=("Arial",20)).pack(pady=10)

guessNumber = Entry(mainFrame,font=("Arial",16))
guessNumber.pack(pady=10)

guessBtn = Button(mainFrame,text="Guess the Number",width=16,background="green",font=("Arial",18),command=guessTheNumber)
guessBtn.pack()

resultLabel = Label(mainFrame,text="",font=("Arial",16))
resultLabel.pack(pady=10)

root.mainloop()