import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

titdf = pd.read_csv("titanictrain.csv")
print("_______displaying header__________")
titdf.head()

print("_______displaying data set discription_________")
titdf.info()
titdf.describe()

print("_______droping unwanted columns_____")
titdf1 = titdf.drop(['PassengerId','Name','Ticket'],axis=1)
titdf1.head()

print("_____manuplating database______")
titdf["Embarked"] = titdf["Embarked"].fillna("s")
print(titdf["Embarked"])

ax = sns.countplot(x='Pclass', hue='Survived', palette='Set1', data=titdf)
ax.set(title = 'passenger status survived or dead', xlabel = 'Passenger class', ylabel = 'total')
plt.show()