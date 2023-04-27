import tkinter as tk
from tkinter import ttk
import mysql.connector

# Set up the GUI
root = tk.Tk()
root.title("BavisRentals - Bstands for Bike")


# Set up the grid layout
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

top_frame = ttk.Frame(root)
top_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

left_frame = ttk.Frame(top_frame)
left_frame.grid(row=0, column=0, sticky="nsew")

right_frame = ttk.Frame(top_frame)
right_frame.grid(row=0, column=1, sticky="nsew")

def get_primary_key(table_name):
        if table_name:
            cursor.execute(f"SHOW KEYS FROM {table_name} WHERE Key_name = 'PRIMARY'")
            primary_key = cursor.fetchone()
            if primary_key:
                return primary_key[4]  # Column_name is at index 4
        return None

def create_record():
    table_name = table_var.get()

    if table_name:
        values = tuple(entry.get() for entry in field_entries)
        placeholders = ",".join(["%s"] * len(field_entries))
        query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        cursor.execute(query, values)
        db.commit()
        show_table_contents()

def update_record():
    table_name = table_var.get()

    if table_name:
        # Get the primary key column name and value
        pk_col_name = get_primary_key(table_name)
        pk_value = None
        if pk_col_name:
            for i, label in enumerate(field_labels):
                if label['text'] == pk_col_name:
                    pk_value = field_entries[i].get()
                    break

        if pk_col_name and pk_value:
            # Update the record
            set_clause = ", ".join([f"{label['text']}=%s" for label in field_labels if label['text'] != pk_col_name])
            values = [entry.get() for i, entry in enumerate(field_entries) if field_labels[i]['text'] != pk_col_name] + [pk_value]
            query = f"UPDATE {table_name} SET {set_clause} WHERE {pk_col_name}=%s"

            # Debug information
            print(f"Table name: {table_name}")
            print(f"Primary key column name: {pk_col_name}")
            print(f"Primary key value: {pk_value}")
            print(f"Set clause: {set_clause}")
            print(f"Values: {values}")
            print(f"SQL query: {query}")

            cursor.execute(query, values)
            db.commit()
            show_table_contents()
                def delete_record():
    table_name = table_var.get()

    if table_name:
        # Get the primary key column name and value
        pk_col_name = get_primary_key(table_name)
        pk_value = None
        if pk_col_name:
            for i, label in enumerate(field_labels):
                if label['text'] == pk_col_name:
                    pk_value = field_entries[i].get()
                    break



        if pk_col_name and pk_value:
            # Debug information
            print(f"Table name: {table_name}")
            print(f"Primary key column name: {pk_col_name}")
            print(f"Primary key value: {pk_value}")

            # Delete the record
            query = f"DELETE FROM {table_name} WHERE {pk_col_name}=%s"
            print(f"SQL query: {query}")
            cursor.execute(query, (pk_value,))
            db.commit()
            show_table_contents()

                
