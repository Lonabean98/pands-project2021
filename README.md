# pands-project2021

#The dataset
This project consists in analysing the Fisher’ Iris data set. The data set consists of 50 samples from each of three species of Iris. The set contains the length and width measurements for sepals and petals of the Iris setosa, Iris virginica, Iris versicolor. The columns of the data set correspond to sepal length, sepal width, petal length, petal width and species. The data set was created by Sir Ronald Aylmer Fisher in 1936. It has been used extensively, including most recently for statistical classification techniques in machine learning. (Iris flower data set- Wikipedia, n.d.) 
The three species of Iris included in the dataset:

![image](https://user-images.githubusercontent.com/77697552/114313273-d23be780-9aed-11eb-82b0-a5d400bdcbf3.png)

 
The variables in the dataset:

 ![image](https://user-images.githubusercontent.com/77697552/114313277-d7009b80-9aed-11eb-8c94-7ea0800b4686.png)

Irises have three sepals, which are usually spreading or droop downwards, also referred to as "falls". The three, sometimes reduced, petals stand upright, partly behind the sepal bases. They are called "standards". (Iris (plant)- Wikipedia, n.d.) Unlike most other flowers, the most “showy” part of the Iris is actually the sepal, not the petal. 

## Modules used to analyse the dataset
The first step consists in importing the Python modules that are used to analyse the dataset: Pandas, matplotlib.pyplot, numpy, random, seaborn, matplotlib.patches

Explanation of Code to import the modules:

![image](https://user-images.githubusercontent.com/77697552/114313291-e8e23e80-9aed-11eb-973b-d084c48d5c19.png)



 
Pandas: A data analysis and manipulation tool built using the Python programming language.

Matplotlib.pyplot: Matplotlib is a library for data visualisation. Pyplot is an interface which provides a MATPLOT-like way of plotting. (matplotlib.pyplot, n.d.)

Numpy: brings the computational power of languages like C to Python, which is easier to use. (Numpy, n.d.)

Random: Implements pseudo-random number generators. 

Seaborn: Statistical data visualisation library based on matplotlib. (seaborn: statistical data visualization, n.d.)

Matplotlib.patches: A patch is a 2D artist with a face color and an edge color. (matplotlib.patches.Patch- Matplotlib.org, n.d.)

## Reading the dataset

The data is read into a csv file using the following code. (pandas.read_csv, n.d.)

![image](https://user-images.githubusercontent.com/77697552/114313303-f39cd380-9aed-11eb-89da-894b587eb6d4.png)

 
Each column of the data file is then labelled. (pandas.DataFrame.columns, n.d.)

![image](https://user-images.githubusercontent.com/77697552/114313308-f7c8f100-9aed-11eb-940f-65b19205592d.png)

 
A random sample of data for 10 flowers is printed to the terminal.

![image](https://user-images.githubusercontent.com/77697552/114313314-fdbed200-9aed-11eb-970c-57e7499cf120.png)


## Making the summary and writing to a text file

A summary of the 4 variables being analysed is written to a text file using the following code. (Python | Pandas Dataframe.describe() method, n.d.)

![image](https://user-images.githubusercontent.com/77697552/114313323-04e5e000-9aee-11eb-9668-7fd8c46d073f.png)

 

Summary: 

![image](https://user-images.githubusercontent.com/77697552/114313334-09aa9400-9aee-11eb-97f8-427fd0fe487d.png)

 

Analysis of the summary:
Petal width: From this summary, it is apparent that on average, the petal width of the 3 variants is the smallest variable. On average, the sepal length is the largest variable. The virginica species has the highest average sepal length of any species, but also has the highest standard deviation. 

Sepal length: The virginica sample contains the highest sepal length value (7.9 cm) and also has the highest average sepal length (6.588). The setosa sample contains the lowest value (4.3 cm) and the lowest average (5 cm). However, setosas have the lowest standard deviation for sepal length, which means that there is very little variation. 

Sepal Width: The setosa sample contains the highest value for sepal width (4.4 cm) as well as the highest average (3.4 cm). Setosas also have the highest standard deviation for sepal width (0.38 cm) but not by a large margin. On average, Versicolors have the thinnest sepals. 

Petal Length: Virginicas on average have the longest petal length, but also the highest standard deviation. This means that there is a lot of variation in petal length in this species. On average, setosas have the shortest petals. 

Petal Width: Setosas also have the shortest petals on average. 

## Histograms

Histograms of each variables are created and saved to .png files using the following code. The colours for each plot are hard-coded (primary colours were selected)

![image](https://user-images.githubusercontent.com/77697552/114313343-116a3880-9aee-11eb-83f2-da08584f820d.png)

 

Histograms:

![image](https://user-images.githubusercontent.com/77697552/114313353-162eec80-9aee-11eb-9886-96b8005965ca.png)
![image](https://user-images.githubusercontent.com/77697552/114313357-1a5b0a00-9aee-11eb-965d-d4fdc6cd835f.png)
![image](https://user-images.githubusercontent.com/77697552/114313363-1f1fbe00-9aee-11eb-8182-6d1f43d5a872.png)
![image](https://user-images.githubusercontent.com/77697552/114313374-26df6280-9aee-11eb-9d1d-779bd4f73d8a.png)


 

 

 
The histograms for petal length and petal width show two peaks, which indicates two groups of Irises with very different petal sizes. The sepal length and width show a more normal distribution (a bell-type curve). 

Pairplots

A pairplot is created using the following code. Each of the three species of irises is represented by a different colour. The code automatically selects the different colours for the different species and plots a legend of the meaning of the colours. 

![image](https://user-images.githubusercontent.com/77697552/114313382-2d6dda00-9aee-11eb-9f80-0e680b47d98f.png)

 
## Pairplots:

![image](https://user-images.githubusercontent.com/77697552/114313383-3199f780-9aee-11eb-8985-c3f752ab567b.png)


 
There are 16 plots, plotting all four variables against each other. The plots below the NW-SE diagonal are the mirror images of the plots below the diagonal, across the y=x diagonal. There are only 6 unique combinations of each of the 4 variables. We can see from this pair plot that generally, the setosa species is linearly separable from the other two. 

The plots along the NW-SE diagonal are not scatter plots but the distribution of the data in question. These distribution plots give more information than the overall histograms presented above, allowing to refine the analysis per species. The analysis of these distribution plots confirms the hypothesis above: the different peaks in the overall histogram corresponds to different species. The petal length and petal width show a very distinct peak of lowest petal size for a species of Iris. This is the setosa species. The distributions for the other two species overlap somewhat, virginica being slightly larger than versicolor. The overlap is more important for the sepal variable, indicating that there is not much difference in sepal size (this variable may not matter as much to the breeders).

## Individual scatter plots 

![image](https://user-images.githubusercontent.com/77697552/114313389-378fd880-9aee-11eb-9c94-abcc015bbc6a.png)


 
The code outputs a scatter plot of each pair of variables. Six scatter plots are created in turn. The colours of the species are hard-coded. There are six unique groups of 2 items out of a collection of 4 items (6 “combinations” in mathematics). 
In all of these scatter plots, we can see that setosa species is linearly separable to the other two. 

![image](https://user-images.githubusercontent.com/77697552/114313394-3eb6e680-9aee-11eb-8bdd-0f433f4271d4.png)

 
The above plot shows that the setosa species has sepals that are wide but not very long. They are the “roundest” sepals. The other two variaties have a roughly similar sepal width to length ratio. While the virginica and versicolor species are comparable, it seems that the sepals of virginica are slightly longer. 
There appears to be a linear correlation between these two variables for setosa only. There is no clear correlation for the other two species. 

![image](https://user-images.githubusercontent.com/77697552/114313402-44acc780-9aee-11eb-8730-b76a4c4633a1.png)



 
From the above plot, we can see that the sepals and petals of the setosa species are similar in length as there is not much spread within the group. We can also see that the sepals and petals of the setosa species are shorter in comparison to the other two variants. The virginica species has some of the longest sepals and petals as the data points extend almost to the top right of the plot. The versicolor species have average petal and sepal lengths. There appears to be a linear positive correlation between petal length and sepal length within each species. This means that a line can be drawn through the data “cloud”, with little variability on each part of the line. The slopes of the lines are different. Petal length is related to sepal length, the “biggest” flowers in each species having proportionately bigger sepals and petals. 

![image](https://user-images.githubusercontent.com/77697552/114313404-4a0a1200-9aee-11eb-86b8-b9e48811b678.png)

 
We can see that the setosa species has the lowest petal width- sepal length ratio of the 3. The setosa species also has very little variation in petal widths and sepal lengths. The virgincia species has some of the longest petal widths and sepal lengths. There is a lot of variation in the virgincia data as the points are very spread out.  The versicolor species is somewhere in between. There doesn’t appear to be any correlation between these variables within each species.

![image](https://user-images.githubusercontent.com/77697552/114313406-4e362f80-9aee-11eb-955c-e1e60c422fbd.png)


 
The setosa species has some of highest sepal widths compared to petal lengths. The sepal width of this species is much greater than the petal length. The other two species have similar ratios, again with the virginicas tending to be longer than the versicolors. As above there is little or no apparent correlation between these variables within each species. 
 
![image](https://user-images.githubusercontent.com/77697552/114313413-58582e00-9aee-11eb-9b33-26c0b56ac7eb.png)

Setosas have the narrowest petals and the widest sepals. There is a lot more variation in sepal width than in petal width, with no apparent correlation between the 2 variables. There seems to be a weak positive linear correlation for the two other species. 

![image](https://user-images.githubusercontent.com/77697552/114313422-60b06900-9aee-11eb-8ff5-c88d0d4ee967.png)


 
The setosa species have the shortest and thinnest petals. Virginica has the longest and widest petals. Versicolour has average petal width and length. There is a strong overall positive linear correlation for the entire dataset, and a weaker correlation among each dataset. There is not much overlap between the data “clouds”. The overall size of the petal (length and width) distinguishes clearly between the species. This plot could even be used as a criterion to determine the species if no other information about a flower was available such as its colour pattern and so on. In this graph we can see most clearly what distinguishes the species: a species with small petals, one with medium petals and one with large petals. 

## Discussion and conclusion

In conclusion, the setosa species seems to be the smallest in general for both sepal and petal size. Virginica and versicolor are not easily distinguishable by their individual sepal and petal size variables. 

Iris setosa is a dwarf species: it is a dwarf version of Iris sibirica (Wikipedia - Iris setosa). Referring back to the photos at the top of this readme file, one can see that setosa has a more compact, round flower shape. Its appearance is most different from the others. Its size and overall shape could help a non-botanist to identify this species. The compact shape of Iris setosa is probably an adaptation to the cold arctic environments to which it is native. This species is easy to identify using several of the individual variables measured in the dataset that do not overlap, for example petal length < 1.9 cm.
Referring back to the photos, the other two, virginica and versicolor, have relatively similar flower sizes, and slightly different petal and sepal shapes. They have different colour markings. Versicolor means "variously coloured". (Iris versicolor- Wikipedia, n.d.). Iris virginica and versicolor are both native to North America. (Iris virginica- Wikipedia, n.d.)

However, it is notoriously difficult to differentiate between Iris versicolor and Iris virginica as both have similar growth habits, floral colors, and bloom times. In fact, they are often sold interchangeably in the trade as blue flag iris. (Clemson Home and Garden Information Garden Centre, n.d.) As they are found in the same region of the world, they may have a close common ancestor. 

With data analysis and data visualization of the Fisher data set, is it possible to find quantitative indicators to distinguish not only setosa from the other two species, but also between virginica and versicolor? The data analysis and visualizations show that the range of many of their variables overlap. We can try to find a combination of variables that is discriminant and allows to identify the species with minimal possibility of error. A possibility could be the ratio (i.e. slope) between some of these variables.  The petal width vs. sepal width plots seems to show a good linear relationship and a different slope (ratio petal width/sepal width) for the 3 species. A further analysis would be required to determine the slope of the linear regressions. This ratio could be used in the field to identify the 3 species. Alternatively, machine learning could be used to find unique combination of these variables as a discriminating factor between the species. 

References
Clemson Home and Garden Information Garden Centre. (n.d.). Retrieved from https://hgic.clemson.edu/factsheet/rain-garden-plants-iris-versicolor-and-iris-virginica/

Cui, Y. (2020, April 25). The Iris Dataset — A Little Bit of History and Biology. Retrieved from towards data science: https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5

Hatterer, R. (2020, July 29). datasets.load_iris() in Python. Retrieved from Stackoverflow: https://stackoverflow.com/questions/43159754/datasets-load-iris-in-python

Iris (plant)- Wikipedia. (n.d.). Retrieved from https://en.wikipedia.org/wiki/Iris_(plant)

Iris flower data set- Wikipedia. (n.d.). Retrieved from https://en.wikipedia.org/wiki/Iris_flower_data_set

Iris versicolor- Wikipedia. (n.d.). Retrieved from https://en.wikipedia.org/wiki/Iris_versicolor

Iris virginica- Wikipedia. (n.d.). Retrieved from https://en.wikipedia.org/wiki/Iris_virginica

matplotlib.patches.Patch- Matplotlib.org. (n.d.). Retrieved from https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html

matplotlib.pyplot. (n.d.). Retrieved from matplotlib 3.4.1: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html

Numpy. (n.d.). Retrieved from Numpy.org: https://numpy.org/

pandas.DataFrame.columns. (n.d.). Retrieved from pandas.pydata.org: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html

pandas.read_csv. (n.d.). Retrieved from pandas.pydata.org: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html

Python | Pandas Dataframe.describe() method. (n.d.). Retrieved from geeksforgeeks.org: https://www.geeksforgeeks.org/python-pandas-dataframe-describe-method/#:~:text=Pandas%20describe()%20is%20used,shown%20in%20the%20examples%20below.

seaborn: statistical data visualization. (n.d.). Retrieved from seaborn.pydata.org: https://seaborn.pydata.org/

Wikipedia - Iris setosa. (n.d.). Retrieved from Wikipedia: https://en.wikipedia.org/wiki/Iris_setosa






