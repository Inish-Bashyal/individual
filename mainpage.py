from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

root = Tk()
root.title('DATABASE MANAGEMENT SYSTEM')
root.geometry("1230x500")


# Creating a database
conn = sqlite3.connect('final.db')

# Creating a cursor instance
c = conn.cursor()

# Create Table
# c.execute("""CREATE TABLE entries(
# 	first_name text,
# 	last_name text,
# 	id integer,
# 	address text,
# 	city text,
# 	state text,
# 	zipcode text)
# 	""")


# Adding Record Entry Boxes
data_frame = LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

first_name_label = Label(data_frame, text="First Name")
first_name_label.grid(row=0, column=0, padx=10, pady=10)
first_name_entry = Entry(data_frame)
first_name_entry.grid(row=0, column=1, padx=10, pady=10)

last_name_label = Label(data_frame, text="Last Name")
last_name_label.grid(row=0, column=2, padx=10, pady=10)
last_name_entry = Entry(data_frame)
last_name_entry.grid(row=0, column=3, padx=10, pady=10)

id_label = Label(data_frame, text="ID")
id_label.grid(row=0, column=4, padx=10, pady=10)
id_entry = Entry(data_frame)
id_entry.grid(row=0, column=5, padx=10, pady=10)

address_label = Label(data_frame, text="Address")
address_label.grid(row=1, column=0, padx=10, pady=10)
address_entry = Entry(data_frame)
address_entry.grid(row=1, column=1, padx=10, pady=10)

city_label = Label(data_frame, text="City")
city_label.grid(row=1, column=2, padx=10, pady=10)
city_entry = Entry(data_frame)
city_entry.grid(row=1, column=3, padx=10, pady=10)

state_label = Label(data_frame, text="State")
state_label.grid(row=1, column=4, padx=10, pady=10)
state_entry = Entry(data_frame)
state_entry.grid(row=1, column=5, padx=10, pady=10)

zipcode_label = Label(data_frame, text="Zipcode")
zipcode_label.grid(row=1, column=6, padx=10, pady=10)
zipcode_entry = Entry(data_frame)
zipcode_entry.grid(row=1, column=7, padx=10, pady=10)


# Adding Some Style
style = ttk.Style()

# Changing Selected Color
style.map('Treeview',background=[('selected', "#347083")])

# Creating a Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Creating a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Creating The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configuring the Scrollbar
tree_scroll.config(command=my_tree.yview)

# Defining Our Columns
my_tree['columns'] = ("First Name", "Last Name", "ID", "Address", "City", "State", "Zipcode")

# Formatting Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("First Name",width=140)
my_tree.column("Last Name", width=140)
my_tree.column("ID",  width=100)
my_tree.column("Address",width=140)
my_tree.column("City", width=140)
my_tree.column("State", width=140)
my_tree.column("Zipcode", width=140)

# Creating Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("First Name", text="First Name", anchor=W)
my_tree.heading("Last Name", text="Last Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Address", text="Address", anchor=CENTER)
my_tree.heading("City", text="City", anchor=CENTER)
my_tree.heading("State", text="State", anchor=CENTER)
my_tree.heading("Zipcode", text="Zipcode", anchor=CENTER)

# Creating Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")


# add new record to database
def submit():
    a = first_name_entry.get()
    b = last_name_entry.get()
    h = id_entry.get()
    d = address_entry.get()
    e = city_entry.get()
    f = state_entry.get()
    g = zipcode_entry.get()
    l=[a,b,h,d,e,f,g]

    if (l[0]=="" or l[1]=="" or l[2]=="" or l[3]=="" or l[4]=="" or l[5]=="" or l[6]==""):
        messagebox.showerror("ERROR", "ALL FIELDS REQUIRED")
        # Clear entry boxes
        first_name_entry.delete(0, END)
        last_name_entry.delete(0, END)
        id_entry.delete(0, END)
        address_entry.delete(0, END)
        city_entry.delete(0, END)
        state_entry.delete(0, END)
        zipcode_entry.delete(0, END)
    else:
        # Update the database
        # Create a database or connect to one that exists
        conn = sqlite3.connect('final.db')

        # Create a cursor instance
        c = conn.cursor()

        # Add New Record
        c.execute("INSERT INTO entries VALUES (:first, :last, :id, :address, :city, :state, :zipcode)",
              {
                  'first': first_name_entry.get(),
                  'last': last_name_entry.get(),
                  'id': id_entry.get(),
                  'address': address_entry.get(),
                  'city': city_entry.get(),
                  'state': state_entry.get(),
                  'zipcode': zipcode_entry.get(),
              })

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()

        # Clear entry boxes
        first_name_entry.delete(0, END)
        last_name_entry.delete(0, END)
        id_entry.delete(0, END)
        address_entry.delete(0, END)
        city_entry.delete(0, END)
        state_entry.delete(0, END)
        zipcode_entry.delete(0, END)

        # Clear The Treeview Table
        my_tree.delete(*my_tree.get_children())

        # Run to pull data from database on start
        query()

