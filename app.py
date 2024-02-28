import customtkinter as ctk
from tkinter import *
import sqlite3
from tkinter import messagebox
from datetime import datetime




def create_patients_database():
    
    # Connect to SQLite database
    conn = sqlite3.connect('patients.db')
    #conn1 = sqlite3.connect('prescriptions.db')
    cursor = conn.cursor()
    #cursor1 = conn1.cursor()
    
    # Check if table 'patients' exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='patients'")
    table_exists = cursor.fetchone()
    
    if table_exists:
        print("Table 'patients' already exists.")
    else:
        # Create table 'patients' if it doesn't exist
        cursor.execute('''CREATE TABLE patients (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            FirstName TEXT,
                            LastName TEXT,
                            DOB TEXT,
                            PhoneNumber TEXT,
                            Address TEXT UNIQUE,
                            Gender TEXT,
                            DATE TEXT
                          )''')
        print("Table 'patients' created.")
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

def create_medicine_database():
    # Connect to SQLite database
    conn = sqlite3.connect('medicine.db')
    #conn1 = sqlite3.connect('prescriptions.db')
    cursor = conn.cursor()
    #cursor1 = conn1.cursor()
    
    # Check if table 'patients' exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='medicine'")
    table_exists = cursor.fetchone()
    
    if table_exists:
        print("Table 'medicine' already exists.")
    else:
        # Create table 'medicine' if it doesn't exist
        cursor.execute('''CREATE TABLE medicine (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            Name TEXT,
                            Supplier TEXT,
                            Amount INTEGER,
                            Date TEXT
                          )''')
        print("Table 'medicine' created.")
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

def create_supplier_database():
    # Connect to SQLite database
    conn = sqlite3.connect('supplier.db')
    #conn1 = sqlite3.connect('prescriptions.db')
    cursor = conn.cursor()
    #cursor1 = conn1.cursor()
    
    # Check if table 'patients' exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='supplier'")
    table_exists = cursor.fetchone()
    
    if table_exists:
        print("Table 'supplier' already exists.")
    else:
        # Create table 'supplier' if it doesn't exist
        cursor.execute('''CREATE TABLE supplier (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            Name TEXT,
                            Address TEXT,
                            PhoneNumber TEXT,
                            Date TEXT
                          )''')
        print("Table 'supplier' created.")
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

create_patients_database()
create_medicine_database()
create_supplier_database()
        

