# import mysql.connector
from ast import Pass
from json import load
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
import tkinter as tk
from tkinter import ttk


from time import strftime
from datetime import datetime
import tkinter as tk
import sqlite3

#initialize app
root = tk.Tk()
root.title("Ese Flow")

root.configure(bg="black")
root.geometry("1400x700")


# here I set the custom color
def change_color():
    #colornew = "#234575"
    colornew = "#222023"
    return colornew

bg_colour = change_color()

top_frame = tk.Frame(root,width=700, height=100, bg="#234575", border=20)
top_frame.grid(row=0, column=0)

top_frame2 = tk.Frame(root,width=700, height=100, bg="#234575", border=20)
top_frame2.grid(row=0, column=1)

            # window frame 
window1 =  tk.Frame(root, width=700, height=550, bg=bg_colour)
window1.grid(row=1, column=0)
            # window frame 
window2 =  tk.Frame(root, width=700, height=550, bg=bg_colour)
window2.grid(row=1, column=1)
            # window frame 
            
            # window frame 
window3 =  tk.Frame(root, width=700, height=550, bg=bg_colour)
window3.grid(row=1, column=0)

window4 =  tk.Frame(root, width=700, height=550, bg=bg_colour)
window4.grid(row=1, column=1)
            
# Here I added a Label to display text
tk.Label(top_frame,
        text=" Student Management System ",
        bg="#234575",
         fg="#ffffff",
        font=("arial", 26, "bold")
        ).place(x=40, y=35)

#  ============================ TIME DISPLAY STARTS HERE ====================== 
# Time function and Label starts here 
def time():
    string = strftime("CodeWith-Ese Time: " + '%H:%M:%S %p     %d-%m-%y')
    label.config(text=string)
    label.after(1000, time)
    
label = tk.Label(root, font=("ds-digital", 14), background= "#234575", foreground= "greenyellow", width=40)
label.place(x=980, y=84, anchor='center')
time()

# ========================= Database =============================================
 
