from tkinter import *
from tkinter import ttk
import sqlite3  as db
from tkcalendar import DateEntry
import random as rand
def init():
    connectionObjn = db.connect("donation portal.db")
    curr = connectionObjn.cursor()
    query = '''
    create table if not exists expenses (
        date string,
        name string,
        title string,
        expense number
        )
    '''
    curr.execute(query)
    connectionObjn.commit()
def submitexpense():
    values=[dateEntry.get(),Name.get(),Title.get(),Expense.get()]
    print(values)
    Etable.insert('','end',values=values)
    connectionObjn = db.connect("donation portal.db")
    curr = connectionObjn.cursor()
    query = '''
    INSERT INTO expenses VALUES 
    (?, ?, ?, ?)
    '''
    curr.execute(query,(dateEntry.get(),Name.get(),Title.get(),Expense.get()))
    connectionObjn.commit()
def viewexpense():
    connectionObjn = db.connect("donation portal.db")
    curr = connectionObjn.cursor()
    query = '''
     select * from expenses
    '''
    total='''
    select sum(expense) from expenses
    '''
    curr.execute(query)
    rows=curr.fetchall()
    curr.execute(total)
    amount=curr.fetchall()[0]
    print(rows)
    print(amount)
    
    l=Label(root,text="Date\t  Name\t  Donation\t  Phone number",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white")
    l.grid(row=6,column=0,padx=7,pady=7)
    st=""
    for i in rows:
        for j in i:
            st+=str(j)+'\t'
        st+='\n'
    print(st)
    l=Label(root,text=st,font=('arial',12))
    l.grid(row=7,column=0,padx=7,pady=7)
init()
root=Tk()
root.title("Donation portal")
root.geometry('1200x800')
dateLabel=Label(root,text="Date",font=('times new roman',15,'bold'),bg="green",fg="white",width=15)
dateLabel.grid(row=0,column=0,padx=7,pady=7)
dateEntry=DateEntry(root,width=12,font=('arial',15,'bold'))
dateEntry.grid(row=0,column=1,padx=7,pady=7)
Name=StringVar()
nameLabel=Label(root, text="Name",font=('bookman old style',15,'bold'),bg="yellow",fg="black",width=15)
nameLabel.grid(row=1,column=0,padx=7,pady=7)
NameEntry=Entry(root,textvariable=Name,font=('arial',15,'bold'))
NameEntry.grid(row=1,column=1,padx=7,pady=7)
Title=StringVar()
titleLabel=Label(root, text="Donation type",font=('arial',15,'bold'),bg="yellow",fg="black",width=20)
titleLabel.grid(row=2,column=0,padx=20,pady=15)
titleEntry=Entry(root,textvariable=Title,font=('arial',15,'bold'))
titleEntry.grid(row=2,column=1,padx=20,pady=15)
Expense=IntVar()
expenseLabel=Label(root,text="Phone number",font=('arial',15,'bold'),bg="green",fg="white",width=12)
expenseLabel.grid(row=3,column=0,padx=7,pady=7)
expenseEntry=Entry(root,textvariable=Expense,font=('arial',15,'bold'))
expenseEntry.grid(row=3,column=1,padx=7,pady=7)
submitbtn=Button(root,command=submitexpense,text="Submit",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white",width=12 )
submitbtn.grid(row=4,column=0,padx=13,pady=13)
viewtn=Button(root,command=viewexpense,text="Show post",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white",width=12 )
viewtn.grid(row=4,column=1,padx=30,pady=30)
Elist=['Date','Name','Donation','Phone number']
Tile=IntVar()
plist=["Beware of little expenses. A small leak will sink a great ship.","Save money for your future","Waste of time is the most extravagant and costly of all expenses."]
TileLabel=Label(root,text=rand.choice(plist),font=('arial',15,'bold'),bg="green",fg="white",width=50)
TileLabel.grid(row=30,column=1,padx=20,pady=20)
Etable=ttk.Treeview(root,column=Elist,show='headings',height=7)
for c in Elist:
    Etable.heading(c,text=c.title())
Etable.grid(row=5,column=0,padx=7,pady=7,columnspan=3)
mainloop()

