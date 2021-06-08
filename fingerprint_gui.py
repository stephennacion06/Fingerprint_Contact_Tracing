from tkinter import *
  
# Function for clearing the
# contents of text entry boxes
def clear():
      
    # clear the content of text entry box
    name_field.delete(0, END)
    email_field.delete(0, END)
    address_field.delete(0, END)
    gender_field.delete(0, END)
    phone_field.delete(0, END)
  
  
# Function to take data from GUI 
# window and write to an excel file
def insert():
      
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
  
        # # save the file
        # wb.save('C:\\Users\\Admin\\Desktop\\excel.xlsx')
        print("Done Submitted")
        # set focus on the name_field box
        name_field.focus_set()
  
        # call the clear() function
        clear()
  
  
# Driver code
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
    
    header_section =Frame(root,width=win_w,height=50,bg="#272343")
    header_section.place(x=0,y=0)
    
    title_head = "FINGERPRINT CONTACT TRACING SYSTEM"
    heading_l = Label(header_section, text=title_head , fg="#FFFFFF", bg="#272343")
    heading_l.place(relx=0.5,rely=0.5, anchor=CENTER)
    
    # Register Section
    register_section = Frame(root,width=win_w/2,height=350,bd=2,bg="#E3F6F5")
    register_section.place(x=0,y=50)
    
    # Login Section
    login_section = Frame(root,width=win_w/2,height=350,bd=2,bg="#E3F6F5")
    login_section.place(x=win_w/2,y=50)
    
    login = Button(login_section, text="LOGIN", fg="#272343",
                            bg="#BAE8E8", width=20, height=10, command=insert)
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
    gender_field = Entry(register_section, width="46")
    phone_field = Entry(register_section, width="46")

    # Position Entry Box
    name_field.place(x= 100, y=30-distance_y)
    email_field.place(x= 100, y=90-distance_y)
    address_field.place(x= 100, y=150-distance_y)
    gender_field.place(x= 100, y=210-distance_y)
    phone_field.place(x= 100, y=270-distance_y)

    # create a Submit Button and place into the root window
    submit = Button(register_section, text="REGISTER", fg="#272343",
                            bg="#BAE8E8", width=55, height=2, command=insert)
    submit.place(x= 10, y=310-distance_y)
  
    # start the GUI
    root.mainloop()
    