def create_table():
    conn = sqlite3.connect('ese_store.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS ese_savings
                (product TEXT, date TEXT, cost REAL, quantity INTEGER)''')
    conn.commit()
    conn.close()

def add_product():
    print()

def clear_widgets(frame):
    for widget in frame.winfo_children():
        
        widget.destroy()
        

def load_window1():
    # clear_widgets(frame1)
    # clear_widgets(frame2)
    clear_widgets(window3)
    window1.tkraise()
   # window2.tkraise()
   # window1.pack_propagate(False)
            

    # THIS CODE WILL DELETE THE STUDENT INFOMATION TABLE
    # UN COMMENT IT TO DELETE THE CONTENT IN ORDER TO START INSERT YOUR OWN CONTENT
    # def delete_student():
    #    conn = sqlite3.connect('studentManagement.db')
    #    c = conn.cursor()
    # #    c.execute("DELETE FROM student_info WHERE ID = 44")
    #    c.execute("DROP TABLE student_info")
    #    c.fetchmany()
    #    conn.close()
    
    # delete_student()
    
    def create_student_table():
        conn = sqlite3.connect('studentManagement.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS student_info
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    firstname TEXT NOT NULL, lastname TEXT NOT NULL,
                    mothername TEXT NOT NULL, address TEXT NOT NULL,
                    email TEXT NOT NULL, gender TEXT NOT NULL, birthday INTEGER NOT NULL )''')
        conn.commit()
        conn.close()
    create_student_table()
                
    def add_student():
        if student_name.get():
            try:
                firstn =  student_name.get().capitalize()
                lastn = student_lastName_entry.get().capitalize()
                mothern = student_mothers.get().capitalize()
                address = student_address_entry.get().title()
                emailn = student_email_entry.get()
                gend = gender_entry.get().title()
                birth = int(birt_day_entry.get())
                
                
                date2 = datetime.now().strftime(f" %d-%m-%Y   %H:%M:%p   ")
                date = date2
                
                conn = sqlite3.connect('studentManagement.db')
                c = conn.cursor()
                c.execute("INSERT INTO student_info (firstname, lastname, mothername, address, email, gender, birthday) VALUES (?, ?, ?, ?, ?, ?, ?)", (firstn, lastn, mothern, address, emailn, gend, birth))
                conn.commit()
                conn.close()
            
                # --------- writing to a text file------------- 
                # dba = open("student_Informaton.txt", "w")
                dba = open("student_Informaton.txt", "a")
                dba.write("\n")
                dba.write(f"---  Registration Date:  {date}  ---\n ")
                dba.write(f"---  Student Information\n ".upper())
                dba.write("\n")
                dba.write(f"---  First Name:    {firstn}\n ")
                dba.write(f"---  Last Name:     {lastn}\n")
                dba.write(f"---  Address:       {address}\n ")
                dba.write(f"---  Email ID:      {emailn}\n ")
                dba.write(f"---  Gender:        {gend}\n ")
                # dba.write(f"---  Birth Day:     {birth}\n ")
                dba.write("\n")
                dba.close()
                
                # --------- writing to a text file------------- 
                conplete_student_textfile = open("student_personal.txt", "a")
                conplete_student_textfile.write("\n")
                conplete_student_textfile.write(f"--- Regiration Date   {date}  \n ")
                conplete_student_textfile.write(f" Student Personal Information\n ".upper())
                conplete_student_textfile.write("\n")
                conplete_student_textfile.write(f"---   First Name:     {firstn}\n ")
                conplete_student_textfile.write(f"---   Last Name:      {lastn}\n")
                conplete_student_textfile.write(f"---   Mother's Name:  {mothern}\n ")
                conplete_student_textfile.write(f"---   Address:        {address}\n ")
                conplete_student_textfile.write(f"---   Email ID:       {emailn}\n ")
                conplete_student_textfile.write(f"---   Gender:         {gend}\n ")
                conplete_student_textfile.write(f"---   Birth Day:      {birth}\n ")
                conplete_student_textfile.write("\n")
                conplete_student_textfile.close()
                
                # -----------------------------------------  
                                
                student_name.delete(0, "end")
                student_name.insert(0, "First Name") 
                
                student_lastName_entry.delete(0, "end")
                student_lastName_entry.insert(0, "Last Name ") 
                
                student_mothers.delete(0, "end")
                student_mothers.insert(0, "Mother's Name")
                
                
                student_address_entry.delete(0, "end")
                student_address_entry.insert(0, "Address")
                
                student_email_entry.delete(0, "end")
                student_email_entry.insert(0, "Email")
                
                gender_entry.delete(0, "end")
                gender_entry.insert(0, "Gender")
                
                birt_day_entry.delete(0, "end")
                birt_day_entry.insert(0, "Birth")
                
                show_studen_information()
                
                # clear_widgets(window2)
                
                messagebox.showinfo("Success", f" {firstn} {lastn} File Created Successfully")

            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please fill in the entry box to add data")

    student_info_lable = tk.Label(
        window1,
        text="STUDENT INFORMATION ",
        font=("ds-digital", 12),  bg=bg_colour, foreground= "red",
        ).place(x=400, y=25)

    #-------------------------------
    # student's ID Entry starts here 

    def on_enterId(e):
        studend_id.delete(0, "end")

    def on_leavID(e):
        var_id = studend_id.get()
        if var_id=="":
            studend_id.insert(0," Student's ID") 
            
    studend_id = tk.Entry(window1, bg="#876543", fg="white", width=12,border=4, font=("TkHeadFont", 12))
    studend_id.place(x=160, y=50)
    studend_id.insert(0, " Student's ID")
    studend_id.bind("<FocusIn>", on_enterId)
    studend_id.bind("<FocusOut>", on_leavID)

    #=================================== lebel for item 1 ===========================
    tk.Label(
        window1,
        text="Student's Id",
        bg=bg_colour,
        fg="white",
        
        font=("ds-digital",14)
        ).place(x=20, y=50)
    
    #=================================== Entry ===========================
    # student's Name Entry starts here 
    
    def on_enterName(e):
        student_name.delete(0, "end")

    def on_leavName(e):
        var_name = student_name.get()
        if var_name=="":
            student_name.insert(0," First Name") 
            
    student_name = tk.Entry(window1, bg="#876543", fg="white", width=12,border=4, font=("TkHeadFont", 12))
    student_name.place(x=160, y=100)
    student_name.insert(0, " First Name ")
    student_name.bind("<FocusIn>", on_enterName)
    student_name.bind("<FocusOut>", on_leavName)

    #=================================== lebel for item 1 ===========================
    tk.Label(
        window1,
        text="First Name",
        bg=bg_colour,
        fg="white",
        
        font=("ds-digital",14)
        ).place(x=20, y=100)
    
    #=================================== Entry ===========================   
    # student's Last Name Entry starts here 
    def on_enter_lastName(e):
        student_lastName_entry.delete(0, "end")

    def on_leav_lastName(e):
        var_lastN = student_lastName_entry.get()
        if var_lastN=="":
            student_lastName_entry.insert(0," Last Name") 
            
    student_lastName_entry = tk.Entry(window1, bg="#876543", fg="white", width=12,border=4, font=("TkHeadFont", 12))
    student_lastName_entry.place(x=160, y=150)
    student_lastName_entry.insert(0, " Last Name ")
    student_lastName_entry.bind("<FocusIn>", on_enter_lastName)
    student_lastName_entry.bind("<FocusOut>", on_leav_lastName)

    
    #=================================== lebel for item 1 ===========================
    tk.Label(
        window1,
        text="Last Name",
        bg=bg_colour,
        fg="white",
        
        font=("ds-digital",14)
        ).place(x=20, y=150)
    
    #=================================== Entry ===========================
    def on_enter_mothers(e):
        student_mothers.delete(0, "end")

    def on_leaveMother(e):
        var_mother = student_mothers.get()
        if var_mother=="":
            student_mothers.insert(0," Last Name") 
            
    student_mothers = tk.Entry(window1, bg="#876543", fg="white", width=12,border=4, font=("TkHeadFont", 12))
    student_mothers.place(x=160, y=200)
    student_mothers.insert(0, " Mother's Name ")
    student_mothers.bind("<FocusIn>", on_enter_mothers)
    student_mothers.bind("<FocusOut>", on_leaveMother)

    #=================================== lebel for item 1 ===========================

    tk.Label(
        window1,
        text="Mother's Name",
        bg=bg_colour,
        fg="white",
        
        font=("ds-digital",14)
        ).place(x=20, y=200)
    #=================================== Entry ===========================
    
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
    # student's Address Entry starts here 
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def on_enter_address(e):
        student_address_entry.delete(0, "end")

    def on_leav_address(e):
        var_mother = student_address_entry.get()
        if var_mother=="":
            student_address_entry.insert(0," Address") 
            
    student_address_entry = tk.Entry(window1, bg="#876543", fg="white", width=12,border=4, font=("TkHeadFont", 12))
    student_address_entry.place(x=160, y=250)
    student_address_entry.insert(0, " Address ")
    student_address_entry.bind("<FocusIn>", on_enter_address)
    student_address_entry.bind("<FocusOut>", on_leav_address)

    #=================================== lebel for item 1 ===========================

    tk.Label(
        window1,
        text="Address",
        bg=bg_colour,
        fg="white",
        
        font=("ds-digital",14)
        ).place(x=20, y=250)
    #=================================== Entry ===========================
    
    
        
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
    # student's Email  Entry starts here 
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def on_enter_email(e):
        student_email_entry.delete(0, "end")

    def on_leav_email(e):
        var_email = student_email_entry.get()
        if var_email=="":
            student_email_entry.insert(0," Email") 
            
    student_email_entry = tk.Entry(window1, bg="#876543", fg="white", width=12,border=4, font=("TkHeadFont", 12))
    student_email_entry.place(x=160, y=300)
    student_email_entry.insert(0, " Email ")
    student_email_entry.bind("<FocusIn>", on_enter_email)
    student_email_entry.bind("<FocusOut>", on_leav_email)

    #=================================== lebel for item 1 ===========================

    tk.Label(
        window1,
        text="Email :",
        bg=bg_colour,
        fg="white",
        
        font=("ds-digital",14)
        ).place(x=20, y=300)
    #=================================== Entry ===========================
    
    
            
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
    # student's Gender  Entry starts here 
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def on_enter_gender(e):
        gender_entry.delete(0, "end")

    def on_leave_gender(e):
        var_gender = gender_entry.get()
        if var_gender=="":
            gender_entry.insert(0," Gender") 
            
    gender_entry = tk.Entry(window1, bg="#876543", fg="white", width=12,border=4, font=("TkHeadFont", 12))
    gender_entry.place(x=160, y=350)
    gender_entry.insert(0, " Gender ")
    gender_entry.bind("<FocusIn>", on_enter_gender)
    gender_entry.bind("<FocusOut>", on_leave_gender)

    #=================================== lebel for item 1 ===========================

    tk.Label(
        window1,
        text="Gender :",
        bg=bg_colour,
        fg="white",
        
        font=("ds-digital",14)
        ).place(x=20, y=350)
    #=================================== Entry ===========================
    
                
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
    # student's Date of Birth  Entry starts here 
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def on_enter_birthday(e):
        birt_day_entry.delete(0, "end")

    def on_leav_birthday(e):
        var_birtday = birt_day_entry.get()
        if var_birtday=="":
            birt_day_entry.insert(0," Date of Birth") 
            
    birt_day_entry = tk.Entry(window1, bg="#876543", fg="white", width=12,border=4, font=("TkHeadFont", 12))
    birt_day_entry.place(x=160, y=400)
    birt_day_entry.insert(0, " Date of Birth ")
    birt_day_entry.bind("<FocusIn>", on_enter_birthday)
    birt_day_entry.bind("<FocusOut>", on_leav_birthday)

    #=================================== lebel for item 1 ===========================

    tk.Label(
        window1,
        text="Date of Birth :",
        bg=bg_colour,
        fg="white",
        
        font=("ds-digital",14)
        ).place(x=20, y=400)
     
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
    # ADMIN BUTTON starts here 
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    #=================================== lebel for item 1 ==========================
    
    Create_button = tk.Button(
        window1,
        text="SAVE",
        bg="black",
        fg="white",
        font=("TkVersion", 10),
        cursor= "hand2",
        width=12,
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:add_student()).place(x=160, y=460) 
    #=================================== Entry ===========================
    admin = tk.Button(
        window1,
        text="ADMIN ONLY",
        bg="black",
        fg="white",
        font=("TkVersion", 10),
        cursor= "hand2",
        width=12,
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_window3()).place(x=160, y=500) 
    

    
    #==== STUDENT INFOMATION ========  
    def show_studen_information():
        conn = sqlite3.connect('studentManagement.db')
        c = conn.cursor()
        # c.execute("SELECT * FROM student_info ")
        c.execute("SELECT (ID),(firstname),(lastname),(gender),(birthday) FROM student_info")
        rows = c.fetchall()
        conn.close()
        
        list_view2.delete(0, tk.END)
        for row in rows:
            list_view2.insert(tk.END, row)
            # list_view2.insert(tk.END, row)
    
    list_scroll = tk.Scrollbar(window1)
    list_scroll.place(x=652, y=50, height=410)

    list_view2 = tk.Listbox(window1, bg="black", fg="cyan", font=("ds-digital", 12), width= 31, height=21, border=5)#  bg="#658765",
    list_view2.place(x=360, y=50)
    
    list_scroll.config(command=list_view2.yview)
    
    show_studen_information()
   
    

    profile_label = tk.Label(
        window1, width=40, height=3,
        border=4, bg="white",).place(x=360, y=470)
    


