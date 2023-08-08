import tkinter as tk
import pickle

def add_task():
    task = entry_task.get()
    if task.strip():
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        tk.messagebox.showwarning(title="Warning!", message="You must enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        tk.messagebox.showwarning(title="Warning!", message="You must select a task.")

def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tk.END)
        for task in tasks:
            listbox_tasks.insert(tk.END, task)
    except FileNotFoundError:
        tk.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")

def save_tasks():
    tasks = listbox_tasks.get(0, tk.END)
    pickle.dump(tasks, open("tasks.dat", "wb"))

# Create GUI
root = tk.Tk()
root.title("To-Do List by K.B AMOGH")

frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=20, width=100)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=90)
entry_task.pack()

button_add_task = tk.Button(root, text="Add task", width=100, command=add_task)
button_add_task.pack()

button_delete_task = tk.Button(root, text="Delete task", width=100, command=delete_task)
button_delete_task.pack()

button_load_tasks = tk.Button(root, text="Load tasks", width=100, command=load_tasks)
button_load_tasks.pack()

button_save_tasks = tk.Button(root, text="Save tasks", width=100, command=save_tasks)
button_save_tasks.pack()

root.mainloop()
