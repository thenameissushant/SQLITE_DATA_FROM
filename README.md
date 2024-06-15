# Data Entry Form Application

## Overview
This application is a simple GUI-based data entry form created using Python's Tkinter library. It collects user information, including personal details and course information, and stores the data in an SQLite database.

## Features
- Collects user's first name, last name, title, age, and nationality.
- Allows the user to indicate their registration status.
- Collects information about the number of courses and semesters.
- Ensures that the user accepts terms and conditions before submission.
- Stores the collected data in an SQLite database.

## Requirements
- Python 3.x
- Tkinter (usually included with Python)
- SQLite (usually included with Python)

## Installation
1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Run the script**:
    ```bash
    python data_entry_form.py
    ```

## Usage
1. **Fill out the form**:
    - Enter your first name and last name.
    - Select your title from the dropdown.
    - Enter your age.
    - Select your nationality from the dropdown.
    - Choose your registration status.
    - Enter the number of courses you are taking.
    - Enter the number of semesters you are enrolled for.
    - Check the box to accept the terms and conditions.

2. **Submit the form**:
    - Click the "Submit" button to save your information.
    - If any required fields are missing or if the terms are not accepted, you will see a warning message.

3. **Data Storage**:
    - The data will be stored in a file named `data.db` in the same directory as the script.
    - The database contains a table named `Student_Data` where all the form submissions are stored.

## Code Explanation
### Function: `enter_data`
This function is called when the "Submit" button is clicked. It performs the following tasks:
- Checks if the terms and conditions are accepted.
- Validates that both the first name and last name are provided.
- Collects all data from the form fields.
- Creates a SQLite database and table if they do not exist.
- Inserts the collected data into the database.

### GUI Layout
- The main window is created using `tkinter.Tk()`.
- The form is divided into several sections using `LabelFrame` for better organization.
- Widgets such as `Label`, `Entry`, `Combobox`, `Spinbox`, `Radiobutton`, and `Checkbutton` are used to create the form fields.
- The submit button is created using `Button` and is linked to the `enter_data` function.

## Database Schema
The SQLite database `data.db` contains a table `Student_Data` with the following schema:
- `firstname`: TEXT
- `lastname`: TEXT
- `title`: TEXT
- `age`: INTEGER
- `nationality`: TEXT
- `registration_status`: TEXT
- `num_courses`: INTEGER
- `num_semesters`: INTEGER

## Contact
For any issues or questions, please contact [thenameissushant@gmail.com].

---