class App(ctk.CTk): 
    def __init__(self):
        super().__init__()
        self.title('PMS - Pharmacy Management System')
        w_height = self.winfo_screenheight()
        w_width = self.winfo_screenwidth()
        self.geometry("%dx%d" % (w_width, w_height))
        self.minsize(600, 600)

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=2)
        
        #widgets
        self.frame1 = ctk.CTkFrame(self, width=200, height=w_height)
        self.frame1.grid(row=0, column=0, padx=(15,0), pady=(15,15), rowspan=8, sticky="nsew")
        self.frame1.grid_rowconfigure(12, weight=1)
        
        self.title1 = ctk.CTkLabel(self.frame1, text="PMS", font=("Bold", 36))
        self.title1.grid(row=0, column=0, padx=(100,100), pady=(30,10))

        self.label2 = ctk.CTkButton(self.frame1, text="New Patient", font=("", 14), command=self.new_patient)
        self.label2.grid(row=1, column=0, padx=20, pady=(50,10))

        self.label3 = ctk.CTkButton(self.frame1, text="Manage Medicines", font=("", 14), command=self.medicine)
        self.label3.grid(row=2, column=0, padx=20, pady=(10,10))

        self.label4 = ctk.CTkButton(self.frame1, text="Suppliers", font=("", 14))
        self.label4.grid(row=3, column=0, padx=20, pady=(10,10))

        self.label5 = ctk.CTkButton(self.frame1, text="Option4", font=("", 14))
        self.label5.grid(row=4, column=0, padx=20, pady=(10,10))

        self.label6 = ctk.CTkButton(self.frame1, text="Option5", font=("", 14))
        self.label6.grid(row=5, column=0, padx=20, pady=(10,10))
        
        self.label7 = ctk.CTkButton(self.frame1, text="Option5", font=("", 14))
        self.label7.grid(row=6, column=0, padx=20, pady=(10,10))

        self.label8 = ctk.CTkButton(self.frame1, text="Option5", font=("", 14))
        self.label8.grid(row=7, column=0, padx=20, pady=(10,10))

        self.label9 = ctk.CTkButton(self.frame1, text="Option5", font=("", 14))
        self.label9.grid(row=8, column=0, padx=20, pady=(10,10))

        self.label10 = ctk.CTkButton(self.frame1, text="Option5", font=("", 14))
        self.label10.grid(row=9, column=0, padx=20, pady=(10,10))

        self.label11 = ctk.CTkButton(self.frame1, text="Option5", font=("", 14))
        self.label11.grid(row=10, column=0, padx=20, pady=(10,10))

        self.label12 = ctk.CTkButton(self.frame1, text="Option5", font=("", 14))
        self.label12.grid(row=11, column=0, padx=20, pady=(10,10))

        self.label13 = ctk.CTkButton(self.frame1, text="Exit", font=("", 14))
        self.label13.grid(row=12, column=0, padx=20, pady=(10,10))


        self.after(0, lambda: self.wm_state('zoomed'))
        self.mainloop()

        
    def new_patient(self):

        button_list = [self.label2, 
                       self.label3, 
                       self.label4, 
                       self.label5, 
                       self.label6, 
                       self.label7, 
                       self.label8, 
                       self.label9, 
                       self.label10, 
                       self.label11, 
                       self.label12
                       ]

        

        for v in button_list:
            v.configure(state='disabled')

        def changeState():
            print(date_entry.get())
            
            for i in button_list:
                i.configure(state="normal")
        
        def inputPatientData():

            all_entries = [
            name_entry,
            surname_entry,
            dob_entry,
            phoneNumber_entry,
            address_entry,
            gender_entry,
            date_entry
            ]

            conn = sqlite3.connect('patients.db')
            cursor = conn.cursor()

            values = [entry.get() for entry in all_entries]

            cursor.execute("INSERT INTO patients (FirstName, LastName, DOB, PhoneNumber, Address, Gender, Date) VALUES (?, ?, ?, ?, ?, ?, ?)", values)
            conn.commit()

        def getAllPatients():
            # Connect to the SQLite database
            scrollable_frame = ctk.CTkScrollableFrame(treeview_frame, width=treeview_frame.winfo_screenwidth() - 790, height=treeview_frame.winfo_screenheight() - 200)
            scrollable_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
            conn = sqlite3.connect('patients.db')
            c = conn.cursor()

            # Retrieve all data from the table except id
            c.execute("PRAGMA table_info(patients)")
            columns = c.fetchall()
            column_names = [col[1] for col in columns if col[1] != 'id']

            c.execute(f"SELECT {','.join(column_names)} FROM patients")
            all_data = c.fetchall()
            
            # Close connection
            conn.close()

            Texts = ['        First Name', 'Last Name', 'Date Of Birth', 'Phone Number', 'Address', 'Gender' ,'Date']
            col_count = 0
            for i in Texts:
                textLabel = ctk.CTkLabel(scrollable_frame, text=i, font=("Bold", 24))
                textLabel.grid(row=0, column=col_count, padx=(10,10), pady=(20,20), sticky="nsew")
                col_count = col_count + 1

            # Create and display text labels for each entry
            for idx, row in enumerate(all_data):
                for col_idx, value in enumerate(row):
                    label = ctk.CTkLabel(scrollable_frame, text=f"{value}", padx=10, pady=5)
                    label.grid(row=idx+1, column=col_idx, sticky="nsew")




        new_patient_frame = ctk.CTkFrame(self, width=self.winfo_screenwidth(), height=self.winfo_screenheight())
        new_patient_frame.grid(row=0, column=1, padx=(15,15), pady=(15,15))
        new_patient_frame.grid_propagate(False)
        
        add_patient_frame = ctk.CTkFrame(new_patient_frame, width=350, height=new_patient_frame.winfo_screenheight() - 170)
        add_patient_frame.grid(row=0, column=0, padx=(15,15), pady=(15,40))
        add_patient_frame.grid_propagate(False)


        treeview_frame = ctk.CTkFrame(new_patient_frame, width=new_patient_frame.winfo_screenwidth() - 730, height=new_patient_frame.winfo_screenheight() - 170)
        treeview_frame.grid(row=0, column=1, padx=(15,15), pady=(15,40))
        treeview_frame.grid_propagate(False)

        treeview_frame.grid_columnconfigure(2, weight=1)
        treeview_frame.grid_columnconfigure((9, 3), weight=0)
        treeview_frame.grid_rowconfigure((20 , 1, 2), weight=2)

        # patient_tree = tb.Treeview(treeview_frame, bootstyle="success", columns=columns, show="headings")
        # patient_tree.heading('first_name', "First Name")
        # patient_tree.heading('sur_name', "SurName")
        # patient_tree.heading('date_of_birth', "DOB")
        # patient_tree.heading('phone_number', "Phone Number")
        # patient_tree.heading('address', "Address")
        # patient_tree.heading('date', "Date")


        name_label = ctk.CTkLabel(add_patient_frame, text="First Name", width=50, font=('Bold', 17), justify="left")
        name_entry = ctk.CTkEntry(add_patient_frame, placeholder_text="Name", width=200)
        name_label.grid(row=0, column=0, padx=(15,0), pady=(50,5), sticky="w")
        name_entry.grid(row=0, column=1, padx=(5,15), pady=(50,5))

        surname_label = ctk.CTkLabel(add_patient_frame, text="Last Name", width=50, font=('Bold', 17), justify="left")
        surname_entry = ctk.CTkEntry(add_patient_frame, placeholder_text="Last Name", width=200)
        surname_label.grid(row=1, column=0, padx=(15,0), pady=(5,5), sticky="w")
        surname_entry.grid(row=1, column=1, padx=(5,15), pady=(5,5))

        dob_label = ctk.CTkLabel(add_patient_frame, text="Date Of Birth", width=50, font=('Bold', 17), justify="left")
        dob_entry = ctk.CTkEntry(add_patient_frame, placeholder_text="DOB", width=200)
        dob_label.grid(row=2, column=0, padx=(15,0), pady=(5,5), sticky="w")
        dob_entry.grid(row=2, column=1, padx=(5,15), pady=(5,5))

        phoneNumber_label = ctk.CTkLabel(add_patient_frame, text="Telephone", width=50, font=('Bold', 17), justify="left")
        phoneNumber_entry = ctk.CTkEntry(add_patient_frame, placeholder_text="Phone Number", width=200)
        phoneNumber_label.grid(row=3, column=0, padx=(15,0), pady=(5,5), sticky="w")
        phoneNumber_entry.grid(row=3, column=1, padx=(5,15), pady=(5,5))

        address_label = ctk.CTkLabel(add_patient_frame, text="Address", width=50, font=('Bold', 17), justify="left")
        address_entry = ctk.CTkEntry(add_patient_frame, placeholder_text="Address", width=200)
        address_label.grid(row=4, column=0, padx=(15,0), pady=(5,5), sticky="w")
        address_entry.grid(row=4, column=1, padx=(5,15), pady=(5,5))

        def optionmenu_callback(choice):
            print("optionmenu dropdown clicked:", choice)

        address_label = ctk.CTkLabel(add_patient_frame, text="Select Gender", width=50, font=('Bold', 17), justify="left")
        address_label.grid(row=5, column=0, padx=(15,0), pady=(5,5), sticky="w")
        gender_entry = ctk.CTkOptionMenu(add_patient_frame, width=200,
                                       values=["Male", "Female"],
                                       command=optionmenu_callback)
        gender_entry.grid(row=5, column=1, padx=(5,15), pady=(5,5))
        gender_entry.set('Male')


        date_label = ctk.CTkLabel(add_patient_frame, text="Date", width=50, font=('Bold', 17), justify="left")
        current_date = datetime.now()
        mystr = StringVar()
        dateString = current_date.strftime("%d/ %m/ %y")
        mystr.set(dateString)
        date_entry = ctk.CTkEntry(add_patient_frame, state='disabled', textvariable=mystr, width=200)
        date_label.grid(row=6, column=0, padx=(15,0), pady=(5,5), sticky="w")
        date_entry.grid(row=6, column=1, padx=(5,15), pady=(5,5))

        submit_btn = ctk.CTkButton(add_patient_frame, text="Submit", command=inputPatientData)
        submit_btn.place(relx=0.5, rely=0.7, anchor=CENTER)

        get_patients_btn = ctk.CTkButton(add_patient_frame, text="Get All Patients", command=getAllPatients)
        get_patients_btn.place(relx=0.5, rely=0.75, anchor=CENTER)

        exit = ctk.CTkButton(new_patient_frame, text="Close", command=lambda:[changeState(), new_patient_frame.destroy()])
        exit.place(rely=0.95, relx=0.01)

        #run

    def medicine(self):
        button_list = [self.label2, 
                       self.label3, 
                       self.label4, 
                       self.label5, 
                       self.label6, 
                       self.label7, 
                       self.label8, 
                       self.label9, 
                       self.label10, 
                       self.label11, 
                       self.label12
                       ]

        supplier_value = []
        for v in button_list:
            v.configure(state='disabled')

        def changeState():    
            for i in button_list:
                i.configure(state="normal")

        def addSupplier():
            
            supplierAdd = ctk.CTkToplevel(self)
            supplierAdd.geometry('350x300')

            supplierName = ctk.CTkEntry(supplierAdd, placeholder_text="Name of the supplier...", width=200)
            supplierName.pack(pady=10)
            supplierAddress = ctk.CTkEntry(supplierAdd, placeholder_text="Address of the supplier",width=200)
            supplierAddress.pack(pady=10)
            supplierPhoneNumber = ctk.CTkEntry(supplierAdd, placeholder_text="Phone Number of the supplier",width=200)
            supplierPhoneNumber.pack(pady=10)
            current_date = datetime.now()
            mystr = StringVar()
            dateString = current_date.strftime("%d/ %m/ %y")
            mystr.set(dateString)
            date_entry = ctk.CTkEntry(supplierAdd, state='disabled', textvariable=mystr, width=200)
            date_entry.pack(pady=10)

            def addSupplierInfo():
                getName = supplierName.get()
                getAddress = supplierAddress.get()
                getPhoneNumber = supplierPhoneNumber.get()
                getDate = date_entry.get()
                

                conn = sqlite3.connect('supplier.db')
                c = conn.cursor()

                c.execute("INSERT INTO supplier (Name, Address, PhoneNumber, Date) VALUES (?,?,?,?)",(getName, getAddress, getPhoneNumber, getDate))
                c.execute("SELECT Name FROM supplier")
                names = c.fetchall()
                print(names)

                supplier_entry.configure(values=[row[0] for row in names])
                 
                conn.commit()
            
            
            btn = ctk.CTkButton(supplierAdd, text="Add Supplier", command=addSupplierInfo)
            btn.pack()

            supplierAdd.after(100, supplierAdd.lift)
            supplierAdd.mainloop()

        def addMedicine():
            all_entries = [
                medicine_name_entry,
                supplier_entry,
                medicine_amout_entry,
                medicine_date_entry
            ]

            conn = sqlite3.connect('medicine.db')
            cursor = conn.cursor()

            values = [entry.get() for entry in all_entries]

            cursor.execute("SELECT * FROM medicine")
            medicine_data = cursor.fetchall()
            print(medicine_data)
            
            if not medicine_data:
                cursor.execute("INSERT INTO medicine(Name, Supplier, Amount, Date) VALUES (?, ?, ?, ?)", values)  
                conn.commit()  
                print('Inserted New Data')
            else:
                print('Detected same medicine and supplier... changing amount of the medicine')
                addedamount = int(medicine_data[0][3]) + int(values[2])
                print(addedamount)
                cursor.execute('''UPDATE medicine SET Amount = ?
                                WHERE Name = ? AND Supplier = ?
                ''',(addedamount, values[0], values[1]))
                conn.commit()
                messagebox.showinfo("PMS - Info", "Detected same medicine and supplier, Just changing amount of medicine")
        
        

        conn = sqlite3.connect('supplier.db')
        c = conn.cursor()
        c.execute("SELECT Name FROM supplier")
        suppliers = c.fetchall()

         
        s_values= [
            row[0] for row in suppliers
        ]
        
        
        new_medicine_frame = ctk.CTkFrame(self, width=self.winfo_screenwidth(), height=self.winfo_screenheight())
        new_medicine_frame.grid(row=0, column=1, padx=(15,15), pady=(15,15))
        new_medicine_frame.grid_propagate(False)
        
        add_medicine_frame = ctk.CTkFrame(new_medicine_frame, width=350, height=new_medicine_frame.winfo_screenheight() - 170)
        add_medicine_frame.grid(row=0, column=0, padx=(15,15), pady=(15,40))
        add_medicine_frame.grid_propagate(False)

        medicine_name_label = ctk.CTkLabel(add_medicine_frame, text="Medicine", width=50, font=('Bold', 17), justify="left")
        medicine_name_entry = ctk.CTkEntry(add_medicine_frame, placeholder_text="Name Of The Medicine", width=200)
        medicine_name_label.grid(row=0, column=0, padx=(15,0), pady=(50,5), sticky="w")
        medicine_name_entry.grid(row=0, column=1, padx=(5,15), pady=(50,5))

        select_supplier_label = ctk.CTkLabel(add_medicine_frame, text="Choose Supplier ", width=50, font=('Bold', 15), justify="left")
        select_supplier_label.grid(row=3, column=0, padx=(15,0), pady=(5,5), sticky="w")
        supplier_entry = ctk.CTkOptionMenu(add_medicine_frame, width=200,
                                           values=s_values
                                       )
        supplier_entry.grid(row=3, column=1, padx=(5,15), pady=(5,5))
        supplier_entry.set('Choose Supplier')

        add_supplier = ctk.CTkButton(add_medicine_frame, text="Add Supplier", command=addSupplier)
        add_supplier.grid(row=4, column=1, padx=(5,15), pady=(5,35))

        medicine_amout_label = ctk.CTkLabel(add_medicine_frame, text="Quantity", width=50, font=('Bold', 17), justify="left")
        medicine_amout_entry = ctk.CTkEntry(add_medicine_frame, placeholder_text="Quantity Of The Medicine", width=200)
        medicine_amout_label.grid(row=4, column=0, padx=(15,0), pady=(50,5), sticky="w")
        medicine_amout_entry.grid(row=4, column=1, padx=(5,15), pady=(50,5))

        current_date = datetime.now()
        mystr = StringVar()
        dateString = current_date.strftime("%d/ %m/ %y")
        mystr.set(dateString)

        medicine_date_label = ctk.CTkLabel(add_medicine_frame, text="Date", width=50, font=('Bold', 17), justify="left")
        medicine_date_entry = ctk.CTkEntry(add_medicine_frame, state='disabled', textvariable=mystr, width=200)
        medicine_date_label.grid(row=5, column=0, padx=(15,0), pady=(5,5), sticky="w")
        medicine_date_entry.grid(row=5, column=1, padx=(5,15), pady=(5,5))

        myfont = ctk.CTkFont('Helvetica', size=20, weight="bold")

        add_medicine_btn = ctk.CTkButton(add_medicine_frame, text="Add Medicine", width=320, font=myfont, command=addMedicine)
        add_medicine_btn.place(relx=0.5, rely=0.3, anchor=CENTER)




        exit = ctk.CTkButton(new_medicine_frame, text="Close", command=lambda:[changeState(), new_medicine_frame.destroy()])
        exit.place(rely=0.95, relx=0.01)
        
App()

