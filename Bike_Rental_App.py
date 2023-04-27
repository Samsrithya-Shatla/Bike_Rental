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
