import copy
import random
ts=[]

'''Создаем класс предметов - каждый обладает именем, уровнем урона, защиты, питательности и знаний'''

class thing():
    def __init__(self, name, harm, protection, health, knowledge):
        self.harm=harm
        self.protection=protection
        self.name=name
        self.health=health
        self.knowledge=knowledge
        ts.append(self)

'''Задаем параметры лабиринта'''

l=list()
vnesh_l=list()
true_l=list()
n= int(input("Ширина лабиринта:"))
m=int(input("Длина лабиринта: "))
vnesh_l=[['*' for j in range(n)] for i in range(m)]
true_l=[[1 for j in range(n)] for i in range(m)]
vnesh_l[0][0]='O'

'''Генерируем предметы'''

key=thing('ключ', 1, 0, 0, 0)
potion1=thing('простое зелье', 0, 0, 25, 25)
potion2=thing('супер-зелье', 0, 0, 100, 100)
potion3=thing('опасное зелье', 0, 0, -30, -10)
mushroom=thing('гриб', 0, 0, -50, -5)
pie=thing('яблоко', 1, 0, 5, 0)
sweet=thing('бутерброд', 0, 0, 10, 0)
meat=thing('кусок мяса', 1, 1, 15, 0)
axe=thing('топор', 30, 0, -10, 0)
hammer=thing('молот', 30, 0, -10, 0)
sword=thing('меч', 50, 10, -10, 0)
gun=thing('гранатомет', 65, 10, -5, 0)
screen=thing('щит', 5, 30, -3, 0)
armor=thing('доспехи', 0, 75, 0, 0)
book=thing('книга', 0, 5, 0, 55)
stone=thing('камень', 5, 0, -5, 0)
ferrum=thing('кусок железа', 7, 0, -3, 0)
none=thing('.', 0, 0, 0, 0)



'''Создаем список для хранения координат открытых сундуков - новых предметов в них появляться не будет'''
open_cases=list()

'''Генерируем лабиринт размера n*m, заполняем его
случайными числами - типами комнат'''


for i in range(int(m*n/5)):
    true_l[int((m)*random.random())][int((n)*random.random())]=5;
    true_l[int((m)*random.random())][int((n)*random.random())]=4;
    true_l[int((m)*random.random())][int((n)*random.random())]=3;
    true_l[int((m)*random.random())][int((n)*random.random())]=2;


'''Добавляем выход и вход'''
true_l[-1][-1]=6
true_l[0][0]=0

'''Печатаем лабиринт'''
for i in range(m):
    print(*vnesh_l[i])



