from tkinter import *

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

root = Tk()

day = []
calendarRowShift = 1
lengthOfCalendar = 5
widthOfCalendar = 7
month = "January"

monthTitle = Label(root, text=month)
monthTitle.grid(row=0, columnspan=widthOfCalendar)

for i in range(31):
    day.append(Button(root, text=i+1, command=lambda i=i: callback(i), height=5, width=8))

counter = 0
for x in range(5):
    for y in range(7):
        day[counter].grid(row=x+calendarRowShift, column=y)
        counter += 1
        if counter == 31:
            break


root.mainloop()

