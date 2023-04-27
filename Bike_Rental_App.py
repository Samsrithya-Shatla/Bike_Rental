
import tkinter as tk
from tkinter import ttk
import mysql.connector
import pandas as pd
from pandastable import Table

def show_table_contents():
    table_name = table_var.get()
    
    if table_name:
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        records = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(records, columns=column_names)

        table_frame = tk.Toplevel(root)
        table_frame.title(f"Contents of {table_name}")
        table_frame.geometry("800x400")

        pt = Table(table_frame, dataframe=df)
        pt.show()

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="S.Sam1461",
    database="BikeRentalDB"
)
cursor = db.cursor()

# Define the GUI
root = tk.Tk()
root.title("MySQL Table Viewer")
root.geometry("300x200")

table_var = tk.StringVar()

label = ttk.Label(root, text="Select a table:")
label.pack(pady=10)

table_combo = ttk.Combobox(root, textvariable=table_var)
table_combo['values'] = ('customers', 'bikes', 'rentals', 'rental_return')  # Your table names
table_combo.pack(pady=10)

show_button = ttk.Button(root, text="Show Table Contents", command=show_table_contents)
show_button.pack(pady=10)

root.mainloop()

# Close database connection
cursor.close()
db.close()
