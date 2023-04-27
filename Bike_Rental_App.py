import tkinter as tk
from tkinter import ttk
import mysql.connector

def show_table_contents():
    for record in tree.get_children():
        tree.delete(record)

    table_name = table_var.get()
    
    if table_name:
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        records = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]

        tree["columns"] = column_names
        for col_name in column_names:
            tree.column(col_name, anchor="w", stretch=tk.YES, minwidth=100)
            tree.heading(col_name, text=col_name)

        for record in records:
            tree.insert('', 'end', values=record)

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
root.geometry("800x400")

table_var = tk.StringVar()

label = ttk.Label(root, text="Select a table:")
label.grid(row=0, column=0, pady=10, padx=10)

table_combo = ttk.Combobox(root, textvariable=table_var)
table_combo['values'] = ('customers', 'bikes', 'rentals', 'rental_return')  # Your table names
table_combo.grid(row=0, column=1, pady=10)

show_button = ttk.Button(root, text="Show Table Contents", command=show_table_contents)
show_button.grid(row=0, column=2, pady=10, padx=10)

tree = ttk.Treeview(root, selectmode="browse")
tree.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# Add scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
scrollbar.grid(row=1, column=3, padx=0, pady=10, sticky="nsew")
tree.configure(yscrollcommand=scrollbar.set)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()

# Close database connection
cursor.close()
db.close()


