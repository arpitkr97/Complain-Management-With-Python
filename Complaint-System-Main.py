import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

from complaintListing import ComplaintListing
from configdb import ConnectionDatabase
from abc import ABC, abstractmethod

# Config
conn = ConnectionDatabase()


class demo(ABC):

    @abstractmethod
    def SaveData(self):
        pass

    def ComplaintList(self):
        pass

# used inheritance


class System(tk.Tk):
    def __init__(self, master=None):
        super().__init__()
        self.geometry('550x350')
        self.title('Complaint Management System')
        self.configure(bg='gray')

# Style

        style = Style()
        style.theme_use('classic')
        for styles in ['TLabel', 'TButton', 'TRadioButton']:
            style.configure(styles, bg='white')

        labels = ['First Name:', 'Last Name:',
                  'Address:', 'Gender:', 'Enter complaint:']
        for i in range(5):
            Label(self, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)

        ButtonList = Button(self, text='View Complain')
        ButtonList.grid(row=5, column=1)

        ButtonSubmit = Button(self, text='Submit Now')
        ButtonSubmit.grid(row=5, column=2)

# Entries
        firstname = Entry(self, width=40, font=('Arial', 14))
        firstname.grid(row=0, column=1, columnspan=2)

        lastname = Entry(self, width=40, font=('Arial', 14))
        lastname.grid(row=1, column=1, columnspan=2)

        address = Entry(self, width=40, font=('Arial', 14))
        address.grid(row=2, column=1, columnspan=2)

        GenderGroup = StringVar()
        Radiobutton(self, text='Male', value='male',
                    variable=GenderGroup).grid(row=3, column=1)
        Radiobutton(self, text='Female', value='female',
                    variable=GenderGroup).grid(row=3, column=2)

        comment = Text(self, width=40, height=5, font=('Arial', 14))
        comment.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

        def SaveData():
            message = conn.AddText(firstname.get(), lastname.get(
            ), address.get(), GenderGroup.get(), comment.get(1.0, 'end'))
            firstname.delete(0, 'end')
            lastname.delete(0, 'end')
            address.delete(0, 'end')
            comment.delete(1.0, 'end')
            showinfo(title='Add Information', message=message)

        def ComplaintList():
            ComplaintListing()

        # accessing methods of the conn object of ConnectionDatabase
        entry1 = conn.AddText("Anjali", "Rathore", "Near FRI, Dehradun",
                              "Female", "Water Supply not proper")

        # accessing variables of class ConnectionDatabase
        print(conn.name)
        print(conn.des)

# myname = person("Deepanshu", "Bhalla")
# print(myname.last)
        ButtonSubmit.config(command=SaveData)
        ButtonList.config(command=ComplaintList)


# self.mainloop()
if __name__ == "__main__":
    app = System()
    app.mainloop()