load_window1()

def load_window2():
    clear_widgets(window4)
    window2.tkraise()
    window2.pack_propagate(False)

    #================================
    # @ DISPLAY STUDENT INFOMATION  @

    def open_text():
        # text_file = open("dbaz.txt", "r")
        text_file = open("student_Informaton.txt", "r")
        stuff = text_file.read()
        
        my_textfile.insert("end", stuff)
        
        text_file.close()

    text_scroll= tk.Scrollbar(window2)
    text_scroll.place(x=477, y=50, height=408)

    my_textfile = tk.Text(window2, width=51, height=22, bg="black", fg="cyan", font=("ds-digital", 12), border=5)
    my_textfile.place(x=5, y=50)
    text_scroll.config(command=my_textfile.yview)

    file_button = tk.Button(
        window2,
        text="OPEN",
        bg="black",
        fg="white",
        font=("TkVersion", 10),
        cursor= "hand2",
        width=16,
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:open_text()).place(x=5, y=465) 


    def exitApp():
            root.destroy()
            
    exit_button = tk.Button(
        window2,
        text="EXIT",
        bg="black",
        fg="white",
        font=("TkVersion", 10),
        cursor= "hand2",
        width=16,
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:exitApp()).place(x=170, y=465)
    
    back_window4 = tk.Button(
        window2,
        text="WIDOW 4 ",
        bg="black",
        fg="white",
        font=("TkVersion", 10),
        cursor= "hand2",
        width=16,
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_window4()).place(x=335, y=465) 
    
