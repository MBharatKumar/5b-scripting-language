import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

irsds = pd.read_csv('iris.csv')
print("_____displaying header_____")
irsds.head()

print("_______displaying info and discription________")
irsds.info()
irsds.describe()

print("printing average petal width of each species")
print(irsds[['Class',' Petal_Width']].groupby(['Class'],as_index=True).mean())

ax=sns.countplot(x=" Petal_Width", hue="Class",data=irsds, palette="Set1")
ax.set(title="Categorization of flowers based on sepal width", xlabel="Categories",ylabel="Total")
plt.show()