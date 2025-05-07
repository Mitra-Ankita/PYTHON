import os
from tkinter import *
import random
from tkinter import messagebox
root=Tk()
root.title('billing slip')
root.geometry('1280x720')
bg_color='#4D0039'
#===========Variable=======
c_name=StringVar()
c_phone=StringVar()
item=StringVar()
Rate=IntVar()
Quantity=IntVar()
bill_no=StringVar()
x=random.randint(1000,9999)
bill_no.set(str(x))



items_list = []

def welcome():
    textarea.delete(1.0,END)
    textarea.insert(END,"\t Welcome To My Shop")
    textarea.insert(END,f'\n\nBill Number:\t\t{bill_no.get()}')
    textarea.insert(END,f'\nCustomer Name:\t\t{c_name.get()}')
    textarea.insert(END,f'\nPhone Number:\t\t{c_phone.get()}')
    textarea.insert(END,f'\n======================================')
    textarea.insert(END,'\nProduct              QTY       Price')
    textarea.insert(END, f'\n======================================')
    textarea.configure(font=("Courier New", 15, "bold"))

def additm():
    n = Rate.get()
    m = Quantity.get() * n
    if item.get() == '':
        messagebox.showerror('Error', 'please enter an item')
    else:
        items_list.append((item.get(), Quantity.get(), m))
        # Format product line with fixed width columns for alignment
        product_line = f'\n{item.get():<20}{Quantity.get():<10}{m:<10}'
        textarea.insert(END, product_line)

def gbill():
    if c_name.get() == '' or c_phone.get() == '':
        messagebox.showerror('Error', 'Customer Details are must')
    else:
        welcome()
        # Insert all items from items_list
        for prod, qty, price in items_list:
            product_line = f'\n{prod:<20}{qty:<10}{price:<10}'
            textarea.insert(END, product_line)
        textarea.insert(END, f'\n======================================')
        # Format total payable amount line with alignment
        total_line = f'\nTotal Paybil Amount:{"":<10}{sum(price for _, _, price in items_list):<10}'
        textarea.insert(END, total_line)
        #textarea.insert(END, f'\n======================================')
        savebill()

def savebill():
    op=messagebox.askyesno('Save bill','Do you want to save the bill')
    if op>0:
        if not os.path.exists("bills"):
            os.makedirs("bills")
        bill_details=textarea.get(1.0,END)
        f1=open("bills/"+str(bill_no.get())+".txt",'w')
        f1.write(bill_details)
        f1.close()
        messagebox.showinfo('saved',f'Bill no:{bill_no.get()} Saved successfully')
    else:
        return

def clear():
    c_name.set('')
    c_phone.set('')
    item.set('')
    Rate.set(0)
    Quantity.set(0)
    welcome()


def exit():
    op=messagebox.askyesno('Exit','Do you want to exit')
    if op>0:
        root.destroy()

#=======Top Section===============
title=Label(root,text='Billing Software',bg=bg_color,fg='white',font=('times new romman',25,'bold'),relief=GROOVE,bd=12)
title.pack(fill=X)

#==============Customer Details==========

F1=LabelFrame(root,text='Customer Details',font=('time new romman',18,'bold'),relief=GROOVE,bd=10,bg=bg_color,fg='gold')
F1.place(x=0,y=80,relwidth=1)

cname_lbl=Label(F1,text='Customer Name',font=('time new romman',18,'bold'),bg=bg_color,fg='white')
cname_lbl.grid(row=0,column=0,padx=10,pady=5)
cname_txt=Entry(F1,width=15,font='arial 15 bold',relief=SUNKEN,textvariable=c_name)
cname_txt.grid(row=0,column=1,padx=10,pady=5)


cphone_lbl=Label(F1,text='Phone Number',font=('time new romman',18,'bold'),bg=bg_color,fg='white')
cphone_lbl.grid(row=0,column=2,padx=10,pady=5)
cphone_txt=Entry(F1,width=15,font='arial 15 bold',relief=SUNKEN,textvariable=c_phone)
cphone_txt.grid(row=0,column=3,padx=10,pady=5)

#=======Product Details========
F2=LabelFrame(root,text='Product Details',font=('time new romman',18,'bold'),relief=GROOVE,bd=10,bg=bg_color,fg='gold')
F2.place(x=20,y=180,width=630,height=500)


itm=Label(F2,text='Product Name',font=('times new romman',18,'bold'),bg=bg_color,fg='lightgreen')
itm.grid(row=0,column=0,padx=30,pady=20)
itm_txt=Entry(F2,width=20,font='arial 15 bold',textvariable=item)
itm_txt.grid(row=0,column=1,padx=30,pady=20)

rate=Label(F2,text='Product Rate',font=('times new romman',18,'bold'),bg=bg_color,fg='lightgreen')
rate.grid(row=1,column=0,padx=30,pady=20)
rate_txt=Entry(F2,width=20,font='arial 15 bold',textvariable=Rate)
rate_txt.grid(row=1,column=1,padx=30,pady=20)

quantity=Label(F2,text='Product Quantity',font=('times new romman',18,'bold'),bg=bg_color,fg='lightgreen')
quantity.grid(row=2,column=0,padx=30,pady=20)
quantity_txt=Entry(F2,width=20,font='arial 15 bold',textvariable=Quantity)
quantity_txt.grid(row=2,column=1,padx=30,pady=20)

#==========button===============
btn1=Button(F2,text='Add Item',font='arial 15 bold',padx=5,pady=10,bg='lime',width=15,command=additm)
btn1.grid(row=3,column=0,padx=10,pady=30)

btn2=Button(F2,text='Generate Bill',font='arial 15 bold',padx=5,pady=10,bg='lime',width=15,command=gbill)
btn2.grid(row=3,column=1,padx=10,pady=30)

btn3=Button(F2,text='Clear',font='arial 15 bold',padx=5,pady=10,bg='lime',width=15 ,command=clear)
btn3.grid(row=4,column=0,padx=10,pady=30)

btn3=Button(F2,text='Exit',font='arial 15 bold',padx=5,pady=10,bg='lime',width=15,command=exit)
btn3.grid(row=4,column=1,padx=10,pady=30)


#=============bill area=========
F3=Frame(root,relief=GROOVE,bd=10)
F3.place(x=700,y=180,width=500,height=500)


bill_title=Label(F3,text='Bill Area',font='arial 15 bold',relief=GROOVE,bd=7).pack(fill=X)
scroll_y=Scrollbar(F3,orient=VERTICAL)
textarea=Text(F3,yscrollcommand=scroll_y)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack()
welcome()



root.mainloop()