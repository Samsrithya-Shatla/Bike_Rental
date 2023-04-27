import tkinter as tk
from tkinter import ttk
import mysql.connector

# Set up the GUI
root = tk.Tk()
root.title("BavisRentals - Bstands for Bike")


# Set up the grid layout
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
