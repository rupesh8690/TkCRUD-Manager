from insertion import insertToDatabase
from tkinter import *
import tkinter as t
from tkinter import ttk  
from tkinter.messagebox import showinfo, askyesno  
from retrieve import retriveData
from delete import deleteRecord  # Import the function to delete records from the database
from validateData import is_valid_phone_number
from validateData import is_valid_name
from update import  updateToDatabase
# Create the main window
window = t.Tk()
window.title("TkCRUD Manager")
window.geometry("1100x600")

# Creating the first canvas
C = t.Canvas(window, height=400, width=400, bg="white", highlightbackground="black", highlightcolor="black", highlightthickness=2)
C.pack(side=t.LEFT, padx=10)

# Adding label to the canvas
name = Label(C, text="Enter Name")
C.create_window(50, 20, window=name) 

# Creating textbox 
nameTextBox = Entry(C)
C.create_window(200, 20, window=nameTextBox) 

fname = Label(C, text="Father's Name")
C.create_window(50, 50, window=fname) 
fatherNameTextBox = Entry(C)
C.create_window(200, 50, window=fatherNameTextBox) 

address = Label(C, text="Enter Address")
C.create_window(50, 80, window=address) 
addressTextbox = Entry(C)
C.create_window(200, 80, window=addressTextbox) 

gender = Label(C, text="Choose Gender")
C.create_window(50, 110, window=gender)

v = IntVar()  # This will store the selected value of the radio buttons

# Creating Radiobuttons
male = Radiobutton(C, text='Male', variable=v, value=1)
C.create_window(170, 110, window=male)

female = Radiobutton(C, text='Female', variable=v, value=2)
C.create_window(250, 110, window=female)

phone = Label(C, text="Phone Number")
C.create_window(50, 140, window=phone) 

phoneTextBox = Entry(C)
C.create_window(200, 140, window=phoneTextBox) 

# Function to refresh the Treeview
def refresh_treeview():
    # Clear the current data in the treeview
    for item in tree.get_children():
        tree.delete(item)
        
    # Get updated data and insert into the treeview
    answer = retriveData() 
    for entry in answer:
        tree.insert('', t.END, values=entry)  

# Getting data from all the input fields and pasing to insert database function as arguements
def getData():
    name = nameTextBox.get()
    fname = fatherNameTextBox.get()
    address = addressTextbox.get()
    gender = "Male" if v.get() == 1 else "Female" if v.get() == 2 else "Not selected"
    phone = phoneTextBox.get()
    
    # Check if all fields are filled
    if name and fname and address and gender != "Not selected" and phone:
        # Insert data into the database
        if is_valid_phone_number(phone) == False:
            warning.config(text="Enter valid phone")
        elif is_valid_name(name) == False:
            warning.config(text="Name must start with letter")
        elif is_valid_name(fname) == False:
            warning.config(text="Name must start with letter")
        else:
            current_state_add= add.cget("state")
            if current_state_add == NORMAL:
                returnedVal = insertToDatabase(name, fname, address, gender, phone)
                warning.config(text=returnedVal)  # Clear the warning if data is valid
                
            

            #also passing value to updator function
            current_state_update= update.cget("state")
            if current_state_update == NORMAL:
                upateReturn= updateToDatabase(uniq_id,name, fname, address, gender, phone)
                warning.config(text=upateReturn)

            
           
        
            # Clear the input fields
            nameTextBox.delete(0, END)
            fatherNameTextBox.delete(0, END)
            addressTextbox.delete(0, END)
            phoneTextBox.delete(0, END)
            v.set(0)  # Reset the gender selection
        
            # Refresh the treeview to show new data
            refresh_treeview()
    else:
        warning.config(text="All fields are required")


#defining function to clear fileds
def clearField():
    # Clear the input fields
    nameTextBox.delete(0, END)
    fatherNameTextBox.delete(0, END)
    addressTextbox.delete(0, END)
    phoneTextBox.delete(0, END)
    v.set(0)  # Reset the gender selection
    update.config(state=DISABLED)
    add.config(state=ACTIVE)

    

add = Button(C, text="Add", command=getData)
C.create_window(50, 170, window=add)

