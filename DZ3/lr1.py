import copy
import random
ts=[]

'''Создаем класс предметов - каждый обладает именем, уровнем урона, защиты, питательности и знаний'''

class thing():
    def __init__(self, name, harm, protection, health, knowledge, cat):
        self.harm=harm
        self.protection=protection
        self.name=name
        self.health=health
        self.knowledge=knowledge
        self.cat=cat
        ts.append(self)

'''Задаем параметры лабиринта. На вход принимаем значения длины и ширины лабиринта'''

l=list()
vnesh_l=list()
true_l=list()
n= int(input("Ширина лабиринта:"))
m=int(input("Длина лабиринта: "))
vnesh_l=[['*' for j in range(n)] for i in range(m)]
true_l=[[1 for j in range(n)] for i in range(m)]
vnesh_l[0][0]='O'

'''Генерируем предметы'''

key=thing('ключ', 1, 0, 0, 0, "key")
potion1=thing('простое зелье', 0, 0, 25, 25, "potion")
potion2=thing('супер-зелье', 0, 0, 100, 100, "potion")
potion3=thing('опасное зелье', 0, 0, -30, -10, "potion")
mushroom=thing('гриб', 0, 0, -50, -5, "food")
pie=thing('яблоко', 1, 0, 5, 0, "food")
sweet=thing('бутерброд', 0, 0, 10, 0, "food")
meat=thing('кусок мяса', 1, 1, 15, 0, "food")
axe=thing('топор', 30, 0, -10, 0, "tool")
hammer=thing('молот', 30, 0, -10, 0, "tool")
sword=thing('меч', 50, 10, -10, 0, "weapon")
gun=thing('гранатомет', 65, 10, -5, 0, "weapon")
screen=thing('щит', 5, 30, -3, 0, "protection")
armor=thing('доспехи', 0, 75, 0, 0, "protection")
book=thing('книга', 0, 5, 0, 55, "book")
stone=thing('камень', 5, 0, -5, 0, "mat")
ferrum=thing('кусок железа', 7, 0, -3, 0, "mat")
none=thing('.', 0, 0, 0, 0, "none")

Saxe=thing('Супер - топор', 60, 0, -10, 0, "tool")
Shammer=thing('Супер - молот', 60, 0, -10, 0, "tool")
Ssword=thing('Супер - меч', 100, 20, -20, 0, "weapon")
Sgun=thing('Супер - гранатомет', 100, 50, -5, 0, "weapon")
Sscreen=thing('Супер - щит', 15, 60, -3, 0, "protection")
Sarmor=thing('Супер - доспехи', 10, 100, 0, 0, "protection")



'''Создаем список для хранения координат открытых сундуков - набор предметов в них будет сохраняться'''
open_cases=list()

'''Генерируем лабиринт размера n*m, заполняем его
случайными числами - типами комнат'''


for i in range(int(m*n/5)):
    true_l[int((m)*random.random())][int((n)*random.random())]=5;
    true_l[int((m)*random.random())][int((n)*random.random())]=3;
    true_l[int((m)*random.random())][int((n)*random.random())]=2;


'''Добавляем выход,  вход и ключ (для гарантии проходимости игры)'''

