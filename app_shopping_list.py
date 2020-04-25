import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()  # basis for the whole program. we attach everyhing to root

# initilize screen size
canvas = tk.Canvas(root, height=600, width=600, bg='#263D42')
canvas.pack() # attach canvas to root

# attaching frame inside root
frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# adding button to add a product to the list
addItem = tk.Button(root, text='Add item', padx=10, pady=5, fg='black', bg='green')
addItem.pack()

root.mainloop() # run the program
