'''
This is a summary of Matplotlib.
I summarized the following video: https://www.youtube.com/watch?v=WGJJIrtnfpk&list=PL9ooVrP1hQOHY-BeYrKHDrHKphsJOyRyu
time stapes: 8:28:18 - 9:02:43
I did this for my myselfe so I can always go back and remember what I have learned.
I encourage everyone to go watch the video, like, subscribe, and show them love in the comment section!
'''
###############################################
print("Matplotlib is a Python package used for 2D graphics")
print("## The Type of Plots:"
      "1. Bar graph"
      "2. Histograms"
      "3. Scatter Plot"
      "4. Pie Plot"
      "5. Hexagonal Bin Plot"
      "6. Area Plot")
###############################################
from matplotlib import pyplot as plt
###############################################
print("## Simple Graph: ##")
print("Here's some basic code to generate one of the most simple graph:")
plt.plot([1,2,3],[4,5,1])
plt.show()
print("Right now there are no tags, nor X and Y labels, nor a title."
      "Also, we will not be writing the data like that, rather we will pass"
      "it as a variable")
x = [5,8,10]
y = [12,16,6]
plt.plot(x,y,'m')
plt.title("Info")
plt.ylabel("Y axis")
plt.xlabel("X axis")
plt.show()
###############################################
print("## Adding Style To Our Graph: ##")
from matplotlib import style
style.use("ggplot") # the type of plot we want to use
x = [5, 8, 10]
y = [12, 16, 6]
x2 = [6, 9, 11]
y2 = [6, 15, 7]

plt.plot(x,y,'m',label = 'line one', linewidth =5)
plt.plot(x2,y2,'c',label = 'line two', linewidth =5)
plt.title("Epic Info")
plt.ylabel("Y axis")
plt.xlabel("X axis")
plt.legend()
plt.grid(True, color ='k')
plt.show()
###############################################
print("## Bar graph: ##")
print("Bar graphs are used to compare things between different groups")
plt.bar([2,4,6,8,10],[8,6,2,5,6], label = "Example two", color ='m')
plt.legend()
plt.xlabel("bar number")
plt.ylabel("bar height")
plt.title("Bar Graph")
plt.show()
###############################################
print("## Histograms: ##")
population_ages = [22,55,62,45,21,22,34,42,4,99,102,
                   110,120,121,122,130,111,115,112,80,75,
                   65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population_ages, bins, histtype='bar',rwidth=0.8, color='m')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Histogram")
plt.legend()
plt.show()
###############################################
print("The difference between bar graph and a histogram:")
print("Meaning: "
      "     Histogram refers to a graphical representation, that displays data by way of bars to show the frequency of numerical data."
      "     Bar graph is a pictorial representation of data that uses bars to compare different categories of data."
      "Indicates:"
      "     Histogram- Distribution of non-discrete variables"
      "     Bar graph- Comparison of discrete variables"
      "Presents:"
      "     Histogram- Quantitative data	"
      "     Bar graph- Categorical data"
      "Spaces:"
      "     Histogram- Bars touch each other, hence there are no spaces between bars	"
      "     Bar graph- Bars do not touch each other, hence there are spaces between bars."
      "Elements:"
      "     Histogram- Elements are grouped together, so that they are considered as ranges.	"
      "     Bar graph- Elements are taken as individual entities."
      "Can bars be reordered?"
      "     Histogram- No"
      "     Bar graph- Yes"
      "Width of bars:"
      "     Histogram- Need not to be the same"
      "     Bar graph- Same")
###############################################
print("## Scatter Plot: ##")
print("we use scatter plot in order to compare between 2 or"
      " 3 things- 3D, to find a corolation ")
x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]
plt.scatter(x,y, label='YaelScat', color='m')
plt.xlabel("X")
plt.ylabel("Y")
plt.title('Scatter')
plt.legend()
plt.show()
###############################################
print("## Stack Plot: ##")
days = [1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

plt.plot([],[],color='r',label='Sleeping', linewidth=5)
plt.plot([],[],color='m',label='Eating', linewidth=5)
plt.plot([],[],color='y',label='Working', linewidth=5)
plt.plot([],[],color='c',label='Playing', linewidth=5)
plt.stackplot(days,sleeping,eating,working,playing,colors=['r','m','y','c'])
plt.xlabel('x')
plt.ylabel('y')
plt.title("Stack Plot")
plt.legend()
plt.show()
###############################################
print("## Pie Plot: ##")
###############################################
print("## Hexagonal Bin Plot: ##")
###############################################
print("## Area Plot: ##")
###############################################
###############################################
###############################################
###############################################
###############################################
########%%%%%%%%%#########%%%%%%%%
########%%%%%%%%%#########%%%%%%%%
########%%%%%%%%%#########%%%%%%%%
########%%%%%%%%%#########%%%%%%%%
########%%%%%%%%%#########%%%%%%%%
#%#%#%#%#%#%#%#%#%#%#
#%#%#%#%#%#%#%#%#%#%#
#%#%#%#%#%#%#%#%#%#%#
#%#%#%#%#%#%#%#%#%#%#
#%#%#%#%#%#%#%#%#%#%#
#%#%#%#%#%#%#%#%#%#%#