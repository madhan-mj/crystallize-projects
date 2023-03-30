from tkinter import *
import random


class Bill_App :

    #Title of the project

    def __init__(self, root) :
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing System of Crystallize")
        bg_color = "Blue"
        title = Label(self.root, text="BILLING SYSTEM OF CRYSTALLIZE", font=("Engravers MT", 30, "bold"), pady = 2, bd=12, bg= "white", fg= "black", relief=GROOVE)
        title.pack(fill=X)

    # Customer Details
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        # x= random.randint(1000,9999)
        # self.bill_no.set(str(x)) 
        self.search_bill = StringVar()


    # Customer retailing details
        f1 = LabelFrame(self.root, text="Customer Details", font=("times new roman", 9,"bold"), bd=10 , bg="white", fg="black")
        f1.place(x=0,y=80, relwidth=1)  
# Customer Name
        cname_lbl = Label(f1, text="Costumer Name", bg="#C0C0C0" , font=("times new roman",12,"bold"))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5) 

        cname_txt =Entry(f1,width=15, textvariable=self.c_name, font=("arial",10), bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

#Customer Phone NO
        cph_lbl = Label(f1, text="Costumer Phone", bg="#C0C0C0" , font=("times new roman",12,"bold"))
        cph_lbl.grid(row=0, column=2, padx=20, pady=5) 

        cph_txt =Entry(f1,width=15, textvariable=self.c_phone, font=("arial",10), bd=7, relief=GROOVE)
        cph_txt.grid(row=0, column=3, pady=5, padx=10)

        cbl_lbl = Label(f1, text="Bill Number", bg="#C0C0C0" , font=("times new roman",12,"bold"))
        cbl_lbl.grid(row=0, column=4,padx=20, pady=5) 

#Bill NUmber
        bilno_txt =Entry(f1,width=15, textvariable=self.bill_no, font=("arial",10), bd=7, relief=GROOVE)
        bilno_txt.grid(row=0, column=5, pady=5, padx=10)
# Search Button
        bil_btn  =Button(f1 ,width=15, text= "Search", bg="#C0C0C0", fg="black",command=self.search_bill, font=("arial",10), bd=7, relief=GROOVE)
        bil_btn.grid(row=0,column=6, padx=10, pady=5)


root = Tk()
obj = Bill_App(root)

root.mainloop()
