import tkinter as tk
from tkinter import simpledialog, messagebox
import os


def display_shopping_list():
    if len(items) == 0:
        main_label = tk.Label(frame, text='The list is empty', bg='green', bd=3,
                              relief='solid', font="Times 18")
        main_label.place(relwidth=0.4, relheight=0.2 ,relx=0.3, rely=0.4)
        # main_label.pack()
    else:
        counter = tk.Label(frame, text='Shopping list contain {0} item(s):'.format(len(items)),
                           width=30, height=2, bg='white', anchor='w', font='bold')
        counter.grid(column=0)
        for i, item in enumerate(items):
            label = tk.Label(frame, text='{0}. {1}'.format(i+1, item), width=30, height=1, bg='white',
                             anchor='w')
            label.grid(column=0)
            i += 1


def destroy_widgets():
    for widget in frame.winfo_children():
        widget.destroy()


def add_item():
    destroy_widgets()
    item = simpledialog.askstring(title='', prompt="Item to add", parent=root)
    items.append(item.title())
    display_shopping_list()


def remove_item():
    destroy_widgets()
    to_remove = simpledialog.askstring(title='', prompt="Item to remove", parent=root)
    flag = True
    temp = []
    for item in items:
        if to_remove in item:
            flag = False
            temp.append(item)
    for i in temp:
        items.remove(i)
    if flag:
        messagebox.showerror("Error", "There is no {0} in the list".format(to_remove))
    display_shopping_list()


def clear_list():
    destroy_widgets()
    items.clear()
    display_shopping_list()


""" Main program is below """

root = tk.Tk()  # basis for the whole program. we attach everyhing to root
root.title('Shopping list')
# root.geometry('600x600')

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
addItem = tk.Button(root, text='Add item', pady=5, fg='black', bg='green', command=add_item)
addItem.place(relwidth=0.2, relx=0.1, rely=0.92)

clearList = tk.Button(root, text='Clear the list', pady=5, fg='black', bg='red', command=clear_list)
clearList.place(relwidth=0.2, relx=0.6, rely=0.92)

removeItem = tk.Button(root, text='Remove item', pady=5, fg='black', bg='yellow', command=remove_item)
removeItem.place(relwidth=0.2, relx=0.35, rely=0.92)

# display the saved shopping list
display_shopping_list()

# run the program
root.mainloop()

""" Saving the list at the end of the program """

with open('shopping_list.txt', mode='w') as f:
    for item in items:
        f.write(item + ',')