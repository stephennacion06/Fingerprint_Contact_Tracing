from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as font

from animations.windows_gui import ImageLabel

import time
from threading import *
# Function for clearing the
# contents of text entry boxes


root_win = None



def timer_window():
    # Call work function
    t1=Thread(target=work)
    t1.start()
  
# work function
def work():
    global root_win
    
    print("sleep time start")
  
    for i in range(5):
        print(i)
        time.sleep(1)
    
    root_win.destroy()
    root_win.update()
    
    print("sleep time stop")


def register_window():
    global root_win
    
    root_win = tk.Toplevel(bg="black")
    root_win.geometry("1024x350+0+50")
    root_win.overrideredirect(1)
    # root = tk.Tk()
    lbl = ImageLabel(root_win)
    lbl.pack()
    lbl.load('animations/ready_for_scan.gif')
    
    label_instruction = tk.Label(root_win, text="Place your finger on the fingerprint sensor for 5 times", 
                                 bg="black", fg="white")
    Font_tuple = ("Modern", 15, "bold")
    label_instruction.config(font = Font_tuple)
    label_instruction.pack()
    

def login_window():
    global root_win
    
    root_win = tk.Toplevel(bg="black")
    root_win.geometry("1024x350+0+50")
    root_win.overrideredirect(1)
    lbl = ImageLabel(root_win)
    lbl.pack()
    lbl.load('animations/ready_for_scan.gif')
    
    label_instruction = tk.Label(root_win, text="Place your finger on the fingerprint sensor", 
                                 bg="black", fg="white")
    Font_tuple = ("Modern", 15, "bold")
    label_instruction.config(font = Font_tuple)
    label_instruction.pack()



def clear():
    # clear the content of text entry box
    name_field.delete(0, END)
    email_field.delete(0, END)
    address_field.delete(0, END)
    gender_field.delete(0, END)
    phone_field.delete(0, END)
  
  
# window and write to an excel file
def insert():
    global root_win 
    
    
    # if user not fill any entry
    # then print "empty input"
    if (name_field.get() == "" and
        email_field.get() == "" and
        address_field.get() == "" and
        gender_field.get() == "" and
        phone_field.get() == ""):
              
        print("empty input")
  
    else:
  
        # assigning the max row and max column
        # value upto which data is written
        # in an excel sheet to the variable
        # current_row = sheet.max_row
        # current_column = sheet.max_column
  
        # # get method returns current text
        # # as string which we write into
        # # excel spreadsheet at particular location
        # sheet.cell(row=current_row + 1, column=1).value = name_field.get()
        # sheet.cell(row=current_row + 1, column=2).value = email_field.get()
        # sheet.cell(row=current_row + 1, column=3).value = address_field.get()
        # sheet.cell(row=current_row + 1, column=4).value = gender_field.get()
        # sheet.cell(row=current_row + 1, column=5).value = phone_field.get()
        # sheet.cell(row=current_row + 1, column=6).value = email_id_field.get()
        # sheet.cell(row=current_row + 1, column=7).value = address_field.get()
        print(gender_field.get())
        
        register_window()
        
        timer_window()
        
        #root_win.destroy()
        #root_win.update()
        
        
        name_field.focus_set()
        
        # call the clear() function
        clear()
  

def login_finger_process():
    global root_win
    
    login_window()
    
    timer_window()
    
    # Fingerprint Scanning here
    

if __name__ == "__main__":
      
    # create a GUI window
    root = Tk()
  
    # set the background colour of GUI window
    root.configure(background='light green')
  
    # set the title of GUI window
    root.title("CONTACT TRACING")
  
    # set the configuration of GUI window
    win_w = 1024
    win_h = 400
    window_size= str(win_w) + "x" + str(win_h)
    root.geometry(window_size)
    root.attributes("-fullscreen", True) 
    
    header_section =Frame(root,width=win_w,height=50,bg="#272343")
    header_section.place(x=0,y=0)
    
    title_head = "FINGERPRINT CONTACT TRACING SYSTEM"
    heading_l = Label(header_section, text=title_head , fg="#FFFFFF", bg="#272343")
    Font_tuple = ("Modern", 20, "bold")
    
    heading_l.config(font = Font_tuple)
    heading_l.place(relx=0.5,rely=0.5, anchor=CENTER)
    
    # Register Section
    register_section = Frame(root,width=win_w/2,height=350,bd=2,bg="#E3F6F5")
    register_section.place(x=0,y=50)
    
    # Login Section
    login_section = Frame(root,width=win_w/2,height=350,bd=2,bg="#E3F6F5")
    login_section.place(x=win_w/2,y=50)
    
    login = Button(login_section, text="LOGIN", fg="#272343",
                            bg="#BAE8E8", width=20, height=10, command=login_finger_process)
    
    myFont = font.Font(family='Modern', size=15, weight='bold')
    login['font'] = myFont
    
    login.place(relx=0.5,rely=0.5, anchor=CENTER)
    
    
    # Create Labels
    
    name_l = Label(register_section, text="NAME", bg="#E3F6F5", fg="#272343")
    
    email_l = Label(register_section, text="EMAIL", bg="#E3F6F5", fg="#272343")
  
    address_l = Label(register_section, text="ADDRESS", bg="#E3F6F5", fg="#272343")
  
    gender_l = Label(register_section, text="GENDER", bg="#E3F6F5", fg="#272343")
    
    phone_l = Label(register_section, text="PHONE", bg="#E3F6F5", fg="#272343")
  
    
    
    # Position Labels
    distance_y = 25
    
    name_l.place(x= 10,y = 30-distance_y)
    email_l.place(x= 10,y = 90-distance_y)
    address_l.place(x= 10,y = 150-distance_y)
    gender_l.place(x= 10,y= 210-distance_y)
    phone_l.place(x= 10,y= 270-distance_y)
    
    # create a text entry box
    name_field = Entry(register_section, width="46")
    email_field = Entry(register_section, width="46")
    address_field = Entry(register_section, width="46")
    
    n = StringVar()
    gender_field = ttk.Combobox(register_section, width = "10", textvariable = n)
  
    # Adding combobox drop down list
    gender_field['values'] = ('Male', 
                            'Female',
    )
                        
    # gender_field = Entry(register_section, width="46")
    phone_field = Entry(register_section, width="46")

    # Position Entry Box
    name_field.place(x= 100, y=30-distance_y)
    email_field.place(x= 100, y=90-distance_y)
    address_field.place(x= 100, y=150-distance_y)
    gender_field.place(x= 100, y=210-distance_y)
    phone_field.place(x= 100, y=270-distance_y)

    # create a Submit Button and place into the root window
    submit = Button(register_section, text="REGISTER", fg="#272343",
                            bg="#BAE8E8", width=31, height=1, command=insert)
    submit.place(x= 10, y=310-distance_y)
    myFont = font.Font(family='Modern', size=15, weight='bold')
    submit['font'] = myFont
    
    # start the GUI
    root.mainloop()
    