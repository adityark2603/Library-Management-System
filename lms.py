import tkinter
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox 
import datetime

class LibraryManagementSystem:
    def __init__ (self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        #========================================Variable===================================================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.first_name_var=StringVar()
        self.last_name_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookID_var=StringVar()
        self.booktitle=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()



        lbltitle=Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="light blue", fg="maroon", bd=20, relief=RIDGE, font=("Georgia", 50, "bold"),padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="light blue")
        frame.place(x=0,y=130, width=1530, height=400)

        #========================================= DataFrameLeft ===========================================
        DataFrameLeft=LabelFrame(frame,text="Membership Information", bg="light blue", fg="maroon", bd=12, relief=RIDGE, font=("Georgia", 12, "bold"))
        DataFrameLeft.place(x=0,y=5,width=900, height=350)

        lblMember=Label(DataFrameLeft, bg="light blue", text="Member Type", font=("Georgia", 12, "bold"),textvariable=self.member_var, padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)

        comMember=ttk.Combobox(DataFrameLeft, font=("Georgia", 12, "bold"), width=27, state="readonly")
        comMember["value"]=("Admin Staff", "Student", "Professor")
        comMember.grid(row=0, column=1)

        lblPRN_No=Label(DataFrameLeft, bg="light blue", text="PRN No.", font=("Georgia", 12, "bold"), padx=2, pady=6)
        lblPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_No=Entry(DataFrameLeft, font=("Georgia", 12, "bold"), width=29)
        txtPRN_No.grid(row=1, column=1)

        lblTitle=Label(DataFrameLeft, bg="light blue", text="Title", font=("Georgia", 12, "bold"), padx=2, pady=6)
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle=Entry(DataFrameLeft, font=("Georgia", 12, "bold"), width=29)
        txtTitle.grid(row=2, column=1)

        lblFirstName=Label(DataFrameLeft, bg="light blue", text="First Name", font=("Georgia", 12, "bold"), padx=2, pady=6)
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName=Entry(DataFrameLeft, font=("Georgia", 12, "bold"), width=29)
        txtFirstName.grid(row=3, column=1)

        lblLastName=Label(DataFrameLeft, bg="light blue", text="Last Name", font=("Georgia", 12, "bold"), padx=2, pady=6)
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName=Entry(DataFrameLeft, font=("Georgia", 12, "bold"), width=29)
        txtLastName.grid(row=4, column=1)

        lblAddress1=Label(DataFrameLeft, bg="light blue", text="Address 1", font=("Georgia", 12, "bold"), padx=2, pady=6)
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1=Entry(DataFrameLeft, font=("Georgia", 12, "bold"), width=29)
        txtAddress1.grid(row=5, column=1)

        lblAddress2=Label(DataFrameLeft, bg="light blue", text="Address 2", font=("Georgia", 12, "bold"), padx=2, pady=6)
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2=Entry(DataFrameLeft, font=("Georgia", 12, "bold"), width=29)
        txtAddress2.grid(row=6, column=1)

        lblPostalCode=Label(DataFrameLeft, bg="light blue", text="Postal Code", font=("Georgia", 12, "bold"), padx=2, pady=6)
        lblPostalCode.grid(row=7, column=0, sticky=W)
        txtPostalCode=Entry(DataFrameLeft, font=("Georgia", 12, "bold"), width=29)
        txtPostalCode.grid(row=7, column=1)

        lblMobile=Label(DataFrameLeft, bg="light blue", text="Mobile", font=("Georgia", 12, "bold"), padx=2, pady=6)
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile=Entry(DataFrameLeft, font=("Georgia", 12, "bold"), width=29)
        txtMobile.grid(row=8, column=1)

        lblBookID=Label(DataFrameLeft, bg="light blue", text="Book ID", font=("Georgia", 12, "bold"), padx=2, pady=6)
        lblBookID.grid(row=0, column=2, sticky=W)
        txtBookID=Entry(DataFrameLeft, font=("Georgia", 12, "bold"), width=29)
        txtBookID.grid(row=0, column=3)

        lblBookTitle=Label(DataFrameLeft, bg="light blue", text="Book Title", font=("Georgia", 12, "bold"), padx=2, pady=6)
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle=Entry(DataFrameLeft, font=("Georgia", 12, "bold"), width=29)
        txtBookTitle.grid(row=1, column=3)

        lblAuthor=Label(DataFrameLeft, bg="light blue", text="Author", font=("Georgia", 12, "bold"), padx=2, pady=6)
        lblAuthor.grid(row=2, column=2, sticky=W)
        txtAuthor=Entry(DataFrameLeft, font=("Georgia", 12, "bold"), width=29)
        txtAuthor.grid(row=2, column=3)

        lblDateBorrowed=Label(DataFrameLeft, bg="light blue", text="Date Borrowed", font=("Georgia", 12, "bold"), padx=2, pady=6)
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft, font=("Georgia", 12, "bold"), width=29)
        txtDateBorrowed.grid(row=3, column=3)

        lblDateDue=Label(DataFrameLeft, bg="light blue", text="Date Due", font=("Georgia", 12, "bold"), padx=2, pady=6)
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue=Entry(DataFrameLeft, font=("Georgia", 12, "bold"), width=29)
        txtDateDue.grid(row=4, column=3)

        lblDaysOnBook=Label(DataFrameLeft, bg="light blue", text="Days on book", font=("Georgia", 12, "bold"), padx=2, pady=6)
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft, font=("Georgia", 12, "bold"), width=29)
        txtDaysOnBook.grid(row=5, column=3)

        lblLateReturnFine=Label(DataFrameLeft, bg="light blue", text="Late Return Fine", font=("Georgia", 12, "bold"), padx=2, pady=6)
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft, font=("Georgia", 12, "bold"), width=29)
        txtLateReturnFine.grid(row=6, column=3)

        lblDateOverDate=Label(DataFrameLeft, bg="light blue", text="Date Over Date", font=("Georgia", 12, "bold"), padx=2, pady=6)
        lblDateOverDate.grid(row=7, column=2, sticky=W)
        txtDateOverDate=Entry(DataFrameLeft, font=("Georgia", 12, "bold"), width=29)
        txtDateOverDate.grid(row=7, column=3)

        lblActualPrice=Label(DataFrameLeft, bg="light blue", text="Actual Price", font=("Georgia", 12, "bold"), padx=2, pady=6)
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice=Entry(DataFrameLeft, font=("Georgia", 12, "bold"), width=29)
        txtActualPrice.grid(row=8, column=3)

        #========================================= DataFrameRight ===========================================

        DataFrameRight=LabelFrame(frame,text="Book Details", bg="light blue", fg="maroon", bd=12, relief=RIDGE, font=("Georgia", 12, "bold"))
        DataFrameRight.place(x=870,y=5,width=580, height=350)

        self.txtBox=Text(DataFrameRight, font=("Georgia", 12, "bold"), width=32, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")

        listBooks=["1984", "To Kill a Mockingbird", "The Great Gatsby", "Pride and Prejudice", "The Catcher in the Rye", "Harry Potter and the Sorcerer's Stone", "The Lord of the Rings", "The Alchemist", "The Diary of a Young Girl", "The Hobbit", "The Hunger Games", "The Chronicles of Narnia", "The Little Prince", "The Book Thief", "The Da Vinci Code", "The Kite Runner", "The Handmaid's Tale", "The Hitchhiker's Guide to the Galaxy", "The Shining", "The Girl with the Dragon Tattoo"]
        
        def SelectBook(Event=""):
            value=str(listBox.get(list.curselection))
            x=value
            if(x=="1984"):
                self.bookID_var.set("BKID5757")
                self.booktitle_var.set("The Great Gatsby")
                self.author_var.set("Paul")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.30")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 788")

        listBox=Listbox(DataFrameRight, font=("Georgia", 12, "bold"), width=20, height=16)
        listBox.bind("<<Listboxselect>>", SelectBook)
        listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END, item)

        
        #========================================== Buttons Frame ==========================================


        Framebutton=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="light blue")
        Framebutton.place(x=0,y=530, width=1530, height=70)

        btnAddData=Button(Framebutton, command=self.add_data, text="Add Data", font=("Georgia", 12, "bold"), width=20, bg="maroon", fg="white")
        btnAddData.grid(row=0, column=0) 

        btnAddData=Button(Framebutton, text="Show Data", font=("Georgia", 12, "bold"), width=20, bg="maroon", fg="white")
        btnAddData.grid(row=0, column=1)

        btnAddData=Button(Framebutton, text="Update Data", font=("Georgia", 12, "bold"), width=20, bg="maroon", fg="white")
        btnAddData.grid(row=0, column=2)

        btnAddData=Button(Framebutton, text="Delete Data", font=("Georgia", 12, "bold"), width=20, bg="maroon", fg="white")
        btnAddData.grid(row=0, column=3)

        btnAddData=Button(Framebutton, text="Reset Data", font=("Georgia", 12, "bold"), width=20, bg="maroon", fg="white")
        btnAddData.grid(row=0, column=4)

        btnAddData=Button(Framebutton, text="Exit", font=("Georgia", 12, "bold"), width=20, bg="maroon", fg="white")
        btnAddData.grid(row=0, column=5)

        #========================================== Information Frame ==========================================


        FrameDetails=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="light blue")
        FrameDetails.place(x=0,y=590, width=1530, height=210)

        Table_frame=Frame(FrameDetails, bd=6, relief=RIDGE, bg="light blue")
        Table_frame.place(x=0, y=2, width=1460, height=190)

        xscroll=ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame, column=("Member type", "PRN No.", "Title", "First Name", "Last Name", "Address 1", "Address 2", "Post ID", "Mobile", "Book ID", "Book Title", "Author", "Date Borrowed", "Date Due", "Days", "Late Return Fine", "Date Over due", "Final Price"),xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("Member type", text="Member Type")
        self.library_table.heading("PRN No.", text="PRN No.")
        self.library_table.heading("Title", text="Title")
        self.library_table.heading("First Name", text="First Name")
        self.library_table.heading("Last Name", text="Last Name")
        self.library_table.heading("Address 1", text="Address 1")
        self.library_table.heading("Address 2", text="Address 2")
        self.library_table.heading("Post ID", text="Post ID")
        self.library_table.heading("Mobile", text="Mobile Number")
        self.library_table.heading("Book ID", text="Book ID")
        self.library_table.heading("Book Title", text="Book Title")
        self.library_table.heading("Author", text="Author")
        self.library_table.heading("Date Borrowed", text="Date Borrowed")
        self.library_table.heading("Date Due", text="Date Due")
        self.library_table.heading("Days", text="Days on Book")
        self.library_table.heading("Late Return Fine", text="Late Return Fine")
        self.library_table.heading("Date Over due", text="Date Over Due")
        self.library_table.heading("Final Price", text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("Member type", width=100)
        self.library_table.column("PRN No.", width=100)
        self.library_table.column("Title", width=100)
        self.library_table.column("First Name", width=100)
        self.library_table.column("Last Name", width=100)
        self.library_table.column("Address 1", width=100)
        self.library_table.column("Address 2", width=100)
        self.library_table.column("Post ID", width=100)
        self.library_table.column("Mobile", width=100)
        self.library_table.column("Book ID", width=100)
        self.library_table.column("Book Title", width=100)
        self.library_table.column("Author", width=100)
        self.library_table.column("Date Borrowed", width=100)
        self.library_table.column("Date Due", width=100)
        self.library_table.column("Days", width=100)
        self.library_table.column("Late Return Fine", width=100)
        self.library_table.column("Date Over due", width=100)
        self.library_table.column("Final Price", width=100)

    def add_data(self):
            conn=mysql.connector(host="localhost", username="root", password="Born@26March2005", database="adityadb")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.member_var.get(),
            self.prn_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.booktitle_var.get(),
            self.author_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var_get(),
            self.latereturnfine_var.get(),
            self.dateoverdue_var.get(),
            self.finalprice_var.get()
            ))

            conn.commit()
            conn.close()
            messagebox.showinfo("success", "member has been inserted successfully")


if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
