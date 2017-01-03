from tkinter import *
import calendar
import time

month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
         "December"]

currentMonth = 1
currentYear = 2017
calendar.setfirstweekday(calendar.SUNDAY)
cal = calendar.Calendar()

monthData = cal.monthdayscalendar(currentYear, currentMonth)

#print(calendar.prmonth(2017, 1))
#print(monthData)

def weekAdjustment(colplaced):

    colplaced += 1

    if (colplaced == 7):
        colplaced = 0

    return colplaced


def callback(day, currentMonth, currentYear):

    f = open('CalendarSaveData', 'r')
    top = Toplevel()

    if currentMonth < 10:
        currentMonthCode = "0" + str(currentMonth)
    else:
        currentMonthCode = str(currentMonth)

    if (day+1) < 10:
        dayCode = "0" + str(day+1)
    else:
        dayCode = str(day+1)

    timeCode = currentMonthCode + "-" + dayCode + "-" + str(currentYear)
    #print("timeCode" + str(timeCode))

    counter = 0
    for line in f:
        print(line[:10])
        if timeCode == line[:10]:
            #goalEntered = line[:11]
            previousEvent = Label(top, text=line[11:])
            previousEvent.grid(row=0, column=2)
            print(line)
        counter += 1

    #print(day)
    #print(currentMonth)
    #print(currentYear)

    event = Entry(top)
    event.grid(row=0, column=1)
    enter = Button(top, text="Enter", command=lambda top=top, dayCode=dayCode, event=event, currentMonthCode=currentMonthCode, currentYear=currentYear: enterGoal(top, event, dayCode, currentMonthCode, currentYear))
    enter.grid(row=1, column=1)
    top.mainloop()
    f.close()

def enterGoal(top, event, dayCode, currentMonthCode, currentYear):

    with open('CalendarSaveData') as fin, open('temp', 'w') as fout:
        s = event.get()
        #print(s)

        lineWritten = 0
        timeCode = currentMonthCode + "-" + dayCode + "-" + str(currentYear)
        for line in fin:
            if timeCode == line[:10] and lineWritten == 0:
                output = timeCode + ": " + s + "\n"
                fout.write(output)
                lineWritten = 1
            elif line == "---" and lineWritten == 0:
                output = timeCode + ": " + s + "\n"
                fout.write(output)
                fout.write("---")
                lineWritten = 1
            else:
                fout.write(line)


    with open('CalendarSaveData', 'w') as fout, open('temp') as fin:
        for line in fin:
            fout.write(line)

    top.destroy()

def prevMonth():
    global currentMonth
    global currentYear
    currentMonth -= 1

    if currentMonth < 1:
        currentMonth = 12
        currentYear -= 1


    startingDay, numDays = calendar.monthrange(currentYear, currentMonth)
    startingDay = weekAdjustment(startingDay)
    changeMonth(currentMonth, numDays, startingDay, currentYear)

def nextMonth():
    global currentMonth
    global currentYear
    currentMonth += 1

    if currentMonth > 12:
        currentMonth = 1
        currentYear += 1

    startingDay, numDays = calendar.monthrange(currentYear, currentMonth)
    startingDay = weekAdjustment(startingDay)
    changeMonth(currentMonth, numDays, startingDay, currentYear)

def changeMonth(currentMonth, numDays, startingDay, currentYear):

    global month

    monthLabelString = month[currentMonth-1] + " " + str(currentYear)
    monthTitle.config(text=monthLabelString, font=("Helvetica", 16))

    for i in range(len(day)):
        day[i].destroy()

    del day[:]

    for i in range(numDays):
         day.append(Button(root, text=i + 1, command=lambda i=i, currentMonth=currentMonth, currentYear=currentYear:
            callback(i, currentMonth, currentYear), height=5, width=8))

    counter = 0
    flag = 0
    colplaced = startingDay
    for x in range(5):
        for y in range(7):
            #print(counter)
            day[counter].grid(row=x + calendarRowShift, column=colplaced, padx=3, pady=3)
            counter += 1
            colplaced += 1

            if colplaced == 7:
                colplaced = 0
                x += 1

            if counter == numDays:
                #print("break" + str(counter))
                flag = 1
                break
        if flag == 1:
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

monthLabelString = month[currentMonth-1] + " " + str(currentYear)
monthTitle = Label(root, text=monthLabelString, font=("Helvetica", 16))
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

counter = 0
colplaced, numDays = calendar.monthrange(currentYear, currentMonth)

colplaced = weekAdjustment(colplaced)

print("NumDays " + str(numDays))
print("StartDay " + str(colplaced))

for i in range(numDays):
    day.append(Button(root, text=i + 1, command=lambda i=i, currentMonth=currentMonth, currentYear=currentYear:
    callback(i, currentMonth, currentYear), height=5, width=8))

for x in range(5):
    for y in range(7):
        day[counter].grid(row=x+calendarRowShift, column=colplaced, padx=3, pady=3)
        counter += 1
        colplaced += 1

        if colplaced == 7:
            colplaced = 0
            x += 1

        if counter == numDays:
            break


root.mainloop()