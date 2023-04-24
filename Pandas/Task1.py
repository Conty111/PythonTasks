"""
Из набора данных Titanic.csv выведите:
количество пассажиров,
средний возраст пассажира,
среднуюю стоимость билета,
максимальную и минимальную цену билета,
пассажира с максимальной ценой билета,
средний возраст мужчин и женщин по отдельности,
средний процент выживаемости мужчин и женщин,
среднюю стоимость билета в зависимости от класса проживания,
количество билетов по классам проживания,
количество выживших пассажиров
"""
import pandas as pd


dataframe = pd.read_csv("Pandas/Titanic.csv")
fare = dataframe["Fare"]

print(f"Count of passengers: {dataframe['PassengerId'].count()}")
print(f"Mean age of passengers: {dataframe['Age'].mean()}")
print(f"Mean cost of tickets: {fare.mean()}")
print(f"Most expensive ticket: {fare.max()}. Most cheap ticket: {fare.min()}")
print(f"Passenger with the most expensive ticket: {dataframe[fare==fare.max()]['Name']}\n")
print(f"Mean age of mens: {dataframe[dataframe['Sex']=='male']['Age'].mean()}")
print(f"Mean age of womans: {dataframe[dataframe['Sex']=='female']['Age'].mean()}")
print(f"Mean value of survived mans: {dataframe[dataframe['Sex']=='male']['Survived'].mean()}")
print(f"Mean value of survived womans: {dataframe[dataframe['Sex']=='female']['Survived'].mean()}")

for plane_class in set(dataframe["Pclass"].values):
    classes_now = dataframe["Pclass"] == plane_class
    print(f"Mean cost at class {plane_class}: {dataframe[classes_now]['Fare'].mean()}")
    print(f"Count of tickets at class {plane_class}: {dataframe[classes_now]['Ticket'].count()}")
print(f"Count of survived: {dataframe['Survived'].count()}")
