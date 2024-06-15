import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def enter_data():
    accepted = accept_var.get() 

    if accepted == "Accepted":
        # User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            # Course info
            registration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()

            print("First name:", firstname, "Last name:", lastname)
            print("Title:", title, "Age:", age, "Nationality:", nationality)
            print("# Courses:", numcourses, "# Semesters:", numsemesters)
            print("Registration status:", registration_status)
            print("-----------------------------------------")

            # Create Table
            conn = sqlite3.connect('data.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data
                                    (firstname TEXT, lastname TEXT, title TEXT, age INT, nationality TEXT,
                                    registration_status TEXT, num_courses INT, num_semesters INT)'''
            
            conn.execute(table_create_query)

            # Insert Data
            data_insert_query = '''INSERT INTO Student_Data 
                                   (firstname, lastname, title, age, nationality, registration_status, num_courses, num_semesters)
                                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
            data_insert_tuple = (firstname, lastname, title, age, nationality, registration_status, numcourses, numsemesters)
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()

        else:
            messagebox.showwarning(title="Error", message="First name and last name are required")
    else:
        messagebox.showwarning(title="Error", message="You have not accepted the terms")

# Create the main window
window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack(padx=10, pady=10)

# User Information
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

# First Name
first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)

# Last Name
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)
last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

# Title
title_label = tkinter.Label(user_info_frame, text="Title")
title_label.grid(row=0, column=2)
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
title_combobox.grid(row=1, column=2)

# Age
age_label = tkinter.Label(user_info_frame, text="Age")
age_label.grid(row=2, column=0)
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=100)
age_spinbox.grid(row=3, column=0)

# Nationality
nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_label.grid(row=2, column=1)
nationality_combobox = ttk.Combobox(user_info_frame, values=["", "American", "British", "Canadian", "Other"])
nationality_combobox.grid(row=3, column=1)

# Registration Status
registration_frame = tkinter.LabelFrame(frame, text="Registration Status")
registration_frame.grid(row=1, column=0, padx=20, pady=10)

reg_status_var = tkinter.StringVar(value="Not Registered")
reg_status_yes = tkinter.Radiobutton(registration_frame, text="Registered", variable=reg_status_var, value="Registered")
reg_status_yes.grid(row=0, column=0)
reg_status_no = tkinter.Radiobutton(registration_frame, text="Not Registered", variable=reg_status_var, value="Not Registered")
reg_status_no.grid(row=0, column=1)

# Course Information
courses_frame = tkinter.LabelFrame(frame, text="Course Information")
courses_frame.grid(row=2, column=0, padx=20, pady=10)

# Number of Courses
numcourses_label = tkinter.Label(courses_frame, text="# Courses")
numcourses_label.grid(row=0, column=0)
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=1, to=10)
numcourses_spinbox.grid(row=1, column=0)

# Number of Semesters
numsemesters_label = tkinter.Label(courses_frame, text="# Semesters")
numsemesters_label.grid(row=0, column=1)
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=1, to=10)
numsemesters_spinbox.grid(row=1, column=1)

# Accept Terms
accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(frame, text="I accept the terms and conditions", variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=3, column=0, pady=10)

# Submit Button
submit_button = tkinter.Button(frame, text="Submit", command=enter_data)
submit_button.grid(row=4, column=0, pady=10)

# Run the main window loop
window.mainloop()
