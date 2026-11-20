from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import sys
import qdarktheme

import sqlite3


'''Создаем базу данных - две таблицы. Одна содержит имя пользователя, пароль и id.
 Вторая содержит id задачи, Id пользователя, текст задачи, приоритет, метку о выполнении'''
con = sqlite3.connect("data.db", timeout=5.0)
cursor = con.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS people
                (id INTEGER PRIMARY KEY,  
                username TEXT NOT NULL UNIQUE, 
                password TEXT NOT NULL)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS tasks
                (id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL,
                task TEXT NOT NULL,
                priority INTEGER NOT NULL,
                is_done INTEGER NOT NULL DEFAULT 0,
                FOREIGN KEY (user_id)
                REFERENCES people(id))""")




'''Основное окно'''
class MainWindow(QMainWindow):
    def __init__(self, id):
        super().__init__()
        self.id=id
        self.resize(750, 500)
        '''Тут будем хранить последние индексы каждой категории, чтобы корректно добавлять элементы'''
        self.last_indexes=[0, 0, 0]
        self.count=0
        self.setWindowTitle("Task Manager")


        '''Реализуем основные кнопки и поля ввода'''
        self.btn_clear=QPushButton("Сбросить")
        self.btn_clear.clicked.connect(self.f_clear)
        self.btn_add=QPushButton("Добавить задачу")
        self.btn_add.clicked.connect(self.f_add_task)
        self.task_entry=QLineEdit()
        self.one=QRadioButton("Срочный")
        self.two=QRadioButton("Важный")
        self.three=QRadioButton("Обычный")
        self.four=QPushButton("Очистить выбор")
        self.four.clicked.connect(self.f_clearch)
        self.five=QRadioButton()
        self.label_choose=QLabel("Выберите приоритет:")
        main_layout=QVBoxLayout()
        
        '''Группируем кнопки выбора приоритета'''
        self.gr=QButtonGroup()
        self.gr.addButton(self.one)
        self.gr.addButton(self.two)
        self.gr.addButton(self.three)
        self.gr.addButton(self.five)
        self.five.setChecked(True)
        '''Объединяем элементы в layout для корректного отображения'''
        entry_layout=QFormLayout()
        entry_layout.addRow("Введите задачу", self.task_entry)

        choise_layout=QVBoxLayout()
        choise_layout.addWidget(self.label_choose)
        choise_layout.addWidget(self.one)
        choise_layout.addWidget(self.two)
        choise_layout.addWidget(self.three)
        choise_layout.addWidget(self.four)

        btn_layout=QHBoxLayout()
        btn_layout.addWidget(self.btn_clear)
        
        btn_layout.addWidget(self.btn_add)
        main_layout.addLayout(entry_layout)
        main_layout.addLayout(choise_layout)
        main_layout.addLayout(btn_layout)
        self.Table=QListWidget()
        self.Table.itemDoubleClicked.connect(self.f_click_item)
        main_layout.addWidget(self.Table)
        self.Table.itemChanged.connect(self.task_completed)
        main_widget=QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)


        '''Добавляем задачи пользователя из базы данных'''

        cursor.execute("""SELECT * FROM tasks WHERE user_id = ?""", (id, ))
        tasks=cursor.fetchall()

        for task in tasks:
            text=task[2]
            a=task[3]
            isdone=task[4]
            task_id=task[0]
            t=QListWidgetItem(text)
            if isdone==0:
                t.setCheckState(Qt.CheckState.Unchecked)
            else:
                t.setCheckState(Qt.CheckState.Checked) 
            t.setData(Qt.ItemDataRole.UserRole, task_id)   
            ind=self.last_indexes[a]
            for i in range(a, 3):
                self.last_indexes[i]+=1
            self.Table.insertItem(ind, t)
   
                       
    """Если задача меняет статус выполнения - записываем это изменение в БД"""                        
    def task_completed(self, item):
        is_done = 1 if item.checkState() == Qt.CheckState.Checked else 0
        task_id = item.data(Qt.ItemDataRole.UserRole)
        if task_id is None:
            return
        cursor.execute("""UPDATE tasks SET is_done = ? WHERE id = ?""", (is_done, task_id))
        con.commit()

    '''Очищаем поле ввода и приоритет'''
    def f_clear(self):
        self.task_entry.clear() 
        self.five.setChecked(True) 

    '''Очищаем поле приоритетов'''
    def f_clearch(self):
        self.five.setChecked(True) 
    '''Добавляем задачу, проверяя возможность ее добавления'''
    def f_add_task(self):
        self.count+=1
        a=4
        task=QListWidgetItem(self.task_entry.text())
        task.setCheckState(Qt.CheckState.Unchecked)
        if self.five.isChecked():
            a=4
        if self.one.isChecked():
            a=0
        if self.two.isChecked():
            a=1
        if self.three.isChecked():
            a=2
        if a==4:
            self.warning_priority()
        else:
            if len(task.text())<5:
                self.little_task()
            else:
                ind=self.last_indexes[a]
                for i in range(a, 3):
                    self.last_indexes[i]+=1
                self.Table.insertItem(ind, task)
                self.f_clear()
                """Дописываем данные о задаче в БД"""
                cursor.execute("""INSERT INTO tasks (user_id, task, priority, is_done) VALUES (?, ?, ?, ?)""", (self.id, task.text(), a, 0))
                con.commit()
                task.setData(Qt.ItemDataRole.UserRole, cursor.lastrowid)
                
        if self.count%5==0:
            self.win=DonutWin()
            self.win.exec()
    def little_task(self):
        self.win=LittleWin()
        self.win.show()
    '''Предупреждение о необходимости приоритета'''
    def warning_priority(self):
        self.wwindow = WarningWindow()
        self.wwindow.show()
    '''Реализуем функцию удаления при нажатии на элемент списка'''
    def f_click_item(self, item):
        self.window=ItemWindow(self, item)
        self.window.exec()
'''Класс для окна донатов - выводится после добавления каждой пятой задачи'''
class DonutWin(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Донат")
        self.resize(300, 100)
        label = QLabel("Если Вам нравится приложение, Вы можете порадовать разработчиков десятком золотых - по номеру +79191972150 на сбер. Общажная жизнь нелегкая...")
        label.setWordWrap(True) 
        btn=QPushButton("Учту!")
        layout = QVBoxLayout()
        btn.clicked.connect(self.close)
        layout.addWidget(label)
        layout.addWidget(btn)
        self.setLayout(layout)
'''Подтверждение удаления задачи'''        
class ItemWindow(QDialog):
    def __init__(self, main_window, item):
        super().__init__()
        self.main_window = main_window
        self.item = item
        self.setWindowTitle("Удаление")
        self.resize(300, 100)
        layout = QVBoxLayout()
        label = QLabel("Хотите удалить задачу?")
        btn=QPushButton("Да")
        btn.clicked.connect(self.func)
        btn2=QPushButton("Нет")
        btn2.clicked.connect(self.close)
        lay_btn=QHBoxLayout()
        lay_btn.addWidget(btn2)
        lay_btn.addWidget(btn)
        layout.addWidget(label)
        layout.addLayout(lay_btn)
        self.setLayout(layout)
    '''Корректное удаление окна - поправляем индексы последних элементов категорий, удаляем саму задачу, закрываем окно'''
    def func(self):
        ind=self.main_window.Table.row(self.item)
        task_id=self.item.data(Qt.ItemDataRole.UserRole)
        self.main_window.Table.takeItem(ind)
        for i in range(3):
            if self.main_window.last_indexes[i] > ind:
                self.main_window.last_indexes[i]-=1
        
        cursor.execute("""DELETE FROM tasks WHERE id = ?""", (task_id,))
        con.commit()

        self.accept()
                
        


'''Окно-предупреждение о необходимости выбора приоритета'''
class WarningWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Предупреждение")
        self.resize(300, 100)
        
    
        layout = QVBoxLayout()
        label = QLabel("Введите приоритет!")
        btn=QPushButton("Понято-Принято")
        btn.clicked.connect(self.close)
        layout.addWidget(label)
        layout.addWidget(btn)
        self.setLayout(layout)


'''Окно для контроля корректности ввода'''
class LittleWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Предупреждение")
        self.resize(300, 100)
        
    
        layout = QVBoxLayout()
        label = QLabel("Задача должна содержать не менее 5 символов!")
        btn=QPushButton("Понято-Принято")
        btn.clicked.connect(self.close)
        layout.addWidget(label)
        layout.addWidget(btn)
        self.setLayout(layout)


'''Приветственное окно'''
class Login(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")
        self.resize(350, 150)
        layout = QVBoxLayout()
        label = QLabel("Уже есть аккаунт?")
        lay1=QHBoxLayout()
        btn_entry=QPushButton("Да")
        btn_reg=QPushButton("Нет")
        lay1.addWidget(btn_entry)
        lay1.addWidget(btn_reg)
        btn_entry.clicked.connect(self.entry)
        btn_reg.clicked.connect(self.reg)
        layout.addWidget(label)
        layout.addLayout(lay1)
        self.setLayout(layout)
    '''При нажатии на кнопку "есть аккаунт", данная функция открывает окно для воода логина и пароля'''
    def entry(self):
        self.win = EntryWindow()
        self.win.show()
        self.close()
    '''При нажатии на кнопку "нет аккаунта", данная функция открывает окно регистрации'''
    def reg(self):
        self.win = RegWindow()
        self.win.show()
        self.close()

'''Класс окна регистрации'''
class RegWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Регистрация")
        self.resize(350, 150)
        layout = QVBoxLayout()
        self.login=QLineEdit()
        self.password=QLineEdit()
                
        btn_entry=QPushButton("Зарегистрироваться")
        btn_entry.clicked.connect(self.entry)
        log_layout=QFormLayout()
        log_layout.addRow("Логин (username)", self.login)
        log_layout.addRow("Пароль", self.password)
        layout.addLayout(log_layout)
        layout.addWidget(btn_entry)
        self.setLayout(layout)
        self.label=QLabel("Недопустимое имя")
    '''Функция проверяет допустимость введенных данных и открывает окно входа'''
    def entry(self):
        cursor.execute("""SELECT * FROM people WHERE username=?""", (self.login.text(),))
        row= cursor.fetchone()
        if row is not None:
            self.layout().addWidget(self.label)
        else:
            cursor.execute("""INSERT INTO people (username, password) VALUES (?, ?)""", (self.login.text(), self.password.text(),))
            con.commit()
            self.win = EntryWindow()
            self.win.show()
            self.close()
        
'''Класс окна входа'''
class EntryWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вход")
        self.resize(350, 150)
        layout = QVBoxLayout()
        self.login=QLineEdit()
        self.password=QLineEdit()
        
        btn_entry=QPushButton("Войти")
        btn_entry.clicked.connect(self.entry)
        log_layout=QFormLayout()
        log_layout.addRow("Логин", self.login)
        log_layout.addRow("Пароль", self.password)
        layout.addLayout(log_layout)
        layout.addWidget(btn_entry)
        self.setLayout(layout)
        self.label=QLabel("Неверный пароль")
    '''Функция проверяет корректность введенных данных и открывает основное окно'''
    def entry(self):
        cursor.execute("""SELECT * FROM people WHERE username=?""", (self.login.text(),))
        row = cursor.fetchone()
        
        if  row is not None:
            password=row[-1]
            id=row[0]
            if password==self.password.text():
                self.win = MainWindow(id)
                self.win.show()
                self.close()
            else:
                self.layout().addWidget(self.label)

        else:
            self.layout().addWidget(self.label)
        


app = QApplication(sys.argv)

'''Устанавливаем стиль для окна'''
theme_style = qdarktheme.load_stylesheet("dark")
app.setStyleSheet(theme_style)
login = Login()
login.show()
sys.exit(app.exec())         