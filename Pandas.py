'''
This is a summary of Pandas.
I summarized the following video: https://www.youtube.com/watch?v=WGJJIrtnfpk&list=PL9ooVrP1hQOHY-BeYrKHDrHKphsJOyRyu
time stapes: 8:28:18 - 9:02:43
I did this for my myselfe so I can always go back and remember what I have learned.
I encourage everyone to go watch the video, like, subscribe, and show them love in the comment section!
'''

###############################################
text = "## Python Applications ## \n " \
       "1. Web Scraping \n " \
       "2. Web Development \n " \
       "3. Testing \n " \
       "4. Data Analysis"

print(text)

###############################################
print("\n ## Data Life Cycle ##")
text = "Data can be store in different formats: CSV, Excel, HTML.\n" \
       "We can convert this data into a single format and store it somewhere\n" \
       "That is where data warehousing comes in the picture.\n" \
       "Storing your data allows us to then to analyze, we can use different analysis, like:" \
       "after analyzing the data we can then even plot it and use data visualization.\n"
print(text)


################################################
## What is Pandas? - Numpy, Scipy ##
print("\n ## What is Pandas? - Numpy, Scipy ##")
text = "Pandas is a software library written for" \
       "Python programming language, for data manipulation and analysis." \
       "Pandas is well suited for many different kinds of data\n" \
       "* Tabular data with heterogeneously-typed columns\n" \
       "* Ordered and unordered time series data.\n" \
       "* Arbitrary matrix data with row and column labels." \
       "* Any other form of observational / statistical data sets." \
       "The data actually need not to be laeled at all to be placed " \
       "into a pandas data structure"
print(text)

################################################
## Pandas Operations ##
print("\n \n ## Pandas Operations: ##")
import pandas as pd
XYZ_web = {'Day': [1, 2, 3, 4, 5, 6], "Visitors": [1000, 700, 6000, 1000,400,350], 'Bounce_Rate': [20, 20, 23, 15, 10, 34]}
df = pd.DataFrame(XYZ_web) # how to make a data frame using Pandas
print("printing the data will look like this: ")
print(df)
########%%%%%%%%%#########%%%%%%%%
print("\n ## Slicing the DataFrame:")
XYZ_web = {'Day': [1, 2, 3, 4, 5, 6], "Visitors": [1000, 700, 6000, 1000,400,350], 'Bounce_Rate': [20, 20, 23, 15, 10, 34]}
df = pd.DataFrame(XYZ_web) # how to make a data frame using Pandas
print("Slicing the head of the data frame (the first rows)")
print(df.head(2)) # will print the 2 first rows
print("Slicing the tail of the data frame (the last rows)")
print(df.tail(2)) # will print the 2 last rows
########%%%%%%%%%#########%%%%%%%%
print("\n ##Joining and Merging:")
print(" start with the merging first:")
df1 = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int_rate": [2, 1, 2, 3], "IND_GDP": [50, 45, 45, 67]},
                   index=[2001, 2002, 2003, 2004])
df2 = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int_rate": [2, 1, 2, 3], "IND_GDP": [50, 45, 45, 67]},
                   index=[2005, 2006, 2007, 2008])
print("Merging two data frames in to one:")
merge = pd.merge(df1, df2)
print(merge)
print("This is how we can specify one (or more) column to be merged both for x and y, when we merge:")
merge = pd.merge(df1, df2, on = "HPI") # the merged column will be HPI
print(merge)
#%#%#%#%#%#%#%#%#%#%#
print("\n Now Let's move on to the Joining:")
text = "The 2 data frames are joined at the base of there index value"
print("\n", text)
df1 = pd.DataFrame({"Int_rate": [2, 1, 2, 3], "IND_GDP": [50, 45, 45, 67]},
                   index=[2001, 2002, 2003, 2004])
df2 = pd.DataFrame({"Low_Tier_HPI": [50, 45, 67, 34], "Unemployment": [1, 3, 5, 6]},
                   index=[2005, 2006, 2007, 2008])
