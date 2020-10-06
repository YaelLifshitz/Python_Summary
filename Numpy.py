'''
This is a summary of Numpy.
I summarized the following video: https://www.youtube.com/watch?v=WGJJIrtnfpk&list=PL9ooVrP1hQOHY-BeYrKHDrHKphsJOyRyu
time stapes: 7:38:23 - 8:09:58
I did this for my myselfe so I can always go back and remember what I have learned.
I encourage everyone to go watch the video, like, subscribe, and show them love in the comment section!
'''

import numpy as np
import time
import sys
# arrays are faster than list, which is why it is better to use numpy
# the next few lines will prove it:

## Memory Space:
S = range(1000)
print("Memory occupied by the list: ")
print(sys.getsizeof(5)*len(S)) # we put 5 but we could have put a different num it wouldn't matter
D = np.arange(1000)
#D.size = space occupaied by a single elment, D/itemsize = the length of the array
# the result gives us the entire memory occupied by the numpy array
print("Memory occupied by the Numpy array: ")
print(D.size*D.itemsize)

## Excute Time:
SIZE = 1000000
#we will define tw0 lists
L1 = range(SIZE)
L2 = range(SIZE)
# we also define two arrays using numpy
A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start = time.time() #this var will help us see which way is faster
# now calculating the space each one take
#in order to calculate the sum we need to use a for loop in lists
result = [(x, y) for x, y in zip(L1, L2)] # this is how you calculate sim in lists
# using numpy is more convenient, you will se in the next result...
print("Time taken to compute the sum of the list: ")
print((time.time()-start)*1000) # this will give us the time taken by our list to compute the sum
start = time.time()
result = A1+A2
print("Time taken to compute the sum of the array: ")
print((time.time()-start)*1000)
# we can see that is takes significantly more time to sum up the list than to sum up the arrays using numpy

####################################################################
# two dimensional array
a = np.array([(1, 2, 3), (2, 3, 4)])
# to know what is the dimension of the array:
print("The dimension of the array is: ")
print(a.ndim) # in this case will print 2
# to find out what is the byte size each element in the array:
print("The byte size of each element in the array is: ")
print(a.itemsize) #in this case will give 4
# to know what is the data type stored in the array:
print("The data type  stored in the array is: ")
print(a.dtype) #in this case will give int32

######################################################################
## Size, Shape ##
a = np.array([1, 2, 3])
# to know how many elements are in the array:
print("The amount of elements in the array:")
print(a.size) # this case will print 3
# to know the shape of the array:
print("The shape of the array is:")
print(a.shape) # this case will print (3, ) because there is no rows only columns
a = np.array([(1, 2, 3, 4, 5, 6, 7), (8, 9, 10, 11, 12, 13, 14)])
print(a.shape) # this case will print (2, 7)
########################################################################
## Numpy Operations: ##
## Reshape ##
# reshape = changing the num of rows to num of columns and vise versa.
# but the cloumns dont turn into rows- see next what is the result
a = np.array([(1, 2, 3, 4), (3, 4, 5, 6)])
print("array a before reshape: ")
print(a)
'''
this case will print
 [[1 2 3 4]
    [3 4 5 6]]
'''
a = a.reshape(4,2)
print("array a after reshape: ")
print(a)
'''
this case will print
 [[1 2]
    [3 4]
    [3 4]
    [5 6]]
'''

## How to access an element\s in the array ##
a = np.array([(1, 2, 3, 4), (3, 4, 5, 6)])
#the first element in the array will be 0 and the secound will be one
print(a[0,2]) # will print 3
# 0: means all the rows, that includes 0 as well
# will print the 3 index from both of the rows
print(a[0:, 3]) #in this case we get [4 6]
# since the 3 element in the first row is 4
# and the third element in the secound row is 6
a = np.array([(1, 2, 3, 4), (3, 4, 5, 6), (7, 8, 9, 10)])
# we can't do print(a[0:, 3]) and get the same result as above in this case
print(a[0:, 3]) #the result of this will be [4 6 10]
#instead we can write:
print(a[0:2, 3]) #in this case we get [4 6]
#this will not include the third row

## Line space = equally spares values from an array ##
# will give 5 values which are equally spares between 1 to 3
a = np.linspace(1, 3, 5) # this will give [1. 1.5 2. 2.5 3.]
print(a)

## Min ##
a = np.array([1, 2, 3])
print(a.min()) # = 1

## Max ##
a = np.array([1, 2, 3])
print(a.max()) # = 3

## Sum ##
a = np.array([1, 2, 3])
print(a.sum()) # = 6

## Sum of Axis ##
a = np.array([(1, 2, 3), (3, 4, 5)])
print(a.sum(axis = 0)) # will print [4 6 8] , because 1+3=4, 2+4=6, 3+5=8
print(a.sum(axis = 1)) # will print [6 12] ,because 1+2+3=6, 3+4+5=12

## Squre root ##
print("Squre root: ")
a = np.array([(1, 2, 3), (3, 4, 5)])
print(np.sqrt(a)) # will give the square root of each element in the array

## Standard Deviation ##
print("Standard Deviation: ")
a = np.array([(1, 2, 3), (3, 4, 5)])
print(np.std(a)) # standard deviation of the array
# The Standard Deviation is a measure of how spread out numbers are.
# Its symbol is σ (the greek letter sigma)

## Matrices Addition (element wise) ##
print("Matrices Addition (element wise): ")
a = np.array([(1, 2, 3), (3, 4, 5)])
b = np.array([(1, 2, 3), (3, 4, 5)])
print(a+b)

## Matrices Subtraction (element wise) ##
print("Matrices Subtraction (element wise): ")
a = np.array([(1, 2, 3), (3, 4, 5)])
b = np.array([(1, 2, 3), (3, 4, 5)])
print(a-b)

## Matrices Multiplication (element wise) ##
print("Matrices Multiplication (element wise): ")
a = np.array([(1, 2, 3), (3, 4, 5)])
b = np.array([(1, 2, 3), (3, 4, 5)])
print(a*b)

## Matrices Diviation (element wise) ##
print("Matrices Diviation (element wise): ")
a = np.array([(1, 2, 3), (3, 4, 5)])
b = np.array([(1, 2, 3), (3, 4, 5)])
print(a/b)

## Matrices Stacking - Vertical Stacking ##
print("Vertical Stacking: ")
print(np.vstack((a, b)))
print()
## Matrices Stacking - Horizontal Stacking ##
print("Horizontal Stacking: ")
print(np.hstack((a, b)))

## Turn a Matrix to a single column ##
print("Turn a Matrix to a single column: ")
a = np.array([(1, 2, 3), (3, 4, 5)])
print(a.ravel()) # this will print [1 2 3 3 4 5]

########################################################################
# the next special functions require matplotlib library
import matplotlib.pyplot as plt
## Sine Function ##
print("A Sin graph will appear: ")
x = np.arange(0, 3*np.pi, 0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()

## Cosine Function ##
print("A Cos graph will appear: ")
x = np.arange(0, 3*np.pi, 0.1)
y = np.cos(x)
plt.plot(x,y)
plt.show()

## Tan Function ##
print("A Tan graph will appear: ")
x = np.arange(0, 3*np.pi, 0.1)
y = np.tan(x)
plt.plot(x,y)
plt.show()

## Exponential Function ##
ar = np.array([1, 2, 3])
print(np.exp(ar)) # will return the value element wise

## Logarithmic Function ##
ar = np.array([1, 2, 3])
print(np.log(ar)) #calculate the natural log which is basically ln
#ln = log base e
print(np.log10(ar)) # log base 10
