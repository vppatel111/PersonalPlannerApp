from tkinter import *


def callback():
    print("oi")

def notcallback():
    print("lack of oi")

root = Tk()

day = []

for i in range(31):
    day.append(Button(root, text=i+1, command=callback))

counter = 0
for x in range(5):
    for y in range(7):
        day[counter].grid(row=x, column=y)
        counter += 1
        if counter == 31:
            break


root.mainloop()

