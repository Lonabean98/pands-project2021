#with open('iris.data', 'r') as f:
    #data=f.read()
    #print(data)

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv("iris.data")  
df.columns = ["sepal length", "sepal width", "petal length", "petal width", "variety"]

#head() command shows first x number of lines. Specify number in bracket  
print(df.head(10))  


summary = df.describe(include="all")  
summaryt = summary.transpose()  
print("")
print("Summary Statistics")
print(summaryt)

#plt.hist(df.columns[1])
#plt.show()