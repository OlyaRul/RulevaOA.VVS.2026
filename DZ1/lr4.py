from decimal import Decimal
from math import *
class Calc:
    '''
создаем класс простейших калькуляторов
для выполнения стандартных арифметических действий
'''
    def __init__(self, num):
        self.num=num
        
    
    def plus(self, num2):
        self.num+=num2
        

    def minus(self, num2):
        self.num-=num2
        
    
    def umn(self, num2):
        self.num*=num2
       
    
    def d(self, num2):
        if num2==0:
            print("Делить на ноль нельзя!")
            return
        self.num/=num2
        

    

calc1=Calc(Decimal(1))
'''
Создаем экземпляр класса для дальнейших расчетов
'''


class Calories_calc(Calc):
    '''
Создаем класс-наследник,
с помощью которого реализуем калькулятор КБЖУ
'''
    def __init__(self, num):
        self.num=num
    
    def BMR(self, s, w, h, a):
        '''
Реализуем формулу Миффлина-Сан-Жеора для расчета базового обмена.
На вход принимаем пол, вес, рост, массу, на выходе аргументом экземпляра становится базовый обмен веществ
'''
        if s==0:
            self.num=Decimal(5)
        else:
            self.num=Decimal(-161)
        calc1.num=Decimal(10)
        calc1.umn(w)
        self.plus(calc1.num)
        calc1.num=Decimal(6.25)
        calc1.umn(h)
        self.plus(calc1.num)
        calc1.num=Decimal(5)
        calc1.umn(a)
        self.minus(calc1.num)
        
    def daynorm(self, act, p):
        '''
Реализуем метод, подсчитывающий дневную норму.
На вход принимаем экземпляр, аргумент которого равен базовому обмену,
а так же уровень активности и цель
После применения метода аргументом экземпляра становится дневная норма калорий

'''
        self.umn(act)
        if p==-1:
            self.umn(Decimal(0.9))
        elif p==1:
            self.umn(Decimal(1.1))
    def  imt(self, w, r):
        ''' Реализация метода подсчета ИМТ
На вход получаем вес и рост,
На выходе аргументом экземпляра становится ИМТ пользователя
'''
        self.num=w
        self.d(r)
        self.d(r)
CC=Calories_calc(0)
print("Расчет суточной нормы калорий, КБЖУ, ИМТ тела")
while True:
    print('')
    print("Что хотели бы рассчитать?")
    print("0 - расчет базового обмена веществ")
    print("1 - расчет суточной нормы калорий")
    print("2 - расчет индекса массы тела")
    print("3 - расчет КБЖУ на сутки")
    f=int(input("Введите соответсвующую цифру: "))
    if f==0 or f==1 or f==3:
        s=Decimal(input("введите 0 - если вы мужчина, 1 - если вы женщина: "))
        w=Decimal(input("введите Ваш вес в килограммах: "))
        h=Decimal(input("введите Ваш рост в см: "))
        a=Decimal(input("введите Ваш возраст в годах: "))
        CC.BMR(s, w, h, a)
        if f==0:
            print("Ваш базовый обмен веществ составляет ",round(CC.num, 2), "Ккал")
        else:
            print("Выберите коэффициент своего уровня активности: ")
            print("1.2 — сидячий образ жизни, без спорта")
            print("1.375 — легкие тренировки или долгая ходьба 1–3 раза в неделю")
            print("1.55 — умеренная активность, тренировки 3–5 раз в неделю")
            print("1.725 — интенсивные тренировки 6–7 раз в неделю")
            print("1.9 — тяжелая физическая работа или профессиональный спорт")
            act=Decimal(input())
            print("Ваша цель:")
            print(" -1 - похудение, 0 - поддержка веса, 1 - набор массы")
            p=Decimal(input())
            CC.daynorm(act, p)
            if f==1:
                print("Ваша суточная норма калорий составляет: ", round(CC.num, 2))
            else:
                n=CC.num
                CC.umn(Decimal(0.3))
                CC.d(Decimal(4))
                print("Белки:", round( CC.num, 2))
                CC.num=n
                CC.umn(Decimal(0.3))
                CC.d(Decimal(9))
                print("Жиры:", round(CC.num, 2))
                CC.num=n
                CC.umn(Decimal(0.4))
                CC.d(Decimal(4))
                print("Углеводы:", round(CC.num, 2))
                                      
    elif f==2:
        w=Decimal(input("Ваш вес в кг: "))
        r=Decimal(input("Ваш рост в м: "))
        CC.imt(w, r)
        print("Ваш ИМТ составляет ", round(CC.num, 2), "кг/м^2")

            
            
