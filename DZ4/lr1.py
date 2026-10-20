import pandas as pd
import numpy as np
with open('tested.csv'):
    '''6. загрузка данных в dataframe'''
    data=pd.read_csv('tested.csv')
    print(data)


'''Часть 2'''
print('7. первые n строк')
n=int(input('Количество строк: '))
print(data.head(n))
print(" ")

print('8. последние 5 строк')
print(data.tail(5))
print(" ")

print('9. кол-во строк и столбцов')
print("Строк: ", data.shape[0], ", стобцов: ", data.shape[1])
print(" ")

print('10. Названия столбцов')
print(data.columns.tolist())
print(" ")

print('11. Типы данных каждого столбца')
print(data.dtypes.tolist())
print(" ")

print('13. Расчет среднего, медианы, минимума, максимума, стандартного отклонения для числовых признаков')
for i in ["Age", "SibSp", "Parch", "Fare"]:
    print(i)
    print(f'Среднее {data[i].mean()}, медиана {data[i].median()}, минимум {data[i].min()}, максимум {data[i].max()}, стандартное отклонение {data[i].std()}')
print("")

print("14. Кол-во пассажиров каждого класса")
for i in set(data['Pclass']):
    print(i, len(data[data["Pclass"]==i]))
print("")

print("15. Количество уникальных значений Embarked")
print(data['Embarked'].nunique())
print('')


'''Часть 3'''

print('16. Количество пропусков')
for i in data.columns:
    print(i, data[i].isna().sum())
print('')

print('17. Процент пропусков')
for i in data.columns:
    print(i, round((data[i].isna().sum())/len(data[i])*100, 2))

print("18. Максимальное кол-во пропусков в столбце Cabin")

print('19. Age. Значение среднего, медианы, минимума, максимума, стандартного отклонения, количество известных значений')
age_mean=data["Age"].mean()
age_median=int(data["Age"].median())
age_min=data["Age"].min()
age_max=data["Age"].max()
age_std=data["Age"].std()
age_val=len(data["Age"])-(data["Age"].isna().sum())
print(age_mean, age_median, age_min, age_max, age_std, age_val)
print('')

print("20. Заменим пустые ячейки Age медианой")
data["Age"]=data['Age'].fillna(age_median)

print("20. Новые значения характеристик Age")
age_mean=data["Age"].mean()
age_median=data["Age"].median()
age_min=data["Age"].min()
age_max=data["Age"].max()
age_std=data["Age"].std()
age_val=len(data["Age"])-(data["Age"].isna().sum())
print(age_mean, age_median, age_min, age_max, age_std, age_val)

print("")


print("23. Embarked")
for i in range(len(data["Embarked"])):
    if data.iat[i, 11]=="NaN":
        data=data.drop[i]


print("24. Cabin")
a=data["Cabin"].isna().sum()/len(data["Cabin"])*100
print("Доля пропусков: ", a)
if a>50.0:
    data=data.drop(columns=["Cabin"])
    print("Столбец Cabin удален")


print("25. Проверим пропуски")
prop=0
for i in data.columns:
    print(i, data[i].isna().sum())
    prop+=data[i].isna().sum()
print(f'Всего {prop}')

print("26. Количество строк и столбцов после обработки")
print(len(data.columns), len(data))





'''Часть 4'''

print("31-32. Выжившие")
surv=data["Survived"].to_numpy()
print(f'Процент выживших - {round(np.mean(surv)*100, 2)} %')
surv_s=data[["Survived", "Sex"]].to_numpy()
sex=data["Sex"].to_numpy()

print("Процент выживших мужчин - ", round(np.mean(surv[sex=="male"])*100, 2))
print("Процент выживших женщин - ", round(np.mean(surv[sex=="female"])*100, 2))

print("33-34. Средний возраст")
age=data["Age"].to_numpy()
print("Средний возраст мужчин - ", round(np.mean(age[sex=="male"]), 2))
print("Средний возраст женщин - ", round(np.mean(age[sex=="female"]), 2))

if len(age[(sex=="male")&(surv==0)])>0: 
    print("Средний возраст погибших мужчин - ", round(np.nanmean(age[(sex=="male")&(surv==0)]), 2))
if len(age[(sex=="female")&(surv==0)])>0:
    print("Средний возраст погибших женщин - ", round(np.nanmean(age[(sex=="female")&(surv==0)]), 2))
if len(age[(sex=="male")&(surv==1)])>0:
    print("Средний возраст выживших мужчин - ", round(np.nanmean(age[(sex=="male")&(surv==1)]), 2))
if len(age[(sex=="female")&(surv==1)])>0:
    print("Средний возраст выживших женщин - ", round(np.nanmean(age[(sex=="female")&(surv==1)]), 2))

print("35. стоимость билета")
data["Fare"]=data["Fare"].replace(",", ".")
fare=pd.to_numeric(data["Fare"]).to_numpy()
print("Максимальная", np.nanmax(fare))
print("Минимальная", np.nanmin(fare))
print("Средняя", np.nanmean(fare))

print ("36. Возраст")
print("Стандартное отклонение", np.nanstd(age))




'''Часть 5'''
print("Фильтрация данных")
print("#1")
filtered_data=data[(data["Sex"]=="male") & (data["Age"]>30) & (data["Pclass"]==1)]
print(len(filtered_data))
print(filtered_data.head(10))

print("#2")
filtered_data=data[((data["Age"]<18)|(data["Sex"]=="female"))&(data["Survived"]==1)]
print(len(filtered_data))
print(filtered_data.head(10))

print("#3")
f_3=data[data["Pclass"]==3]
mean_f_3=f_3["Fare"].mean()
filtered_data=data[(data["Pclass"]==3)&(data["Fare"]>mean_f_3)]
print(len(filtered_data), mean_f_3)
print(filtered_data)

print("#4")
filtered_data=data[(data["Embarked"]=="S") & (data["Age"]>=20) & (data["Age"]<=40)]
print(len(filtered_data))
print(filtered_data)




'''Часть 6'''
print("Группировка и агрегирование")

print("#37")
newdata1=data.groupby(['Pclass', 'Sex'], as_index=False).agg({
    "PassengerId":"size",
    "Age": "mean",
    "Survived":"mean",
    "Fare":"mean"
})

newdata1.columns=["Pclass", "Sex", "Кол-во пассажиров", "Средний возраст", "Доля выживших (%)", "Средняя цена билета"]
newdata1["Доля выживших (%)"]=newdata1["Доля выживших (%)"]*100
print(newdata1)

print("#38")
newdata=data.groupby(['Embarked'])['PassengerId'].size()
print(newdata)
newdata=data.groupby(['Embarked'])['Survived'].mean()*100
print(newdata)

print("#39")
newdata=data.groupby(['Pclass'])["Survived"].mean()*100
print(newdata)
print("Наибольшая доля выживших в 1 классе")



'''Сохранение результатов в csv. Часть 7'''

data.to_csv('titanic_processed.csv')

newdata1.to_csv('titanic_statistics.csv')

with open('titanic_processed.csv'):
    test_1=pd.read_csv('titanic_processed.csv')
    print(test_1)
with open('titanic_statistics.csv'):
    test_2=pd.read_csv('titanic_statistics.csv')
    print(test_2)