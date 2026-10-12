from decimal import *
''' подключаем модуль decimal для точной арифметики '''

def f(a, b, c):
    ''' производим операцию над числами.
Принимает на вход два числа и знак операции,
возвращает результат вычислений'''
    if b=="+":
        return a+c
    elif b=="-":
        return a-c
    elif b=="*":
        return a*c
    elif b=="/":
        return a/c
        
nums=[]
a=Decimal(0)
b=str("0")
ans=Decimal(0)
a=Decimal(input())
b=str(input())
c=Decimal(input())
ans=f(a, b, c)
print(ans)
while True:
    b=str(input())
    c=Decimal(input())
    ans=f(ans, b, c)
    print(ans)
    
