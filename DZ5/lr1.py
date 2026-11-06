import tkinter as tk
from tkinter import ttk
 

def task_select(event):
    def del_task():
        List.delete(List.selection())
        win1.destroy()
    if not List.selection() or (List.selection()[0] in category.values()):
        return
    win1=tk.Toplevel(root, background="#FFC091")
    label_1=ttk.Label(win1, text="Удалить задачу?")
    btn_del_task=ttk.Button(win1, text="Да", command=del_task, style="bad.TButton")
    
    btn_ret=ttk.Button(win1, text="Нет", command=win1.destroy, style="good.TButton")
    
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
        win2=tk.Toplevel(root, background="#FFC091")
        win2.geometry("250x200")
        l=ttk.Label(win2, wraplength=200, text="Вы можете поблагодарить разработчика, отправив пару червонцев на покушать (+79191972150 - сбер). Общажная жизнь нелегкая...")
        l.pack(expand=True)
    def no():
        win1.destroy()
        win2=tk.Toplevel(root, bg="#FFC091")
        
        l=ttk.Label(win2, text="Мы постараемся стать лучше!", font="arial 13", foreground="#673404", background="#f6aa63",  padding=10)
        l.pack(expand=True)

    win1=tk.Toplevel(root, bg="#FFC091")
    win1.geometry("400x100")
    lab=ttk.Label(win1, text="Вам нравится менеджер задач?")
    btn1=ttk.Button(win1, text="Да, все круто!", command=yes, style="good.TButton")
    btn2=ttk.Button(win1, text="Не нравится, переделывай", command=no, style="bad.TButton")
    lab.pack(anchor="n")
    btn1.pack(side="left", expand=True)
    btn2.pack(side="right", expand=True)


'''Добавление новой задачи'''
def new_task(event=None):
    global counter
    counter+=1
    if counter%5==0:
        donut()
    global List
    global var
    if var.get()==0:
        err()
    else:
        List.insert(category[var.get()], tk.END, text=task.get(), value=task.get())
        
        Clear_entry()


def err():
    win=tk.Toplevel(root, background="#FFA591")
    win.title("Предупреждение!")
    win.geometry("300x50")
    win_l=ttk.Label(win, text="Выберите приоритет!", background="#FFA591", foreground="#6A281A")
    win_l.pack(expand=True)

root=tk.Tk()
root.config(bg="#FFC091")  
root.title("Менеджер задач")
root.geometry("900x600")
counter=0
style=ttk.Style()
style.theme_use('clam')
style.configure("TLabel",  font="arial 13", foreground="#673404", background="#f6aa63",  padding=10) 
style.configure("TButton",  font="arial 13", borderwidth=0, foreground="#673404", background="#fd9637", bordercolour="#fd9637", padding=10) 
style.configure("TRadiobutton", font="arial 13", borderwidth=0, foreground="#673404", background="#fd9637", bordercolour="#fd9637", padding=10)
style.configure("TFrame", font="arial 13", borderwidth=0, foreground="#673404", background="#FFC091", padding=10)
style.configure("Treeview", font="arial 13", foreground="#673404", background="#ffe4cb", rowheight=35, fieldbackground="#ffe4cb")
style.map("TButton", background=[("active", "#d68840")], foreground=[("active", "#3d1e02")]) 
style.map("TRadiobutton", background=[("active", "#d68840")], foreground=[("active", "#3d1e02")]) 
style.map("Treeview", background=[("active", "#d68840")], foreground=[("active", "#3d1e02")]) 
style.configure("bad.TButton", foreground="#672004", background="#ff7e5b")
style.configure("good.TButton", foreground="#0D2600", background="#60a357")

'''Обработка нажатия на задачу'''
'''Создаем контейнеры. Frame 1 - для части с кнопками, вводом задач. Frame 2 - сам todo-лист'''
frame_1=ttk.Frame()
frame_1_1=ttk.Frame(frame_1)
frame_2=ttk.Frame()

btn_save=ttk.Button(frame_1, text="Внести в список", command=new_task, style="good.TButton")
btn_clear=ttk.Button(frame_1, text="Сбросить", command=Clear_entry, style="bad.TButton")
task_label=ttk.Label(frame_1, text='Введите задачу: ')
task=tk.Entry(frame_1, font="arial 13", foreground="#673404", background="#ffe4cb")
task.bind("<Return>", new_task)


var=tk.IntVar(value=0)
def clear():
    global var
    var.set(0)
choose_label=ttk.Label(frame_1_1, text="Выберите приоритет:")
btn1_ch=ttk.Radiobutton(frame_1_1, text="Срочный", variable=var, value=1)
btn2_ch=ttk.Radiobutton(frame_1_1, text="Важный",  variable=var, value=2)
btn3_ch=ttk.Radiobutton(frame_1_1, text="Обычный",  variable=var, value=3)
btn_clear_ch=ttk.Button(frame_1_1, text="Очистить выбор", command=clear)

btn1_ch.bind("<Return>", new_task)
btn2_ch.bind("<Return>", new_task)
btn3_ch.bind("<Return>", new_task)
tasks=[]
tasks_var=tk.StringVar(value=tasks)

List=ttk.Treeview(frame_2, xscrollcommand=True, selectmode="browse", show="tree")
id_urgent = List.insert("", tk.END, text="Срочное")
id_important = List.insert("", tk.END, text="Важное")
id_normal = List.insert("", tk.END, text="Обычное")

category={1: id_urgent, 2: id_important, 3: id_normal}
List.bind("<<TreeviewSelect>>", task_select)


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
