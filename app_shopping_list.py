import tkinter as tk
from tkinter import simpledialog, messagebox
import os


def display_shopping_list():
    if len(items) == 0:
        main_label = tk.Label(frame, text='The list is empty', bg='white', justify='left')
        main_label.grid(column=0, row= 0)
    for i, item in enumerate(items):
        label = tk.Label(frame, text='{0}. {1}'.format(i+1, item), width=30, height=1, bg='white', anchor='w')
        label.grid(column=0)
        i += 1


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
    to_remove = simpledialog.askstring(title='', prompt="Item to remove", parent=root)
    if to_remove in items:
        items.remove(to_remove)
    else:
        messagebox.showerror("Error", "There is no {0} in the list".format(to_remove))
    display_shopping_list()


def clear_list():
    destroy_widgets()
    items.clear()
    display_shopping_list()


""" Main program is below """

root = tk.Tk()  # basis for the whole program. we attach everyhing to root
root.title('Shopping list')

items = []

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

# App buttons
buttons = []

addItem = tk.Button(root, text='Add item', padx=10, pady=5, fg='black', bg='green', command=add_item)
buttons.append(addItem)

clearList = tk.Button(root, text='Clear the list', padx=10, pady=5, fg='black', bg='green', command=clear_list)
buttons.append(clearList)

removeItem = tk.Button(root, text='Remove item', padx=10, pady=5, fg='black', bg='green', command=remove_item)
buttons.append(removeItem)

for button in buttons:
    button.pack()

# display the saved shopping list
display_shopping_list()

# run the program
root.mainloop()

""" Saving the list at the end of the program """

with open('shopping_list.txt', mode='w') as f:
    for item in items:
        f.write(item + ',')