## TO-DO-LIST APP ##

import tkinter as ts
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(ts.END, task)
        entry_task.delete(0, ts.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task")
        
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]  
        listbox_tasks.delete( selected_task_index)   
    except IndexError:
        messagebox.showwarning("Selection Error", "Please Select a task to delete") 
        
def clear_tasks():
   confirmation = messagebox.askyesnocancel("Confirmation", "Are you sure you want to clear all tasks?")
   if confirmation:
       listbox_tasks.delete(0, ts.END)
   else:
       messagebox.showinfo("operation Cancelled", "Task clearing cancelled") 

def main():
    global entry_task, listbox_tasks 
     
     # main window 
root = ts.Tk()
root.title("TO-DO LIST")

# entry field and add task button
entry_task = ts.Entry(root, width=45)
entry_task.grid(row=0, column=0, padx=10, pady=10,)

add_button = ts.Button(root, text="Add Task", width=15, command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)     

# Task listbox
listbox_tasks = ts.Listbox(root, selectmode=ts.SINGLE, width=60, height=15)   
listbox_tasks.grid(row=1, column=0, columnspan=2, padx=10, pady=10)  
  
# delete task and clear tasks buttons
delete_button = ts.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.grid(row=2, column=0, padx=10, pady=10)

clear_button = ts.Button(root, text="Clear Tasks", width=15, command=clear_tasks)
clear_button.grid(row=2, column=1, padx=10, pady=10)
 
# Run main loop 
root.mainloop()
 
if __name__ == "__main__":
      main()