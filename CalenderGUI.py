from tkinter import *
import calendar
import time

months = ["January", 31, 0, "Febuary", 28, 3, "March", 31, 3, "April", 30, 6]
def callback(day):
    # print("oi")
    f = open('CalendarSaveData', 'r')

    counter = 0
    for line in f:
        if day == counter:
            print(line)
        counter += 1
    # print(day)

    top = Toplevel()
    event = Entry(top)
    event.pack()
    enter = Button(top, text="Enter", command=lambda day=day, event=event: enterGoal(event, day))
    enter.pack()
    f.close()

def enterGoal(event, day):

    with open('CalendarSaveData') as fin, open('temp', 'w') as fout:
        s = event.get()
        print(s)
        counter = 0
        for line in fin:
            # print("Executing loop")
            if day == counter:
                output = s + "\n"
                fout.write(output)
                # print(output)
            else:
                fout.write(line)
                # print(line)
            counter += 1

    with open('CalendarSaveData', 'w') as fout, open('temp') as fin:
        for line in fin:
            fout.write(line)

def notcallback():
    print("lack of oi")

def prevMonth():
    print("does nothing")
    global monthIndex
    monthIndex -= 1

    month = months[monthIndex*3]
    numDays = months[(monthIndex*3)+1]
    startingDay = months[(monthIndex * 3) + 2]
    changeMonth(month, numDays, startingDay)

def nextMonth():
    print("Does nothing")
    global monthIndex
    monthIndex += 1

    month = months[monthIndex * 3]
    numDays = months[(monthIndex * 3) + 1]
    startingDay = months[(monthIndex * 3) + 2]
    changeMonth(month, numDays, startingDay)

def changeMonth(month, numDays, startingDay):

    monthTitle.config(text=month, font=("Helvetica", 16))

    for i in range(len(day)):
        day[i].destroy()

    del day[:]

    for i in range(numDays):
         day.append(Button(root, text=i + 1, command=lambda i=i: callback(i), height=5, width=8))

    counter = 0
    colplaced = startingDay
    for x in range(5):
        for y in range(7):
            day[counter].grid(row=x + calendarRowShift, column=colplaced, padx=3, pady=3)
            counter += 1
            colplaced += 1

            if colplaced == 7:
                colplaced = 0
                x += 1

            if counter == 31:
                break

def tick():
    localtime = time.asctime(time.localtime(time.time()))
    currenttime.config(text=localtime)
    clock = root.after(1000, tick)

root = Tk()
day = []
calendarRowShift = 3
lengthOfCalendar = 5
widthOfCalendar = 7
colStart = 0

month = "January"
monthIndex = 0

monthTitle = Label(root, text=month, font=("Helvetica", 16))
monthTitle.grid(row=1, column=1, columnspan=widthOfCalendar-2)

currenttime = Label(root, text=time.asctime(time.localtime(time.time())), font=("Helvetica", 16))
currenttime.grid(row=0, columnspan=widthOfCalendar)

prevMonth = Button(root, text="Previous", command=prevMonth)
prevMonth.grid(row=1, column=0)

nextMonth = Button(root, text="Next", command=nextMonth)
nextMonth.grid(row=1, column=widthOfCalendar-1)

sunday = Label(root, text="Sunday")
sunday.grid(row=2, column=0)
monday = Label(root, text="Monday")
monday.grid(row=2, column=1)
tuesday = Label(root, text="Tuesday")
tuesday.grid(row=2, column=2)
wednesday = Label(root, text="Wednesday")
wednesday.grid(row=2, column=3)
thursday = Label(root, text="Thursday")
thursday.grid(row=2, column=4)
friday = Label(root, text="Friday")
friday.grid(row=2, column=5)
saturday = Label(root, text="Saturday")
saturday.grid(row=2, column=6)


tick()

for i in range(31):
    day.append(Button(root, text=i+1, command=lambda i=i: callback(i), height=5, width=8))

counter = 0
colplaced = colStart
for x in range(5):
    for y in range(7):
        day[counter].grid(row=x+calendarRowShift, column=colplaced, padx=3, pady=3)
        counter += 1
        colplaced += 1

        if colplaced == 7:
            colplaced = 0
            x += 1

        if counter == 31:
            break


root.mainloop()