import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

bfds = pd.read_csv("BlackFriday.csv")

print("________displaying header________")
bfds.head()

print("_______displaying info and discription________")
bfds.info()
bfds.describe()

print("filling default values in city catogary")
bfds["City_Category"] = bfds["City_Category"].fillna("B")
print(bfds["City_Category"])

print("maping City_Catogery")
bfds["City_Category"] = bfds["City_Category"].map({
    "A":"metro cities",
    "B":"small towns",
    "C":"villages"
})
print(bfds["City_Category"])

ax = sns.countplot(x="City_Category", hue="Gender", palette="Set1", data=bfds)
ax.set(title="city catogery", xlabel="catogery", ylabel="total")
plt.show()

