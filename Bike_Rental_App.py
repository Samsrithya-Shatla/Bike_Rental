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
            tree.column(col_name, anchor="w", stretch=True)
            tree.heading(col_name, text=col_name)

        for record in records:
            tree.insert("", "end", values=record)


def create_record():
    pass  # Implement create functionality

def update_record():
    pass  # Implement update functionality

def delete_record():
    pass  # Implement delete functionality

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
root.geometry("1080x1920")

# Top frame
top_frame = ttk.Frame(root)
top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

# Split the top frame into two frames
left_frame = ttk.Frame(top_frame, width=200)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=10, pady=10)
right_frame = ttk.Frame(top_frame)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Define the table variable
table_var = tk.StringVar()

label = ttk.Label(left_frame, text="Select a table:")
label.pack(pady=10)

table_combo = ttk.Combobox(left_frame, textvariable=table_var)
table_combo['values'] = ('customers', 'bikes', 'rentals', 'rental_return')  # Your table names
table_combo.pack(pady=10)

show_button = ttk.Button(left_frame, text="Show Table and Fields", command=lambda: [show_table_contents(), show_fields()])
show_button.pack(pady=10)

create_button = ttk.Button(left_frame, text="Create Record", command=create_record)
create_button.pack(pady=10)

update_button = ttk.Button(left_frame, text="Update Record", command=update_record)
update_button.pack(pady=10)

delete_button = ttk.Button(left_frame, text="Delete Record", command=delete_record)
delete_button.pack(pady=10)

# Form view in the right frame
fields_frame = ttk.Frame(right_frame, borderwidth=2, relief="groove")
fields_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

field_labels = []
field_entries = []

def show_fields():
    for label, entry in zip(field_labels, field_entries):
        label.pack_forget()
        entry.pack_forget()

    table_name = table_var.get()

    if table_name:
        query = f"SHOW COLUMNS FROM {table_name}"
        cursor.execute(query)
        fields = cursor.fetchall()

        for field in fields:
            field_label = ttk.Label(fields_frame, text=field[0])
            field_labels.append(field_label)
            field_entry = ttk.Entry(fields_frame)
            field_entries.append(field_entry)
            field_label.pack(side=tk.LEFT, padx=10, pady=10)
            field_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)

# Table view in the right frame
table_frame = ttk.Frame(right_frame, borderwidth=2, relief="groove")
table_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

tree = ttk.Treeview(table_frame, selectmode="browse")
tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Add scrollbar
scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.configure(yscrollcommand=scrollbar.set)

# Bottom frame
bottom_frame = ttk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False)

# Add a status bar to the bottom frame
status_var = tk.StringVar()
status_label = ttk.Label(bottom_frame, textvariable=status_var, anchor=tk.W)
status_label.pack(side=tk.BOTTOM, fill=tk.X)
status_var.set("Ready")

root.mainloop()

# Close database connection
cursor.close()
db.close()

HI