load_window2()

#------------------------- window 3 starts here ---------------------------
def load_window3():
    # clear_widgets(frame1)
    # clear_widgets(frame2)
    clear_widgets(window1)
 
    window3.tkraise()
    window3.pack_propagate(False)
    
    # Here I added a Label to display text
    tk.Label(window3,
            text=" ADMIN DASHBOAD   ",
            bg=bg_colour,
            fg="YELLOW",
            font=("arial", 27, "bold")
            ).place(x=170, y=25)

    #----------------------display complete student information ---------------------------
    def show_complete_studen_information():
        text_file = open("student_personal.txt", "r")
        stuff = text_file.read()
        stock_textfile.insert("end", stuff)
        
        text_file.close()

    text_scroll= tk.Scrollbar(window3)
    text_scroll.place(x=665, y=70, height=300)

    stock_textfile = tk.Text(window3, width=70, height=16, bg="black", fg="cyan", font=("ds-digital", 12), border=5)
    stock_textfile.place(x=20, y=70)
    text_scroll.config(command=stock_textfile.yview)
    

    # Amount  Entry starts here 
    #-----------------------------
    def on_enter_cost_price1(e):
        stock_cost_enter.delete(0, "end")

    def on_leave_sale_price1(e):
        qant2a = stock_cost_enter.get()
        if qant2a=="":
            stock_cost_enter.insert(0," Search for Student ") 
            
    stock_cost_enter = tk.Entry(window3, bg="#675432", fg="white", width=20,border=2, font=("TkHeadFont", 10))
    stock_cost_enter.place(x=355, y=380)
    stock_cost_enter.insert(0, "  Search for Student ")
    stock_cost_enter.bind("<FocusIn>", on_enter_cost_price1)
    stock_cost_enter.bind("<FocusOut>", on_leave_sale_price1)

    tk.Label(
        window3,
        text="Search Student",
        bg=bg_colour,
        fg="red",
        
        font=("ds-digital",12)
        ).place(x=220, y=380)
    
 
    button_open_file = tk.Button(
        window3,
        text="OPEN FILE ",
        bg="black",
        fg="white",
        font=("TkVersion", 10),
        cursor= "hand2",
        width=14,
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:show_complete_studen_information()).place(x=80, y=380) 
    
    back_window1 = tk.Button(
        window3,
        text="BACK TO HOME",
        bg="black",
        fg="white",
        font=("TkVersion", 10),
        cursor= "hand2",
        width=14,
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_window1()).place(x=80, y=420) 
    
    show_complete_studen_information()

