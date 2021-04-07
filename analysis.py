import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns


df = pd.read_csv("iris.data")  
# reads a comma-separated values (csv) file into DataFrame as 'df'
#Reference: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.htm

df.columns = ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)", "Variety"]

setosa = df[df['Variety'] == 'Iris-setosa']
versicolor = df[df['Variety'] == 'Iris-versicolor']
virginica = df[df['Variety'] == 'Iris-virginica']

print(df.sample(10))  
#prints data from random sample of 10 flowers


def readData(x,y):
    #function that reads the data and prints a sumamry of the variables.
    summary= x.describe()
    summaryt= summary.transpose()
    print(y)
    print('=========')
    print(summaryt)
    print('=========')
    with open('Summary.txt', 'w') as f:
        f.write(str(summaryt))



readData(setosa,'Setosa Summary')
readData(virginica, 'Virginica Summary')
readData(versicolor, 'Versicolor Summary')




def plothist(x, y):
    #This function takes in a column name and colour and uses 
    # this to plot the histogram
    plt.hist(df[x], color =y, ec="black")
    #plot histogram using x and y variables
    plt.title(x)
    substring= "Width"
    if substring in x:
        plt.xlabel("Width in cm")
    else:
        plt.xlabel("Length in cm")
    #If the x value contains the string "Width", it will name the x axis "Width in cm"
    #if not, it will name the x axis "Lenght in cm"
    plt.ylabel("Frequency")
    plt.savefig(x +".png")
    plt.clf()
    #plt.show()

# plotting the histograms for each variable with different colours.
plothist("Sepal Length (cm)", "red")
plothist("Sepal Width (cm)", "blue")
plothist("Petal Length (cm)", "green")
plothist("Petal Width (cm)", "yellow")
      


def scatter(x,y, z):
    #function that generates a scatter plot for both Sepal variables.
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(x+ " vs "+ y)
    plt.scatter(df[x],df[y], c=z)
    plt.show()
    
    
scatter("Sepal Length (cm)", "Sepal Width (cm)", 'r')
#scatter("Sepal Length (cm)", "Petal Length (cm)", 'b')
#scatter("Sepal Length (cm)", "Petal Width (cm)", 'g')
#scatter("Sepal Width (cm)", "Petal Length (cm)", 'y')
#scatter("Sepal Width (cm)","Petal Width (cm)", 'purple' )
#scatter("Petal Width (cm)", "Petal Length (cm)" , 'cyan')

