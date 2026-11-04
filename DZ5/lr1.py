import tkinter as tk
from tkinter import ttk
def Clear_entry():
    global task
    task.delete(0, "end")
    clear()
    error_label.pack_forget()

def new_task():
    global List
    global var
    if var.get()==0:
        error_label.pack()
    else:
        List.insert(last_elems[var.get()], task.get())
        for i in range(var.get(), 4):
            last_elems[i]+=1
        error_label.pack_forget()
        Clear_entry()
last_elems=dict.fromkeys([1, 2, 3], 0)
root=tk.Tk()
root.title("Менеджер задач")
root.geometry("900x600")

frame_1=ttk.Frame(borderwidth=10, padding=[5, 5])
frame_1_1=ttk.Frame( frame_1, borderwidth=10, padding=[5, 5])
frame_2=ttk.Frame(borderwidth=10, padding =[5, 5])

error_label=ttk.Label(frame_1_1, text="Выберите приоритет!")

btn_save=ttk.Button(frame_1, text="Внести в список", command=new_task)
btn_clear=ttk.Button(frame_1, text="Сбросить", command=Clear_entry)
task_label=ttk.Label(frame_1, text='Введите задачу: ')
task=tk.Entry(frame_1)


var=tk.IntVar(value=0)
def clear():
    global var
    var.set(0)
choose_label=ttk.Label(frame_1_1, text="Выберите приоритет:")
btn1_ch=ttk.Radiobutton(frame_1_1, text="Срочный", variable=var, value=1)
btn2_ch=ttk.Radiobutton(frame_1_1, text="Важный",  variable=var, value=2)
btn3_ch=ttk.Radiobutton(frame_1_1, text="Обычный",  variable=var, value=3)
btn_clear_ch=ttk.Button(frame_1_1, text="Очистить выбор", command=clear)
tasks=[]
tasks_var=tk.StringVar(value=tasks)
List=tk.Listbox(frame_2, listvariable=tasks_var, xscrollcommand=True)



task_label.pack(anchor="nw", padx=5, pady=5 )
task.pack(fill="x", anchor="ne", padx=5, pady=5)

choose_label.pack(side=tk.LEFT)

btn1_ch.pack(padx=5, pady=5, side=tk.LEFT)
btn2_ch.pack(side=tk.LEFT, padx=5, pady=5)
btn3_ch.pack(side=tk.LEFT, padx=5, pady=5)

btn_clear_ch.pack(padx=5, pady=5)

frame_1_1.pack(fill="x", expand=True)
btn_save.pack(side=tk.RIGHT, fill="x", padx=5, pady=5, expand=True)
btn_clear.pack(side=tk.LEFT, fill="x", padx=5, pady=5, expand=True)

frame_1.pack(fill="x", anchor="n")

List.pack(fill="both", expand=True, anchor="s")
frame_2.pack(fill="both", expand=True, anchor="n")

root.mainloop()
