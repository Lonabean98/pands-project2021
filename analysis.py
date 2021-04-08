import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
import matplotlib.patches as mpatches


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
    return summaryt
    

sum1=readData(setosa,'Setosa Summary')
sum2=readData(virginica, 'Virginica Summary')
sum3=readData(versicolor, 'Versicolor Summary')

with open('Summary.txt', 'w') as f:
    def writesummary(x,y):
        f.write(y)
        f.write('\n')
        f.write('=========')
        f.write(str(x))
        f.write('\n')
        f.write('\n')
    writesummary(sum1, 'Setosa Summary')
    writesummary(sum2, 'Virginica Summary')
    writesummary(sum3, 'Versicolor Summary')
    
    
    
            
           

#def pairplot():
#    sns.pairplot(df, hue='Variety')
#    plt.savefig('pairplot.png')
#    plt.show()
#    plt.close()
#pairplot()

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
      


def scatter(x,y):
    #function that generates a scatter plot for both Sepal variables.
    plt.xlabel(x)
    plt.ylabel(y)
    colormap= {'Iris-setosa': 'red', 'Iris-virginica': 'blue', 'Iris-versicolor': 'green'}
    colors = [colormap[x] for x in df['Variety']]
    plt.title(x+ " vs "+ y)
    red_patch = mpatches.Patch(color='red', label='Iris-setosa')
    blue_patch = mpatches.Patch(color='blue', label='Iris-virginica')
    green_patch = mpatches.Patch(color='green', label='Iris-versicolor')
    plt.legend(handles=[red_patch, blue_patch, green_patch])
    plt.scatter(df[x],df[y], c=colors)
    plt.show()
    
    
scatter("Sepal Length (cm)", "Sepal Width (cm)")
#scatter("Sepal Length (cm)", "Petal Length (cm)")
#scatter("Sepal Length (cm)", "Petal Width (cm)")
#scatter("Sepal Width (cm)", "Petal Length (cm)")
#scatter("Sepal Width (cm)","Petal Width (cm)" )
#scatter("Petal Width (cm)", "Petal Length (cm)")


