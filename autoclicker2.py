import tkinter as tk
from pyautogui import *
from tkinter.messagebox import showinfo
import pyautogui as pyautogui

#new window object
window = tk.Tk()
window.geometry("300x150")
window.resizable(False, False)
window.title("Fast Autoclicker")

#global variables
userEntry = tk.StringVar()
userChoice = tk.StringVar()

#functions
def button_clicked():
    print("Button clicked")
    userEntry = entry.get()#get the text in the entry object first
    time.sleep(2.5)
    if userChoice.get() == 'left':
        pyautogui.click(button='left', clicks=int(userEntry), interval=0.08)
    elif userChoice.get() == 'right':
        pyautogui.click(button='right', clicks=int(userEntry), interval=0.08)
    #set the pause time to 1.5 seconds
    # pyautogui.click(button='right', clicks=int(userEntry), interval=0.08) #click the mouse at 100,100 with the number of clicks specified by the userEntry variable
    print("Command Done")


#main frame component
mainFrame = tk.Frame(master=window) #create frame object
mainFrame.pack(padx=10, pady=10, expand=True) #place frame on window

#label component
label1 = tk.Label(mainFrame, text="How many times do you want to click?", bg="white") #create label object
label1.pack(fill='x', expand=True) #place label on frame

#entry component
entry = tk.Entry(mainFrame, width=30) #create entry object
entry.pack(fill='x', expand=True) #place entry on frame

#checkbox component
checkBox = tk.Checkbutton(mainFrame, text="Left Click", variable=userChoice, onvalue='left', offvalue='none') #create checkbox object
checkBox.pack(side='left', fill='x', expand=True) #place checkbox on frame

#checkbox component2
checkBox2 = tk.Checkbutton(mainFrame, text="Right Click",variable=userChoice, onvalue='right', offvalue='none') #create checkbox object
checkBox2.pack(side='right',fill='y', expand=True) #place checkbox on frame

#button component
btn = tk.Button(window, text = "Run", command=button_clicked) #create button object
btn.pack(fill='x', pady=10, padx=10,expand=True) #place button on window

#start the main loop
window.mainloop() #start the event loop

