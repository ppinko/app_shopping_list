import tkinter as tk
from tkinter import Text, simpledialog, messagebox
import os


def display_shopping_list():
    for item in items:
        label = tk.Label(frame, text=item, bg='white')
        label.pack()


def destroy_widgets():
    for widget in frame.winfo_children():
        widget.destroy()


def add_item():
    destroy_widgets()
    item = simpledialog.askstring(title='', prompt="Item to add", parent=root)
    items.append(item)
    display_shopping_list()


def remove_item():
    destroy_widgets()
    while True:
        item = simpledialog.askstring(title='', prompt="Item to remove", parent=root)
        if item in items:
            items.remove(item)
            break
    display_shopping_list()


""" Main program is below """

root = tk.Tk()  # basis for the whole program. we attach everyhing to root
root.title('Shopping list')

items = []
temp_items = None

if os.path.isfile('shopping_list.txt'):
    with open('shopping_list.txt', mode='r') as f:
        temp_items = f.read()
        temp_items = temp_items.split(',')
        items = [x for x in temp_items if x.strip()]

# initilize screen size
canvas = tk.Canvas(root, height=600, width=600, bg='#263D42')
canvas.pack() # attach canvas to root

# attaching frame inside root
frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# adding button to add a product to the list
addItem = tk.Button(root, text='Add item', padx=10, pady=5, fg='black', bg='green', command=add_item)
addItem.pack()

display_shopping_list()

root.mainloop() # run the program

with open('shopping_list.txt', mode='w') as f:
    for item in items:
        f.write(item + ',')