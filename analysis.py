import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import random

# reads a comma-separated values (csv) file into DataFrame as 'df'
#Reference: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
df = pd.read_csv("iris.data")  

df.columns = ["sepal length", "sepal width", "petal length", "petal width", "variety"]

#prints data from random sample of 10 flowers
print(df.sample(10))  

#function that reads the data and prints a sumamry of the variables.
def readData():
    #df.describe() generates descriptive statistics. 
    #Reference: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
    summary = df.describe()
    #transpose index and columns
    #  Reference: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transpose.html
    summary2 = summary.transpose()  
    print("")
    print("Summary Statistics")
    print(summary2)
    # write the transposed summary into a .txt file called 'Summary'.
    with open('Summary.txt', 'w') as f:
        f.write(str(summary2))
readData()



#This function takes in a column name and colour and uses 
# this to plot the histogram
def plothist(x, y):
    plt.hist(df[x], color =y, ec="black")
    plt.title(x)
    plt.xlabel("lenght in cm")
    plt.ylabel("Frequency")
    plt.savefig(x +".png")
    plt.clf()
    #plt.show()

# plotting the histograms for each variable with different colours.
plothist("sepal length", "red")
plothist("sepal width", "blue")
plothist("petal length", "green")
plothist("petal width", "yellow")
      
# function that generates a scatter plot for both Sepal variables.
def scatterSepal():
    x=df["sepal length"]
    y=df["sepal width"]
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Sepal Width (cm)")
    plt.title("Sepal Width vs Sepal Length")
    plt.scatter(x,y)
    plt.show()
scatterSepal()

# function that generates a scatter plot for both Petal variables.
def scatterPetal():
    x=df["petal length"]
    y=df["petal width"]
    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Petal Width (cm)")
    plt.title("Petal Width vs Petal Length")
    plt.scatter(x,y, color= "red")
    plt.show()
scatterPetal()