for i in range(max(3, m*n//25)):
    true_l[int((m)*random.random())][int((n)*random.random())]=4;
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


hp=100
kp=10
size=15
f=1
staff=list()

'''Функции для работы с инвентарем.'''

''' На вход ничего не принимаем, откатываем параметры инвентаря до предыдущего сохраненного состояния'''
def exit_without_save():
    staff=copy.deepcopy(copy_staff)
    hp=hpcopy
    kp=kpcopy
    return
'''Поиск предмета в инвентаре по названию. Принимаем имя искомого объекта'''
def finder(el):
    st_names=[i.name for i in staff]
    el=el.lower()
    if el in st_names:
        print(f'{el.capitalize()} в вашем рюкзаке под номером {st_names.index(el)+1}')
    else:
        print(f'Вы перерыли весь рюкзак, но так и не нашли {el.lower()}...')
    return


'''Реализация использования инвентаря и создания новых объектов'''

def maker():
    if (hammer in staff or axe in staff):
        mat=int(input("Выберите номер материала из того, что есть у вас в рюкзаке"))-1
        if  staff[mat].cat=="mat":
            r=int(input("что хотите создать? 1 - доспехи, 2 - щит, 3 - молот"))
            if r==1:
                staff.pop(mat)
                staff.append(armor)
            elif r==2:
                staff.remove(mat)
                staff.append(screen)
            else:
                staff.remove(mat)
                staff.append(hammer)
        else:
            print("Нет нужного материала!")
    else:
        print("нужен топор или молот!")
    return


'''Используем элемент инвентаря. На вход принимаем номер элемента. Реализуем использование элемента'''
def using(el):
    global hp
    global kp
    if hp+staff[el].health>100:
        hp=100
    else:
        hp+=staff[el].health
    if kp+staff[el].knowledge>100:
        kp=100
    else:
        kp+=staff[el].knowledge
    staff.pop(el)
    return 

def sorting(el):
    d={
        1: lambda: staff.sort(key=lambda x: x.name),
        2: lambda: staff.sort(key=lambda x: -x.harm),
        3: lambda: staff.sort(key=lambda x: -x.protection),
        4: lambda: staff.sort(key=lambda x: -x.health),
        5: lambda: staff.sort(key=lambda x: -x.knowledge),
        6: lambda: staff.reverse()
     }
    action=d.get(el)
    if action:
        action()
    
def upgrade(el):  
    if staff[el].cat=='weapon' or staff[el].cat=='protection' or staff[el].cat=="tool" and book in staff:
        d={
            axe: Saxe,
            hammer: Shammer,
            sword: Ssword,
            gun: Sgun,
            screen: Sscreen,
            armor: Sarmor
        }
        staff[el]=d.get(staff[el])
    else:
        print("Усилить можно только оружие или защиту, также нужно иметь книгу, чтобы знать, как это делается!")

def put():
    while none in case:
        for i in range(len(staff)):
            print(staff[i].name)
        k=int(input("Выберите элемент, который хотите положить в сундук. Если закончили - нажмите 0"))-1
        if k==-1:
            return
        else:
            case.append(staff.pop(k))
            case.remove(none)
            continue
    if not none in case:
        print("Нет места!")
        return 





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
                if len(staff)==0:
                    print("В инвентаре пока пусто...")
                    exit=input("Нажмите любую клавишу для выхода")
                    break
                print("")
                print("1 - Выбросить ненужное")
                print("2 - узнать характеристики")
                print("3 - навести порядок")
                print("4 - найти элемент")
                print("5 - создать новый элемент, использовать существующий")
                print("6 - сохранить и выйти")
                print("7 - выйти без сохранения")
                print("8 - Улучшить элемент")
                d=int(input("Что вы хотите сделать?"))
                if d==7:
                    exit_without_save()
                elif d==6:
                    break
                elif d==4:
                    el=input("Что хотите найти?")
                    finder(el)

                elif d==8:
                    el=int(input("Номер элемента, который хотите улучшить: "))-1
                    upgrade(el);
                
                elif d==5:

                    print("Создавать новые элементы можно только обладая очками знаний (kp) >=50")
                    d=int(input("1- создать элемент, 0 - использовать существующий"))
                    if d==1 and kp>=50:
                        maker()
                    elif d==1 and kp<50:
                        print("вы пока не можете создавать предметы")
                    else:
                        el=int(input("Введите номер предмета: "))-1
                        using(el)
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
                    print("6 - обратный порядок")
                    
                    el=int(input("По чему хотели бы сортировать?"))

                    sorting(el)


                    
                    
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
    
 

    if true_l[x][y]==1:
        print("Тут пусто...")
        continue


    elif true_l[x][y]==4:
        print("Неужели, Вы нашли Ключ!")
        d=input("Нажмите 1 - чтобы забрать")
        if d=='1':
            true_l[x][y]=1
            if len(staff)<size and not key in staff:
                staff.append(key)
            elif len(staff)>=size:
                print("В рюкзаке не хватает места!")
            elif key in staff:
                print("У Вас уже есть ключ!")
        continue
          
    elif true_l[x][y]==6:
        '''Команата с выходом. Конец игры''' 
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
        d=input("1 - выбрать оружие и защиту, любая другая клавиша - сразиться с монстром в кулачном бою")


        t1=-1
        t2=-1
        '''Выбираем предметы из инвентаря для усиления'''
        if d=="1":
            print("Предмет   Урон   Защита")
            for i in staff:
                print(i.name, i.harm, i.protection)
            t1=int(input("Введите номер предмета "))-1
            if t1>len(staff)-1:
                t1=-1
                print("Некорректный номер предмета! Придется отбиваться от монстра без защиты!")
            else:
                d=input("1 - для выбора еще одного предмета")
                if d=='1':
                    t2=int(input("Введите номер предмета "))-1
                    if t2>len(staff)-1:
                        t2=-1
                        print("Некорректный номер! Придется отбиваться от монстра только одним предметом!")
                    elif t1==t2:
                        print("Этот предмет уже был выбран!")
            

        '''Расчет урона от монстра и силы атаки на него'''
        if t1==-1 and t2==-1:
            uron=monstr
            attack=0
        elif t1>-1 and t2==-1:
            attack=staff[t1].harm
            uron=monstr-staff[t1].protection
        else:
            attack=staff[t1].harm + staff[t2].harm
            uron=monstr-staff[t1].protection-staff[t2].protection

        if uron<=0:
            print("Вы победили монстра!")
            true_l[x][y]=1
            continue
           
        elif uron <= attack:
            print("Вы смогли защититься от монстра. Он испугался и больше вас не побеспокоит")
            true_l[x][y]=1
        elif hp+attack-uron>0:
            print("Вы смогли сбежать от монстра. Но он может отомстить...")
            hp=hp+attack-uron
        else:
            print("Вы погибли в неравной схватке с монстром... Жаль, но игра окончена")
            break
    elif true_l[x][y]==2:
        print("Здесь сундук!")
        print("1- посмотреть содержимое")
        print("Любая другая клавиша - пойти дальше")
        d1=input()
        if d1=="1":
            case_is_open=False
            for i in open_cases:
                if i[0]==x and i[1]==y:
                    case=i[2]
                    case_is_open=True
            if not case_is_open:
                case=[ts[int(random.random()*18)] for i in range(5)]
                open_cases.append([x, y, case])
            
            while True:
                for i in range(5):
                    print(case[i].name)
                d=int(input("Выберите номер вещи, которую хотите забрать. Нажмите 0 для выхода, -1 чтобы забрать все, -2 - чтобы положить что-то в сундук"))-1
                if d==-1:
                    for i in open_cases:
                        if i[0]==x and i[1]==y:
                            i[2]=case
                    break
                elif d==-3:
                    put();
                        
                elif d==-2:
                    case=[i for i in case if i!=none]
                    if len(staff)+len(case)<=size:
                        staff.extend(case)
                        case=[none for i in range(5)]
                        
                else:
                    if len(staff)<size and case[d]!=none:
                        staff.append(case.pop(d))
                        case.append(none)
                    elif len(staff)>=size:
                        print("Не хватает места в рюкзаке!")
                        continue
                    else:
                        print("Вы не можете забрать пустоту из сундука")
                        continue
        else:
            continue