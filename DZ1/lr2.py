from decimal import *

def plus(a, b):
    '''складывает числа. Принимает на вход два числа, возвращает их сумму'''
    return a+b
def minus(a, b):
    '''Вычитание чисел. Принимает два числа, возвращает разность первого и второго'''
    return a-b
def umn(a, b):
    '''Умножение чисел. Принимает два числа, возвращает их произведение'''
    return a*b
def d(a, b):
    '''Деление чисел. Принимает два числа, возвращает их частное '''
    return a/b

a=Decimal(input())
c=str(input())
b=Decimal(input())
if c=="+":
    print(plus(a, b))
elif c=="-":
    print(minus(a, b))
elif c=="*":
    print(umn(a, b))
elif c=="/":
    print(d(a, b))

  
