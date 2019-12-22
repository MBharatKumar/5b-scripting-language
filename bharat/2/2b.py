import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st_df = pd.read_csv("StudentsPerformance.csv")

print("________data header__________")
st_df.head()

print("________discription_________")
st_df.info()
st_df.describe()

print("removing lunch and test preparation course")
st_df1 = st_df.drop(['lunch','test preparation course'],axis=1)
st_df1.head()

print("filling the empty values in parental level of education")
st_df1["parental level of education"] = st_df["parental level of education"].fillna("highSchool")
print(st_df1["parental level of education"])

ax = sns.countplot(x="test preparation course", hue="gender", palette="Set1", data=st_df)
ax.set(title="test prepration", xlabel="course", ylabel="total")
plt.show()
