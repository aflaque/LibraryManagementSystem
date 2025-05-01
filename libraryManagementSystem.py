from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter



class LibraryMangementSystem:
    def __init__ (self,root):
        self.root=root
        self.root.title('Library Management System')
        self.root.geometry("1550x800+0+0")

        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finallprice_var=StringVar()



        lbltitle=Label(self.root,text='LIBRARY MANAGEMENT SYSTEM',bg='powder blue',fg='green',bd='20',relief=RIDGE,font=('times new roman',50,'bold'),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg='powder blue')
        frame.place(x=0,y=130,width=1530,height=400)
        

        ###DataFrameleft
        DataFrameLeft=LabelFrame(frame,text='Library Membership Information',bg='powder blue',fg='dark blue',bd='12',relief=RIDGE,font=('times new roman',15,'bold'))
        DataFrameLeft.place(x=0,y=5,width=860,height=350)

        lblMember=Label(DataFrameLeft,bg='powder blue',text="Member Type",font=('ariel',12,'bold'),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)
        lblmember=Entry(DataFrameLeft,font=('arial',8,'bold'),textvariable=self.member_var,width=24)
        lblmember.grid(row=1,column=1)
        
        comMember=ttk.Combobox(DataFrameLeft,font=('ariel',12,'bold'),width=27,state='readonly')
        comMember['value']=('Admin staff','Student','Lecturer')
        comMember.current(0)
        comMember.grid(row=0,column=1)

        lblPRN_NO=Label(DataFrameLeft,bg='powder blue',text="PRN No",font=('ariel',12,'bold'),padx=2)
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=('arial',13,'bold'),textvariable=self.prn_var,width=29)
        txtPRN_NO.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,bg='powder blue',text="ID No",font=('ariel',12,'bold'),padx=2,pady=4)
        lblTitle.grid(row=2,column=0,sticky='w')
        txtTitle=Entry(DataFrameLeft,font=('arial',13,'bold'),textvariable=self.id_var,width=29)
        txtTitle.grid(row=2,column=1)
        
        lblFirstName=Label(DataFrameLeft,bg='powder blue',text="FirstName",font=('ariel',12,'bold'),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky='w')
        txtFirstName=Entry(DataFrameLeft,font=('arial',13,'bold'),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)
        
        lblLastName=Label(DataFrameLeft,bg='powder blue',text="LastName",font=('ariel',12,'bold'),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky='w')
        txtLastName=Entry(DataFrameLeft,font=('arial',13,'bold'),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)
        
        lblAddress1=Label(DataFrameLeft,bg='powder blue',text="Address1",font=('ariel',12,'bold'),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky='w')
        txtAddress1=Entry(DataFrameLeft,font=('arial',13,'bold'),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)
        
        lblAddress2=Label(DataFrameLeft,bg='powder blue',text="Address2",font=('ariel',12,'bold'),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky='w')
        txtAddress2=Entry(DataFrameLeft,font=('arial',13,'bold'),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)
        
        lblPostCode=Label(DataFrameLeft,bg='powder blue',text="Post Code",font=('ariel',12,'bold'),padx=2,pady=6)
        lblPostCode.grid(row=7,column=0,sticky='w')
        txtPostCode=Entry(DataFrameLeft,font=('arial',13,'bold'),textvariable=self.postcode_var,width=29)
        txtPostCode.grid(row=7,column=1)
        
        lblMobile=Label(DataFrameLeft,bg='powder blue',text="Mobile",font=('ariel',12,'bold'),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky='w')
        txtMobile=Entry(DataFrameLeft,font=('arial',13,'bold'),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8,column=1)
        
        lblBookId=Label(DataFrameLeft,bg='powder blue',text="Book Id",font=('ariel',12,'bold'),padx=2)
        lblBookId.grid(row=0,column=2,sticky='w')
        txtBookId=Entry(DataFrameLeft,font=('arial',13,'bold'),textvariable=self.bookid_var,width=29)
        txtBookId.grid(row=0,column=3)
        
        lblBookTitle=Label(DataFrameLeft,bg='powder blue',text="Book Title",font=('ariel',12,'bold'),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky='w')
        txtBookTitle=Entry(DataFrameLeft,font=('arial',13,'bold'),textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1,column=3)
        
        lblAuther=Label(DataFrameLeft,bg='powder blue',text="Auther Name",font=('ariel',12,'bold'),padx=2,pady=6)
        lblAuther.grid(row=2,column=2,sticky='w')
        txtAuther=Entry(DataFrameLeft,font=('arial',13,'bold'),textvariable=self.auther_var,width=29)
        txtAuther.grid(row=2,column=3)
        
        lblDateBorrowed=Label(DataFrameLeft,bg='powder blue',text="Date Borrowed",font=('ariel',12,'bold'),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky='w')
        txtDateBorrowed=Entry(DataFrameLeft,font=('arial',13,'bold'),textvariable=self.dateborrowed_var,width=29)
        txtDateBorrowed.grid(row=3,column=3)
        
        lblDateDue=Label(DataFrameLeft,bg='powder blue',text="Date Due",font=('ariel',12,'bold'),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky='w')
        txtDateDue=Entry(DataFrameLeft,font=('arial',13,'bold'),textvariable=self.datedue_var,width=29)
        txtDateDue.grid(row=4,column=3)
        
        lblDaysOnBook=Label(DataFrameLeft,bg='powder blue',text="Days On Book",font=('ariel',12,'bold'),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky='w')
        txtDaysOnBook=Entry(DataFrameLeft,font=('arial',13,'bold'),textvariable=self.daysonbook_var,width=29)
        txtDaysOnBook.grid(row=5,column=3)
        
        lblLateReturnFine=Label(DataFrameLeft,bg='powder blue',text="Late Return Fine",font=('ariel',12,'bold'),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky='w')
        txtLateReturnFine=Entry(DataFrameLeft,font=('arial',13,'bold'),textvariable=self.lateratefine_var,width=29)
        txtLateReturnFine.grid(row=6,column=3)
        
        lblDateOverdate=Label(DataFrameLeft,bg='powder blue',text="Date Overdate",font=('ariel',12,'bold'),padx=2,pady=6)
        lblDateOverdate.grid(row=7,column=2,sticky='w')
        txtDateOverdate=Entry(DataFrameLeft,font=('arial',13,'bold'),textvariable=self.dateoverdue_var,width=29)
        txtDateOverdate.grid(row=7,column=3)
        
        lblActualPrice=Label(DataFrameLeft,bg='powder blue',text="Actual Price",font=('ariel',12,'bold'),padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky='w')
        txtActualPrice=Entry(DataFrameLeft,font=('arial',13,'bold'),textvariable=self.finallprice_var,width=29)
        txtActualPrice.grid(row=8,column=3)



        ###DataFrameRight
        DataFrameRight=LabelFrame(frame,text='Book Details',bg='powder blue',fg='dark blue',bd='12',relief=RIDGE,font=('ariel',12,'bold'))
        DataFrameRight.place(x=870,y=5,width=540,height=350)

        self.txtBox=Text(DataFrameRight,font=('arial',12,'bold'),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky='ns')

        listBooks=['Head Firt Book','Learn Pyhton The Hard Way','Python Programming','Secrete Rashy','Pyhton Cook Book','Into Machine Learning','Fluent pyhton','Machine Techno','My Python','Joss Ellif Guru','Elite Jungle Python','Jungli Python','Mumbai Python','Pune Pyhton','Machine Python','Advance Pyhton','Inton Pyhton','Redchilli Pyhton','Ishq Pyhton']

        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))       
            x=value
            if (x=="Head Firt Book"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("Paul Berry")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.788")
                
            elif (x=="Learn Pyhton The Hard Way"):
                self.bookid_var.set("BKID8796")
                self.booktitle_var.set("Basic of Python")
                self.auther_var.set("Zed A. Shaw")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.500")
            elif (x=="Python Programming"):
                self.bookid_var.set("BKID1245")
                self.booktitle_var.set("Intro to python Comp Science")
                self.auther_var.set("John Zhelle")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.500")
            elif (x=="Secrete Rashy"):
                self.bookid_var.set("BKID8759")
                self.booktitle_var.set("Basic of Python Tutorial")
                self.auther_var.set("Ref.Kapil Kamble")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.289")
            elif (x=="Pyhton Cook Book"):
                self.bookid_var.set("BKID2546")
                self.booktitle_var.set("Python Cook book")
                self.auther_var.set("Brian Jones")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.354")
            elif (x=="Into Machine Learning"):
                self.bookid_var.set("BKID3618")
                self.booktitle_var.set("Intro to Machine Learning")
                self.auther_var.set("Sarah Guaido")
                
       
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.725")
            elif (x=="Into Machine Learning"):
                self.bookid_var.set("BKID3618")
                self.booktitle_var.set("Intro to Machine Learning")
                self.auther_var.set("Sarah Guaido")
                
       
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.725")
            elif (x=="Fluent pyhton"):
                self.bookid_var.set("BKID4618")
                self.booktitle_var.set("Master Python")
                self.auther_var.set("James Chadwick")
                
       
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.800")
            elif (x=="Machine Techno"):
                self.bookid_var.set("BKID4724")
                self.booktitle_var.set("Technics Of Machine")
                self.auther_var.set("Fabio lambda")
                
       
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.1000")
            elif (x=="My Python"):
                self.bookid_var.set("BKID9087")
                self.booktitle_var.set("My Python")
                self.auther_var.set("Joseph Ryan")
                
       
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.600")
            elif (x=="Joss Ellif Guru"):
                self.bookid_var.set("BKID2031")
                self.booktitle_var.set("Guides In Python")
                self.auther_var.set("Joss Guru")
                
       
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.500")
            elif (x=="Jungli Python"):
                self.bookid_var.set("BKID4321")
                self.booktitle_var.set("Jungli Python")
                self.auther_var.set("Samuel Jackson")
                
       
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.300")
            elif (x=="Mumbai Python"):
                self.bookid_var.set("BKID4044")
                self.booktitle_var.set("Mumbai Python")
                self.auther_var.set("Peter Frost")
                
       
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.750")
            elif (x=="Pune Pyhton"):
                self.bookid_var.set("BKID7431")
                self.booktitle_var.set("Pune Pyhton")
                self.auther_var.set("Hari Prasad")
                
       
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.500")
            elif (x=='Advance Pyhton'):                            
                self.bookid_var.set("BKID3756")
                self.booktitle_var.set("Advanced Learning")
                self.auther_var.set("Robert William Jr.")
                
       
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.1000")
            elif (x=="Inton Pyhton"):
                self.bookid_var.set("BKID5679")
                self.booktitle_var.set("Inton Pyhton")
                self.auther_var.set("steve king")
                
       
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.700")
            
            elif (x=="Redchilli Pyhton"):
                self.bookid_var.set("BKID9701")
                self.booktitle_var.set("Redchilli Pyhton")
                self.auther_var.set("James Holland")
                
       
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.600")
            
            elif (x=="Ishq Pyhton"):
                self.bookid_var.set("BKID3782")
                self.booktitle_var.set("Ishq Pyhton")
                self.auther_var.set("Tony Musk")
                
       
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.400")


        listBox=Listbox(DataFrameRight,font=('ariel',12,'bold'),width=20,height=16)
        listBox.bind('<<ListboxSelect>>',SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)

        ###BUTTON FRAME
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg='powder blue')
        Framebutton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button(Framebutton,command=self.adda_data,text='Add Data',font=('arial',12,'bold'),width=23,bg='blue',fg='white')
        btnAddData.grid(row=0,column=0)                     
        
        btnAddData=Button(Framebutton,command=self.showData,text='Show Data',font=('arial',12,'bold'),width=23,bg='blue',fg='white')
        btnAddData.grid(row=0,column=1)
        
        btnAddData=Button(Framebutton,command=self.update,text='Update',font=('arial',12,'bold'),width=23,bg='blue',fg='white')
        btnAddData.grid(row=0,column=2)
        
        btnAddData=Button(Framebutton,command=self.delete,text='Delete',font=('arial',12,'bold'),width=23,bg='blue',fg='white')
        btnAddData.grid(row=0,column=3)
        
        btnAddData=Button(Framebutton,command=self.reset,text='Reset',font=('arial',12,'bold'),width=23,bg='blue',fg='white')
        btnAddData.grid(row=0,column=4)
        
        btnAddData=Button(Framebutton,command=self.iExit,text='Exit',font=('arial',12,'bold'),width=23,bg='blue',fg='white')
        btnAddData.grid(row=0,column=5)



        ###INFORMATION FRAME
        FrameDetails=Frame(self.root,bd=8,relief=RIDGE,padx=20,bg='powder blue')
        FrameDetails.place(x=0,y=590,width=1530,height=210)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg='powder blue')
        Table_frame.place(x=0,y=2,width=1460,height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)


        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","adress1","adress2","postid","mobile","bookid","booktitle","auther","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)


        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No.")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("adress1",text="Address1")
        self.library_table.heading("adress2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("auther",text="Author")
        self.library_table.heading("dateborrowed",text="Date of Borrowing")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="DaysOnBook")
        self.library_table.heading("latereturnfine",text="LateReturnFine")
        self.library_table.heading("dateoverdue",text="DateOverDue")
        self.library_table.heading("finalprice",text="Final Price")
        
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("adress1",width=130)
        self.library_table.column("adress2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)



    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",passwd="aflaque5",database='project')
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.member_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.auther_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook_var.get(),
                                                                                                                self.lateratefine_var.get(),
                                                                                                                self.dateoverdue_var.get(),
                                                                                                                self.finallprice_var.get(),
                                                                                                                ))
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success","Member has been inserted successfully")

    def update(self): #error
        conn=mysql.connector.connect(host='localhost',username='root',passwd='aflaque5',database='project')
        my_cursor=conn.cursor()
        my_cursor.execute('update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostId=%s,Mobile=%s,BookId=%s,BookTitle=%s,Auther=%s,Dateborrowed=%s,DateDue=%s,Daysonbook=%s,LateReturnFine=%s,Daysoverdue=%s,finalPrice=%s where PRN_NO=%s',(
                                                       self.member_var.get(),
                                                       self.id_var.get(),          
                                                       self.firstname_var.get(),
                                                       self.lastname_var.get(),
                                                       self.address1_var.get(),
                                                       self.address2_var.get(),
                                                       self.postcode_var.get(),
                                                       self.mobile_var.get(),
                                                       self.bookid_var.get(),
                                                       self.booktitle_var.get(),
                                                       self.auther_var.get(),
                                                       self.dateborrowed_var.get(),
                                                       self.datedue_var.get(),
                                                       self.daysonbook_var.get(),
                                                       self.lateratefine_var.get(),
                                                       self.dateoverdue_var.get(),
                                                       self.finallprice_var.get(),
                                                       self.prn_var.get(),
                                                       
                                                ))
                                                                            
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        
        messagebox.showinfo('Success','Member has been Updated')


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",passwd="aflaque5",database='project')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()
        
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event=''):  
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']
        
        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.auther_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.lateratefine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finallprice_var.set(row[17])


    def showData(self):
        self.txtBox.insert(END,'Member Type:\t\t'+ self.member_var.get()+ '\n')
        self.txtBox.insert(END,'PRN No:\t\t'+ self.prn_var.get()+ '\n')
        self.txtBox.insert(END,'ID No:\t\t'+ self.id_var.get()+ '\n')
        self.txtBox.insert(END,'Firstname:\t\t'+ self.firstname_var.get()+ '\n')
        self.txtBox.insert(END,'Lastname:\t\t'+ self.lastname_var.get()+ '\n')
        self.txtBox.insert(END,'Address1:\t\t'+ self.address1_var.get()+ '\n')
        self.txtBox.insert(END,'Address2:\t\t'+ self.address2_var.get()+ '\n')
        self.txtBox.insert(END,'Post Code:\t\t'+ self.postcode_var.get()+ '\n')
        self.txtBox.insert(END,'Mobile No:\t\t'+ self.mobile_var.get()+ '\n')
        self.txtBox.insert(END,'Book ID:\t\t'+ self.bookid_var.get()+ '\n')
        self.txtBox.insert(END,'Book Title:\t\t'+ self.booktitle_var.get()+ '\n')
        self.txtBox.insert(END,'Author:\t\t'+ self.auther_var.get()+ '\n')
        self.txtBox.insert(END,'DateBorrowed:\t\t'+ self.dateborrowed_var.get()+ '\n')
        self.txtBox.insert(END,'DateDue:\t\t'+ self.datedue_var.get()+ '\n')
        self.txtBox.insert(END,'DaysOnBook:\t\t'+ self.daysonbook_var.get()+ '\n')
        self.txtBox.insert(END,'LateRateFine:\t\t'+ self.lateratefine_var.get()+ '\n')
        self.txtBox.insert(END,'DateOverDue:\t\t'+ self.dateoverdue_var.get()+ '\n')
        self.txtBox.insert(END,'FinallPrice:\t\t'+ self.finallprice_var.get()+ '\n')


    def reset(self):
        self.member_var.set(''),
        self.id_var.set(''),
        self.prn_var.set(''),
        self.firstname_var.set(''),
        self.lastname_var.set(''),
        self.address1_var.set(''),
        self.address2_var.set(''),
        self.postcode_var.set(''),
        self.mobile_var.set(''),
        self.bookid_var.set(''),
        self.booktitle_var.set(''),
        self.auther_var.set(''),
        self.dateborrowed_var.set(''),
        self.datedue_var.set(''),
        self.daysonbook_var.set(''),
        self.lateratefine_var.set(''),
        self.dateoverdue_var.set(''),
        self.finallprice_var.set(''),
        self.txtBox.delete('1.0',END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno('library management system','do you want to exit')
        if iExit>0:
            self.root.destroy()
            return


    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=='':
            messagebox.showerror('Error','First select the member')
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='aflaque5',database='project')
            my_cursor=conn.cursor()
            query='delete from library where PRN_NO=%s'
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)
            
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()
            
            messagebox.showinfo('success','Member has been deleted')



if __name__ == '__main__':
    root=Tk()
    obj=LibraryMangementSystem(root)
    root.mainloop()