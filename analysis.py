import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import random

df = pd.read_csv("iris.data")  
df.columns = ["sepal length", "sepal width", "petal length", "petal width", "variety"]

#prints data from random sample of 10 flowers
print(df.sample(10))  

summary = df.describe(include="all")  
summaryt = summary.transpose()  
print("")
print("Summary Statistics")
print(summaryt)


#This function takes in a column name and colour and uses 
# this to plot the histogram
def plothist(x, y):
    plt.hist(df[x], color =y)
    plt.title(x)
    plt.xlabel("lenght in cm")
    plt.ylabel("Frequency")
    #plt.savefig(x +".png")
    #plt.clf()
    #plt.show()


#for columnname in df.columns:
   # colours=["Red", "Yellow", "Blue", "Green"]
    #if columnname != "variety":
        #for colour in colours:
            #plothist(columnname, colour)
      
#plothist('sepal length', "red")
#plothist('sepal width', "yellow")
#plothist("petal length", "blue")
#plothist("petal width", "green")

#def plotscatter(x,y):
   # plt.scatter(df[x,y])
    #plt.show()

def scatterSepal():
    x=df["sepal length"]
    y=df["sepal width"]
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Sepal Width (cm)")
    plt.title("Sepal Width vs Sepal Lenght")
    plt.scatter(x,y)
    plt.show()
scatterSepal()

def scatterPetal():
    x=df["petal length"]
    y=df["petal width"]
    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Petal Width (cm)")
    plt.title("Petal Width vs Petal Lenght")
    plt.scatter(x,y, color= "red")
    plt.show()
scatterPetal()