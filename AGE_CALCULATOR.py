from tkinter import *

 

from tkinter import messagebox

 

def clearAll() :

 

    dayField.delete(0, END)

    monthField.delete(0, END)

    yearField.delete(0, END)

    givenDayField.delete(0, END)

    givenMonthField.delete(0, END)

    givenYearField.delete(0, END)

    rsltDayField.delete(0, END)

    rsltMonthField.delete(0, END)

    rsltYearField.delete(0, END)

 

def checkError() :


 

    if (dayField.get() == "" or monthField.get() == ""

        or yearField.get() == "" or givenDayField.get() == ""

        or givenMonthField.get() == "" or givenYearField.get() == "") :

 

        # show the error message

        messagebox.showerror("Input Error")

 

        # clearAll function calling

        clearAll()

        

        return -1

 

# function to calculate Age

def calculateAge() :


 

    value = checkError()


 

    if value == -1 :

        return

    

    else :

 

        birth_day = int(dayField.get())

        birth_month = int(monthField.get())

        birth_year = int(yearField.get())

 

        given_day = int(givenDayField.get())

        given_month = int(givenMonthField.get())

        given_year = int(givenYearField.get())

        

 

        month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        

        if (birth_day > given_day):

            given_month = given_month - 1

            given_day = given_day + month[birth_month-1]

                    

                    

 

        if (birth_month > given_month):

            given_year = given_year - 1

            given_month = given_month + 12

                    

 

        calculated_day = given_day - birth_day;

        calculated_month = given_month - birth_month;

        calculated_year = given_year - birth_year;

 

        rsltDayField.insert(10, str(calculated_day))

        rsltMonthField.insert(10, str(calculated_month))

        rsltYearField.insert(10, str(calculated_year))

    

 

if __name__ == "__main__" :

    

 

    # Create a GUI window

    gui = Tk()


 

    gui.configure(background = "black")

 

    gui.title("Age Calculator")


 

    gui.geometry("550x300")

    

    

 

    # Create a Date Of Birth : label

    dob = Label(gui, text = "Date Of Birth", bg = "black",fg="yellow",font=("overlock",12))

 

    # Create a Given Date : label

    givenDate = Label(gui, text = "Given Date", bg = "black",fg="yellow",font=("overlock",12))

 

    # Create a Day : label

    day = Label(gui, text = "Day", bg = "black",fg="yellow",font=("overlock",12))

 

    # Create a Month : label

    month = Label(gui, text = "Month", bg = "black",fg="yellow",font=("overlock",12))

 

    # Create a Year : label

    year = Label(gui, text = "Year", bg = "black",fg="yellow",font=("overlock",12))

 

    # Create a Given Day : label

    givenDay = Label(gui, text = "Given Day", bg = "black",fg="yellow",font=("overlock",12))

 

    # Create a Given Month : label

    givenMonth = Label(gui, text = "Given Month", bg = "black",fg="yellow",font=("overlock",12))

 

    # Create a Given Year : label

    givenYear = Label(gui, text = "Given Year", bg = "black",fg="yellow",font=("overlock",12))

 

    # Create a Years : label

    rsltYear = Label(gui, text = "Years", bg = "black",fg="yellow",font=("overlock",12))

 

    # Create a Months : label

    rsltMonth = Label(gui, text = "Months", bg = "black",fg="yellow",font=("overlock",12))

 

    # Create a Days : label

    rsltDay = Label(gui, text = "Days", bg = "black",fg="yellow",font=("overlock",12))

 

    # Create a Resultant Age Button and attached to calculateAge function

    resultantAge = Button(gui, text = "Resultant Age", fg = "Black", bg = "Red", command = calculateAge)

 

    # Create a Clear All Button and attached to clearAll function

    clearAllEntry = Button(gui, text = "Clear All", fg = "Black", bg = "Red", command = clearAll)

 

    # Create a text entry box for filling or typing the information.

    dayField = Entry(gui)

    monthField = Entry(gui)

    yearField = Entry(gui)

    

    givenDayField = Entry(gui)

    givenMonthField = Entry(gui)

    givenYearField = Entry(gui)

    

    rsltYearField = Entry(gui)

    rsltMonthField = Entry(gui)

    rsltDayField = Entry(gui)


 

    # grid method is used for placing

    # the widgets at respective positions

    # in table like structure .

    dob.grid(row = 0, column = 1)

    

    day.grid(row = 1, column = 0)

    dayField.grid(row = 1, column = 1)

    

    month.grid(row = 2, column = 0)

    monthField.grid(row = 2, column = 1)

    

    year.grid(row = 3, column = 0)

    yearField.grid(row = 3, column = 1)

    

    givenDate.grid(row = 0, column = 4)

    

    givenDay.grid(row = 1, column = 3)

    givenDayField.grid(row = 1, column = 4)

    

    givenMonth.grid(row = 2, column = 3)

    givenMonthField.grid(row = 2, column = 4)

    

    givenYear.grid(row = 3, column = 3)

    givenYearField.grid(row = 3, column = 4)

    

    resultantAge.grid(row = 4, column = 2)

    

    rsltYear.grid(row = 5, column = 2)

    rsltYearField.grid(row = 6, column = 2)

    

    rsltMonth.grid(row = 7, column = 2)

    rsltMonthField.grid(row = 8, column = 2)

    

    rsltDay.grid(row = 9, column = 2)

    rsltDayField.grid(row = 10, column = 2)

 

    clearAllEntry.grid(row = 12, column = 2)


 

    # Start the GUI

    gui.mainloop()
