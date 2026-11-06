from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import sys
import qdarktheme
'''Основное окно'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
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
        self.Table.itemClicked.connect(self.f_click_item)
        main_layout.addWidget(self.Table)

        main_widget=QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
    '''Очищаем поле ввода и приоритет'''
    def f_clear(self):
        self.task_entry.clear() 
        self.five.setChecked(True) 

    '''Очищаем поле приоритетов'''
    def f_clearch(self):
        self.five.setChecked(True) 
    '''Добавляем задачу, проверяя возможность ее добавления'''
    def f_add_task(self):
        a=4
        self.count+=1
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

        lay=QVBoxLayout()
        layout.addWidget(label)
        layout.addLayout(lay_btn)
        self.setLayout(layout)
    '''Корректное удаление окна - поправляем индексы последних элементов категорий, удаляем саму задачу, закрываем окно'''
    def func(self):
        ind=self.main_window.Table.row(self.item)
        self.main_window.Table.takeItem(ind)
        for i in range(3):
            if self.main_window.last_indexes[i] > ind:
                self.main_window.last_indexes[i]-=1

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


app = QApplication(sys.argv)
theme_style = qdarktheme.load_stylesheet("dark")
app.setStyleSheet(theme_style)
window = MainWindow()
window.show() 
sys.exit(app.exec()) 