'''Задаем параметры игрока - координаты,
уровень здоровья и опыта,
рюкзак с инвентарем(пока пустой),
размеры рюкзака'''
x=0
y=0
staff=list()
hp=100
kp=10
size=15
f=1
staff=list()
'''Запускаем игру'''
neportal=True
while True:
    '''Проверяем, был ли предыдущий шаг из портала'''
    
    if neportal:
        step=input("Воспользуйтесь клавишами a, w, d, s чтобы сделать ход, z - чтобы посмотреть инвентарь: ")
        if step=='z':
            copy_staff=copy.deepcopy(staff)
            hpcopy=hp
            kpcopy=kp
            while True:
                '''Взаимодействие с инвентарем.
                Принимаем на вход желаемое действие,
                производим требуемые манипуляции с инвентарем'''
                for i in range(len(staff)):
                    print(i+1, ".", staff[i].name)
                print("")
                print("1 - Выбросить ненужное")
                print("2 - узнать характеристики")
                print("3 - навести порядок")
                print("4 - найти элемент")
                print("5 - создать новый элемент, использовать существующий")
                print("6 - сохранить и выйти")
                print("7 - выйти без сохранения")
                d=int(input("Что вы хотите сделать?"))
                if d==7:
                    staff=copy.deepcopy(copy_staff)
                    hp=hpcopy
                    kp=kpcopy
                    break
                elif d==6:
                    break
                elif d==4:
                    el=input("Что хотите найти?")
                    st_names=[i.name for i in staff]
                    if el in st_names:
                        print(f'{el.capitalize()} в вашем рюкзаке под номером {st_names.index(el)+1}')
                    else:
                        print(f'Вы перерыли весь рюкзак, но так и не нашли {el.lower()}...')

                elif d==5:
                    print("Создавать новые элементы можно только обладая очками знаний (kp) >=50")
                    d=int(input("1- создать элемент, 0 - использовать существующий"))
                    if d==1 and kp>=50:
                        if (hammer in staff or axe in staff):
                            mat=input("Выберите материал: 1 - железо, 2 - камень (из того, что есть у вас в рюкзаке)")
                            if mat=="2" and stone in staff:
                                r=int(input("что хотите создать? 1 - доспехи, 2 - щит, 3 - молот"))
                                if r==1:
                                    staff.remove(stone)
                                    staff.append(armor)
                                elif r==2:
                                    staff.remove(stone)
                                    staff.append(screen)
                                else:
                                    staff.remove(stone)
                                    staff.append(hammer)
                            elif ferrum in staff and mat=="1":
                                r=int(input("что хотите создать? 1 - доспехи, 2 - меч, 3 - топор"))
                                if r==1:
                                    staff.remove(ferrum)
                                    staff.append(armor)
                                elif r==2:
                                    staff.remove(ferrum)
                                    staff.append(sword)
                                else:
                                    staff.remove(ferrum)
                                    staff.append(axe)
                            else:
                                print("Нет нужного материала!")
                        else:
                            print("нужен топор или молот!")
                    elif d==1 and kp<50:
                        print("вы пока не можете создавать предметы")
                    else:
                        el=int(input("Введите номер предмета: "))-1
                        if hp+staff[el].health>100:
                            hp=100
                        else:
                            hp+=staff[el].health
                        if kp+staff[el].knowledge>100:
                            kp=100
                        else:
                            kp+=staff[el].knowledge
                        staff.pop(el)
                        if hp<0:
                            print("Игра окончена. Не стоило есть всякую гадость...")
                            f=0;
                            break
                        print(f'hp: {hp} kp: {kp}')                       
                
                elif d==3:
                    print("1 - по алфавиту")
                    print("2 - по урону")
                    print("3 - по степени защиты")
                    print("4 - по пользе для здоровья")
                    print("5 - по знаниям")
                    
                    el=int(input("По чему хотели бы сортировать?"))
                    if el==1:
                        staff.sort(key=lambda x: x.name)
                    elif el==2:
                        staff.sort(key=lambda x: -x.harm)
                    elif el==3:
                        staff.sort(key=lambda x: -x.protection)
                    elif el==4:
                        staff.sort(key=lambda x: -x.health)
                    elif el==5:
                        staff.sort(key=lambda x: -x.knowledge)
                    
                elif d==2:
                    el=int(input("Номер элемента: "))-1
                    print("Имя: ", staff[el].name," урон: ", staff[el].harm, " защита: ", staff[el].protection, " питательность: ", staff[el].health, " знания: ", staff[el].knowledge)
                elif d==1:
                    el=int(input("Номер элемента: "))-1
                    staff.pop(el)
                    print("Удалено")        

        if f==0:
            break

        '''обработка ходов - на вход принимаем направление хода,
        возвращаем новое состояние лабиринта. Если ход предполагает
        выход за границы лабиринта, выводим предупрежение'''        
        if step=="a":
            if y==0:
                print("Недопустимый ход")
                continue
            vnesh_l[x][y]="."
            y=y-1
            vnesh_l[x][y]="O"
        if step=="s":
            if x==m-1:
                print("Недопустимый ход")
                continue
            vnesh_l[x][y]="."
            x=x+1
            vnesh_l[x][y]="O"
        if step=="w":
            if x==0:
                print("Недопустимый ход")
                continue
            vnesh_l[x][y]="."
            x=x-1
            vnesh_l[x][y]="O"
        if step=="d":
            if y==n-1:
                print("Недопустимый ход")
                continue
            vnesh_l[x][y]="."
            y=y+1
            vnesh_l[x][y]="O"
        '''Обрабатываем ситуацию, когда предыдущий ход был в портал'''
    else:
        neportal=True;
        vnesh_l[x][y]="."
        x=int((m)*random.random())
        y=int((n)*random.random())
        vnesh_l[x][y]="O"



            

    '''Выводим обновленный лабиринт, показатели очков жизни и знаний'''
    for i in range(m):
        print(*vnesh_l[i])
    print("hp", hp, "kp", kp)
    
 

    '''Если комната с ключом, сообщаем об этом игроку'''
    if true_l[x][y]==1:
        print("Тут пусто...")
        continue
    elif true_l[x][y]==4:
        print("Неужели, Вы нашли Ключ!")
        d=input("Нажмите 1 - чтобы забрать")
        if d=='1':
            if len(staff)<size:
                staff.append(key)
            else:
                print("У вас уже есть ключ!")
        continue
    '''Команата с выходом. Конец игры'''       
    elif true_l[x][y]==6:
        print("Здесь выход! Воспользуйтесь ключом, чтобы завершить игру")
        print("1-воспользоваться")
        d=input()
        if d=='1':
            if key in staff:
                print("Вы выбрались на свободу! Поздравляем!")
                break
            else:
                print("У вас нет ключа, чтобы открыть эту дверь. Найдите ключ в лабиринте")
                continue

    
    elif true_l[x][y]==5:
        print("Вы попали в портал! Где вы окажетесь дальше, не может предсказать даже создатель игры...")
        true_l[x][y]=1
        neportal=False
        continue
    elif true_l[x][y]==3:
        print("О нет! В этой комнате монстр!!!")
        monstr=int((100)*random.random())
        print("Выберите, чем будете защищаться!")
        d=input("1 - выбрать оружие и защиту, любая другая клавиша - получить по голове")
        if d=="1":
            print("Предмет   Урон   Защита")
            for i in staff:
                print(i.name(), i.harm(), i.protection())
            t1=int(input("Введите номер предмета "))-1
            d=input("1- для выбора еще одного предмета")
            if d=='1':
                t2=int(input("Введите номер предмета "))-1
                if t1==t2:
                    print("Этот предмет уже был выбран!")
            if monstr<=staff[t1].harm()+staff[t2].harm():
                print("Вы победили монстра!")
                true_l[x][y]=1
                continue
            else:
                uron=(monstr-staff[t1].harm()-staff[t2].harm())*2-staff[t1].protection()-staff[t2].protection()
        else:
            uron=monstr
        if uron <=0:
            print("Вы смогли защититься от монстра. Он испугался и больше вас не побеспокоит")
            true_l[x][y]=1
        elif hp-uron>0:
            print("Вы смогли сбежать от монстра. Но он может отомстить...")
            hp=hp-uron
        else:
            print("Вы погибли в неравной схватке с монстром... Жаль, но игра окончена")
            break
    elif true_l[x][y]==2:
        print("Здесь сундук!")
        print("1- посмотреть содержимое")
        print("2 - пойти дальше")
        d=int(input())
        if d==2:
            continue
        else:
            
            if [x, y] in open_cases:
                case=[ts[int(random.random()*18)] for i in range(1)]
                case.extend([none, none, none, none])
            else:
                case=[ts[int(random.random()*18)] for i in range(5)]
                open_cases.append([x, y])
            
            while True:
                for i in range(5):
                    print(case[i].name)
                d=int(input("Выберите номер вещи, которую хотите забрать. Нажмите 0 для выхода, -1 чтобы забрать все, -2 - чтобы положить что-то в сундук"))-1
                if d==-1:
                    break
                elif d==-3:
                    while none in case:
                        for i in range(len(staff)):
                            print(staff[i].name)
                        k=int(input("Выберите элемент, который хотите положить в сундук. Если закончили - нажмите 0"))-1
                        if k==-1:
                            break
                        else:
                            case.append(staff.pop(k))
                            case.remove(none)
                            continue
                        
                elif d==-2:
                    case=[i for i in case if i!=none]
                    if len(staff)+len(case)<=size:
                        staff.extend(case)
                        case=[none for i in range(5)]
                        
                else:
                    if len(staff)<size:
                        staff.append(case.pop(d))
                        case.append(none)
                    else:
                        print("Не хватает места в рюкзаке!")
                        break
            
                        
                        
        
        
    

        
    
            
                    
                    
            
            
                
        
        
        
        
                
            
                
            
        
    
        
    
        
