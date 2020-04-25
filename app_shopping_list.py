import tkinter as tk
from tkinter import filedialog, Text, simpledialog
import os


def add_item():
    item = simpledialog.askstring(title='', prompt="Item to add",
                                    parent=root)
    items.append(item)
    for item in items:
        label = tk.Label(frame, text=item, bg='white')
        label.pack()


root = tk.Tk()  # basis for the whole program. we attach everyhing to root
root.title('Shopping list')

items = []

# initilize screen size
canvas = tk.Canvas(root, height=600, width=600, bg='#263D42')
canvas.pack() # attach canvas to root

# attaching frame inside root
frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# adding button to add a product to the list
addItem = tk.Button(root, text='Add item', padx=10, pady=5, fg='black', bg='green', command=add_item)
addItem.pack()


root.mainloop() # run the program
