from decimal import *
a=Decimal(input())
b=str(input())
c=Decimal(input())

if b=="+":
    print("Результат:", a+c)
elif b=="-":
    print("Результат:", a-c)
elif b=="*":
    print("Результат:", a*c)
elif b=="/":
    print("Резуьтат:", a/c)
elif b=="**":
    print("Резуьтат:", a**c)
elif b=="//":
    print("Резуьтат:", a//c)
elif b=="%":
    print("Резуьтат:", a%c)
else:
    print("Операция не определена")