print("This is how you joine:")
joined = df1.join(df2) # there will be a row for every index. all the columns will appear
#if an index does not have a value for a certain column a NaN will be stored instead
print(joined)
########%%%%%%%%%#########%%%%%%%%
print("\n ## Changing the Index:")
df = pd.DataFrame({"Day": [1, 2, 3, 4], "visitors": [200, 100, 230, 300], "Bounce_Rate":[20, 45, 60, 10]})
print(df)
print("This is how you convert a column to be the index column:")
df.set_index("Day", inplace=True)
print(df)

print("\n Now lets plot it for fun by using the matplotlib library:")
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")
df.plot()
plt.show()
########%%%%%%%%%#########%%%%%%%%
print("\n Changing the column headers:")
df = pd.DataFrame({"Day": [1, 2, 3, 4], "visitors": [200, 100, 230, 300], "Bounce_Rate":[20, 45, 60, 10]})
print("before:\n", df)
df = df.rename(columns={"Visitors": "Users"}) # replace the header visitors with the header users
print("after:\n", df)

########%%%%%%%%%#########%%%%%%%%
print("\n ## Data conversion:")
print("also refers as data munging, basically convert a paricular"
      "format data into a different data format ")
country = pd.read_csv('C:\\Users\\Yael\\Downloads\\world-bank-youth-unemployment\\API_ILO_country_YU.csv', index_col=0)
print("We convert the csv file to an html file:")
country.to_html('yael.html')
'''
if we right click on the yael.html file and choose copy path and paste it
to our browser and we would see the table of data.
'''
########%%%%%%%%%#########%%%%%%%%
print("\n ## Concatenation:")
print("Is is basically adding another column or row to a data frame,"
      "or in this case combining the two data frames")
df1 = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int_rate": [2, 1, 2, 3], "IND_GDP": [50, 45, 45, 67]},
                   index=[2001, 2002, 2003, 2004])
df2 = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int_rate": [2, 1, 2, 3], "IND_GDP": [50, 45, 45, 67]},
                   index=[2005, 2006, 2007, 2008])
Concat = pd.concat([df1, df2])
print("This is how you preforme concatenation:\n", Concat)

################################################
print("\n \n## Use case: ##")
'''
above we already imported this, but just to remind you:
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")
'''
country = pd.read_csv('C:\\Users\\Yael\\Downloads\\world-bank-youth-unemployment\\API_ILO_country_YU.csv', index_col=0)
# the index_col=0 , means there will be no index at all
df = country.head(5) #creates a data frame with only the top 5 data rows
df = df.set_index(["Country Code"]) # defining the Country Code to be the index
sd = df.reindex(columns=['2010', '2011']) # redefining the columns to be only 2010 and 2011
print("this is how sd looks like:\n", sd)
db = sd.diff(axis=1) # db is the difference between the 2 columns 2010 and 2011
# basically will gives us the change between 2010 to 2011 of unemployed youth
print("The next graph will show us the different between 2010 to 2011 of"
      "unemployed youth")
db.plot(kind='bar')
plt.show()
################################################
print("\n\n## Python for Statistics: ##")
print("The most useful operations for statistics are:"
      "\n1. Mean - the average of a particular list or sequence"
      "\n2. Mode- the value that was repeated the most"
      "\n3. Median - the middle value-> if we have an even number of elements then we will have High Median and Low Median"
      "\n4. Variance- the variation of each and every element in the sequence from the arithmetic mean ")
from statistics import mean
li = [1, 2, 2, 2, 1, 3, 4, 1, 5]
print("the list is:\n", li)
print("the mean of the list is: ", mean([1, 2, 2, 2, 1, 3, 4, 1, 5]))
# = 2.3333....
from statistics import median
li = [1, 1, 1, 2, 2]
print("the list is:\n", li)
print("the median of the list is: ", median(li))
# = 1
from statistics import mode
li = [1, 1, 1, 2, 2]
print("the list is:\n", li)
print("the median of the list is: ", mode(li))
# = 1
from statistics import variance
li = [1, 1, 2, 2]
print("the list is:\n", li)
print("the median of the list is: ", variance(li))
# = 0.3
