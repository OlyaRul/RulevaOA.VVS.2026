import tkinter as tk
from tkinter import ttk
 

def task_select(event):
    def del_task():
        List.delete(List.curselection())
        win1.destroy()
    if not List.curselection():
        return
    win1=tk.Toplevel(root)
    label_1=tk.Label(win1, text="Удалить задачу?")
    btn_del_task=ttk.Button(win1, text="Да", command=del_task)
    btn_ret=ttk.Button(win1, text="Нет", command=win1.destroy)
    label_1.pack(anchor="n")
    btn_del_task.pack(side='left')
    btn_ret.pack(side='right')

'''Очистка поля ввода, приоритета при сбросе задачи'''
def Clear_entry():
    global task
    task.delete(0, "end")
    clear()

def donut():
    def yes():
        win1.destroy()
        win2=tk.Toplevel(root)
        win2.geometry("250x100")
        l=ttk.Label(win2, wraplength=200, text="Вы можете поблагодарить разработчика, отправив пару червонцев на покушать (+79191972150 - сбер). Общажная жизнь нелегкая...")
        l.pack(expand=True)
    def no():
        win1.destroy()
        win2=tk.Toplevel(root)
        
        l=ttk.Label(win2, text="Мы постараемся стать лучше!")
        l.pack(expand=True)

    win1=tk.Toplevel(root)
    win1.geometry("250x100")
    lab=ttk.Label(win1, text="Вам нравится менеджер задач?")
    btn1=ttk.Button(win1, text="Да, все круто!", command=yes)
    btn2=ttk.Button(win1, text="Не нравится, переделывай", command=no)
    lab.pack(anchor="n")
    btn1.pack(side="left", expand=True)
    btn2.pack(side="right", expand=True)


'''Добавление новой задачи'''
def new_task():
    global counter
    counter+=1
    if counter%5==0:
        donut()
    global List
    global var
    if var.get()==0:
        err()
    else:
        List.insert(last_elems[var.get()], task.get())
        for i in range(var.get(), 4):
            last_elems[i]+=1
        Clear_entry()


def err():
    win=tk.Toplevel(root)
    win.title("Предупреждение!")
    win.geometry("300x50")
    win_l=ttk.Label(win, text="Выберите приоритет!")
    win_l.pack(expand=True)

last_elems=dict.fromkeys([1, 2, 3], 0)
root=tk.Tk()
root.title("Менеджер задач")
root.geometry("900x600")
counter=0
style=ttk.Style()
style.theme_use('clam')
style.configure("TLabel",  font="arial 13", foreground="#230333", background="#cba4de",  padding=15) 
style.configure("TButton",  font="arial 13", foreground="#230333", background="#b27ccc", bordercolour="#8c50ad", padding=15) 
style.configure("TFrame",  font="arial 13", foreground="#230333", background="#cba4de", bordercolour="#9d69b8", padding=8) 


'''Обработка нажатия на событие'''
'''Создаем контейнеры. Frame 1 - для части с кнопками, вводом задач. Frame 2 - сам todo-лист'''
frame_1=ttk.Frame(borderwidth=10)
frame_1_1=ttk.Frame( frame_1, borderwidth=10)
frame_2=ttk.Frame(borderwidth=10)

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
List=tk.Listbox(frame_2, listvariable=tasks_var, xscrollcommand=True, selectmode="single")
List.bind("<<ListboxSelect>>", task_select)


task_label.pack(anchor="nw" )
task.pack(fill="x", anchor="ne")

choose_label.pack(side=tk.LEFT)

btn1_ch.pack(side=tk.LEFT)
btn2_ch.pack(side=tk.LEFT)
btn3_ch.pack(side=tk.LEFT)

btn_clear_ch.pack()

frame_1_1.pack(fill="x", expand=True)
btn_save.pack(side=tk.RIGHT, fill="x", expand=True)
btn_clear.pack(side=tk.LEFT, fill="x", expand=True)

frame_1.pack(fill="x", anchor="n")

List.pack(fill="both", expand=True, anchor="s")
frame_2.pack(fill="both", expand=True, anchor="n")

root.mainloop()
