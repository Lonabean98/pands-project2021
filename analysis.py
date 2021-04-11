import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
import matplotlib.patches as mpatches

# reads a comma-separated values (csv) file into DataFrame as 'df'
df = pd.read_csv("iris.data")  

#labels the columns of the data frame. Reference: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html
df.columns = ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)", "Variety"]

#Assigning variable names to the different flowers within the variety column
setosa = df[df['Variety'] == 'Iris-setosa']
versicolor = df[df['Variety'] == 'Iris-versicolor']
virginica = df[df['Variety'] == 'Iris-virginica']

#prints data from random sample of 10 flowers
print(df.sample(10))  

#function that reads the data and prints a summary of the variables.
def readData(x):
    # .describe() is used to view basic statistical details like percentile, mean, std etc. of the data frame. 
    # Reference: https://www.geeksforgeeks.org/python-pandas-dataframe-describe-method/#:~:text=Pandas%20describe()%20is%20used,shown%20in%20the%20examples%20below.
    summary= x.describe()
    #.transpose() writes rows as columns and vice-versa. 
    # Reference: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transpose.html
    summarytrans= summary.transpose()
    return summarytrans
    
#Calling the readData function with the different varieties as inputs. 
# I am giving the output of these calls variable names to be used later to write to summary file.
sum1=readData(setosa)
sum2=readData(virginica)
sum3=readData(versicolor)

#writing the summary to a text file 
with open('Summary.txt', 'w') as f:
    def writesummary(x,y):
        f.write(y)
        f.write('\n')
        f.write(str(x))
        f.write('\n')
        f.write('\n')
        #The outputs of the readData function are written to a text file, with heading to differentiate the different varieties.
    writesummary(sum1, 'Setosa Summary:')
    writesummary(sum2, 'Virginica Summary:')
    writesummary(sum3, 'Versicolor Summary:')
    
    
    
            
           
# This function creates a pairplot using seaborn. 
def pairplot():
    sns.pairplot(df, hue='Variety')
    plt.savefig('pairplot.png')
    plt.show()
    plt.close()
pairplot()


# This function takes in a column name and colour and uses 
# this to plot the histogram
def plothist(x, y):
    #plot histogram using x and y variables
    plt.hist(df[x], color =y, ec="black")
    plt.title(x)
    #If the x value contains the string "Width", it will name the x axis "Width in cm"
    #if not, it will name the x axis "Lenght in cm"
    substring= "Width"
    if substring in x:
        plt.xlabel("Width in cm")
    else:
        plt.xlabel("Length in cm")
    plt.ylabel("Frequency")
    plt.savefig(x +".png")
    plt.clf()
    

# plotting the histograms for each variable with different colours.
plothist("Sepal Length (cm)", "red")
plothist("Sepal Width (cm)", "blue")
plothist("Petal Length (cm)", "green")
plothist("Petal Width (cm)", "yellow")
      


def scatter(x,y):
    #function that generates a scatter plot for both Sepal variables.
    plt.xlabel(x)
    plt.ylabel(y)
    # Mapping each variable to a colour using a dictionary. 
    colormap= {'Iris-setosa': 'red', 'Iris-virginica': 'blue', 'Iris-versicolor': 'green'}
    # the colours of the data points will come from the colormap dict. 
    colors = [colormap[x] for x in df['Variety']]
    plt.title(x+ " vs "+ y)
    #Used mpatches.patch to manually add the legend. 
    # Reference: https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html
    red_patch = mpatches.Patch(color='red', label='Iris-setosa')
    blue_patch = mpatches.Patch(color='blue', label='Iris-virginica')
    green_patch = mpatches.Patch(color='green', label='Iris-versicolor')
    plt.legend(handles=[red_patch, blue_patch, green_patch])
    plt.scatter(df[x],df[y], c=colors)
    plt.show()
    
#calling scatter() function with arguments
scatter("Sepal Length (cm)", "Sepal Width (cm)")
scatter("Sepal Length (cm)", "Petal Length (cm)")
scatter("Sepal Length (cm)", "Petal Width (cm)")
scatter("Sepal Width (cm)", "Petal Length (cm)")
scatter("Sepal Width (cm)","Petal Width (cm)" )
scatter("Petal Width (cm)", "Petal Length (cm)")