def query():
    # Create a database or connect to one that exists
    conn = sqlite3.connect('final.db')

    # Create a cursor instance
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM entries")
    records = c.fetchall()

    # Add our data to the screen
    global count
    count = 0

    for record in records:
        if count % 2 == 0: #this loop is used for adding color to the row
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[1], record[2], record[0], record[4], record[5], record[6], record[7]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[1], record[2], record[0], record[4], record[5], record[6], record[7]),
                           tags=('oddrow',))
        # increment counter
        count += 1

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()



# Remove one record
def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)

    # Create a database or connect to one that exists
    conn = sqlite3.connect('final.db')

    # Create a cursor instance
    c = conn.cursor()

    # Delete From Database
    c.execute("DELETE from entries WHERE oid=" + id_entry.get())

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()

    # Clear The Entry Boxes
    clear_entries()

    # Add a little message box for fun
    messagebox.showinfo("Deleted!", "Your Record Has Been Deleted!")


# Remove Many records
def remove_many():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)


# Remove all records
def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)


# Clear entry boxes
def clear_entries():
    # Clear entry boxes
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)


# Select Record
def select_record(enn):
    # Clear entry boxes
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)

    # Grab record Number
    selected = my_tree.focus()
    # Grab record values
    values = my_tree.item(selected, 'values')

    # outputs to entry boxes
    first_name_entry.insert(0, values[0])
    last_name_entry.insert(0, values[1])
    id_entry.insert(0, values[2])
    address_entry.insert(0, values[3])
    city_entry.insert(0, values[4])
    state_entry.insert(0, values[5])
    zipcode_entry.insert(0, values[6])


# Update record
def update_record():
    a = first_name_entry.get()
    b = last_name_entry.get()
    h = id_entry.get()
    d = address_entry.get()
    e = city_entry.get()
    f = state_entry.get()
    g = zipcode_entry.get()
    l=[a,b,h,d,e,f,g]


    # Grab the record number
    selected = my_tree.focus()
    # Update record
    my_tree.item(selected, text="", values=(
    first_name_entry.get(), last_name_entry.get(), id_entry.get(), address_entry.get(), city_entry.get(), state_entry.get(),
    zipcode_entry.get(),))

    if (l[0]=="" or l[1]=="" or l[2]=="" or l[3]=="" or l[4]=="" or l[5]=="" or l[6]==""):
        messagebox.showerror("ERROR", "ALL FIELDS REQUIRED")
        # Clear entry boxes
        first_name_entry.delete(0, END)
        last_name_entry.delete(0, END)
        id_entry.delete(0, END)
        address_entry.delete(0, END)
        city_entry.delete(0, END)
        state_entry.delete(0, END)
        zipcode_entry.delete(0, END)

    else:

        # Update the database
        # Create a database or connect to one that exists
        conn = sqlite3.connect('final.db')

        # Create a cursor instance
        c = conn.cursor()

        c.execute("""UPDATE entries SET
		first_name = :first,
		last_name = :last,
		address = :address,
		city = :city,
		state = :state,
		zipcode = :zipcode

		WHERE oid = :oid""",
              {
                  'first': first_name_entry.get(),
                  'last': last_name_entry.get(),
                  'address': address_entry.get(),
                  'city': city_entry.get(),
                  'state': state_entry.get(),
                  'zipcode': zipcode_entry.get(),
                  'oid': id_entry.get(),
              })

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()

        # Clear entry boxes
        first_name_entry.delete(0, END)
        last_name_entry.delete(0, END)
        id_entry.delete(0, END)
        address_entry.delete(0, END)
        city_entry.delete(0, END)
        state_entry.delete(0, END)
        zipcode_entry.delete(0, END)




# Buttons
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

update_button = Button(button_frame, text="Update Record", command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = Button(button_frame, text="Add Record", command=submit)
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_all_button = Button(button_frame, text="Remove All Records", command=remove_all)
remove_all_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = Button(button_frame, text="Remove One Selected", command=remove_one)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = Button(button_frame, text="Remove Many Selected", command=remove_many)
remove_many_button.grid(row=0, column=4, padx=10, pady=10)


select_record_button = Button(button_frame, text="Clear Entry Boxes", command=clear_entries)
select_record_button.grid(row=0, column=7, padx=10, pady=10)

# Binding the treeview
my_tree.bind("<Button-2>", select_record)

# Running to pull data from database on start
query()

root.mainloop()