exit = Button(C, text="Exit", command=window.quit)
C.create_window(100, 170, window=exit)

update = Button(C, text="Update",state=DISABLED,command=getData)  
C.create_window(150, 170, window=update)

clear= Button(C,text="Clear",command=clearField)
C.create_window(200,170,window=clear)

warning = Label(C, fg="red")
C.create_window(150, 230, window=warning)

# Creating the second canvas
canvas_right = t.Canvas(window, height=400, width=500, bg="white", highlightbackground="black", highlightcolor="black", highlightthickness=2)
canvas_right.pack(side=t.LEFT)  # Use t.LEFT to place it next to the first canvas

# Identifiers for columns  
descriptions = ('SNo', 'Name', 'Fathers Name', 'Address', 'Gender', 'Phone')  
tree = ttk.Treeview(canvas_right, columns=descriptions, show='headings')  

# Setting up the headings for each column with left alignment
tree.heading('SNo', text='SNo.', anchor='w')  
tree.heading('Name', text='Name', anchor='w')  
tree.heading('Fathers Name', text="Father's Name", anchor='w')  
tree.heading('Address', text='Address', anchor='w')  
tree.heading('Gender', text='Gender', anchor='w')  
tree.heading('Phone', text='Phone number', anchor='w')

# Setting up columns with specified widths and left alignment for their content
tree.column('SNo', width=50, anchor='w')  
tree.column('Name', width=120, anchor='w')  
tree.column('Fathers Name', width=120, anchor='w')  
tree.column('Address', width=200, anchor='w')  
tree.column('Gender', width=50, anchor='w')  
tree.column('Phone', width=100, anchor='w')  

# Initial data load
refresh_treeview()  # Load initial data into the treeview

# Function to handle the event <<TreeviewSelect>>  
def selection(event):  
    for i in tree.selection():  
        item = tree.item(i)  
        record = item['values']  
        showinfo(title='Data', message=f'Selected record: {record}')

        #taking id for updation and making it global
        global uniq_id
        uniq_id=record[0]
        print(uniq_id)
      

        #making view button active
        update.config(state=NORMAL)

        #disabling add button if update is clicked
        add.config(state=DISABLED)
        # Clear the textboxes before inserting new data
        nameTextBox.delete(0, 'end')
        fatherNameTextBox.delete(0, 'end')
        addressTextbox.delete(0,'end')
        phoneTextBox.delete(0,'end')
        
       
        # Insert the new data into the textboxes
        nameTextBox.insert(0, record[1])
        fatherNameTextBox.insert(0, record[2])
        addressTextbox.insert(0,record[3])
        phoneTextBox.insert(0,record[5])
        #checking for gender
        if record[4] == "Male":
             male.select() 
        else:
            female.select()


  
    
# Bind the selection event
tree.bind('<<TreeviewSelect>>', selection)  
tree.grid(row=0, column=0, sticky='nsew')  # Treeview widget on the root window  

# Create a label to display messages
message_label = t.Label(canvas_right, text="", fg="green")
message_label.grid(row=2, column=0, pady=10)  # Place it below the delete button

# Function to delete a record
def delete_selected_record():
    global selected_item
    selected_item = tree.selection()
    if not selected_item:
        showinfo("Delete", "Please select a record to delete.")
        return
    
    # Confirm deletion
    confirm = askyesno("Confirm Delete", "Are you sure you want to delete the selected record?")
    if confirm:
        for item in selected_item:
            # Get the selected record's values
            item_values = tree.item(item, 'values')
            # Assuming the first value (SNo) is the identifier to delete from the database
            s_no = item_values[0]
          
            # Call delete function to remove from the database
            deleteRecord(int(s_no))  
            
            # Remove from Treeview
            tree.delete(item)
            
            # Update the message label
            message_label.config(text="Record deleted successfully!")
            # Optionally, clear the message after a few seconds
            canvas_right.after(3000, lambda: message_label.config(text=""))

# Create a delete button
delete_button = t.Button(canvas_right, text="Delete Selected", command=delete_selected_record)
delete_button.grid(row=1, column=0, pady=10)  # Place it below the Treeview


window.mainloop()