# -------------------  END OF WINDOW 3 ----------------------
# -------------------  WINDOW 4 STARTS HERE -----------------

def load_window4():
    clear_widgets(window2)
    window4.tkraise()
    window4.pack_propagate(False)
    
    def show_contacts():
        conn = sqlite3.connect('studentManagement.db')
        c = conn.cursor()
        c.execute("SELECT * FROM student_info ")
        rows = c.fetchall()
        conn.close()
        list_view2.delete(0, tk.END)
        for row in rows:
            list_view2.insert(tk.END, row)
            # list_view2.insert(tk.END, row)

    list_scroll = tk.Scrollbar(window4)
    list_scroll.place(x=530, y=50, height=300)


    list_view2 = tk.Listbox(window4, bg="black", fg="cyan", font=("ds-digital", 12), width=50, height=8)#  bg="#658765",
    list_view2.place(x=20, y=50)

    list_scroll.config(command=list_view2.yview)
    
    show_contacts()
        
    back_window1 = tk.Button(
        window4,
        text="WIDOW 2 ",
        bg="black",
        fg="white",
        font=("TkVersion", 12),
        cursor= "hand2",
        width=15,
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_window2()).place(x=360, y=450) 
          
#------------------- TOTAL STOCK CODE HERE -------------------      
    def show_total_stock():
        conn = sqlite3.connect('ese_store.db')
        c = conn.cursor()
        
         # total monthly_sale 
        total_stock= "select total(quantity) from ese_store"
        c.execute(total_stock) 
        global total_display
        total_display = (c.fetchone()[0])
        conn.close()
        
    show_total_stock()
    
    def all_stack():
        global total_stock_list
        total_stock_list = tk.Listbox(window4, bg="#222", fg="white", width=10, height=1, border=5, font=("TkHeadFont", 12))
        total_stock_list.place(x=130, y=280)    
        #total_stock_list.insert(0, "$")
        total_stock_list.delete(0, "end")
        total_stock_list.insert(0, total_display)
        
        tk.Label(
            window4,
            text="Total Stock ",
            bg=bg_colour,
            fg="white",
            
            font=("ds-digital",12)
            ).place(x=20, y=280)

    all_stack()

    def show_total_cost():
        conn = sqlite3.connect('ese_store.db')
        c = conn.cursor()
        
         # total monthly_sale 
        total_cost= "select total(cost) from ese_store"
        c.execute(total_cost) 
        global total_cost_display
        total_cost_display = (c.fetchone()[0])
        conn.close()
        
    show_total_cost()
    
    def all_stackTotal():
        global total_s_costL
        total_s_costL = tk.Listbox(window4, bg="#222", fg="white", width=10, height=1, border=5, font=("TkHeadFont", 12))
        total_s_costL.place(x=130, y=330)    
        #total_s_costL.insert(0, "$")
        total_s_costL.delete(0, "end")
        total_s_costL.insert(0, total_cost_display)
        
        tk.Label(
            window4,
            text="Total COST ",
            bg=bg_colour,
            fg="white",
            
            font=("ds-digital",12)
            ).place(x=20, y=330)

    all_stackTotal()

#load_window3()

#      Author: by Monday Eseinone Completed 18th March, 2024. 
#####***********************###************ 
autor = tk.Label(window2, font=("ds-digital", 8), text="Created By Monday Eseinone", border=2, background= bg_colour, foreground= "white" )
autor.place(x=20, y=500)

author_email_address = tk.Label(window2, font=("ds-digital", 8), text="Email: eeseinone@gmail.com", background= bg_colour, foreground= "yellow" )
author_email_address.place(x=180, y=500)

author_address = tk.Label(window2, font=("ds-digital", 8), text="Contact: +234 8075236542", background= bg_colour, foreground= "red" )
author_address.place(x=330, y=500)

# ===================== Time Display and Author stops here ============================

root.mainloop()