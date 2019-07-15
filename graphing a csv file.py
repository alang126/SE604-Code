import matplotlib.pyplot as plt
import numpy as np
#import csv

datafile=input('Input the datafile name please:  ')
#print(datafile)
#Name the Axis
plt.xlabel('Position in Inches')
plt.ylabel('Load in lbs')
#Choose the graph title from the file name the user enters
plt.title(datafile)

b = np.genfromtxt(datafile, delimiter=',')
#Print the array data, size, shape and maximum value

print(b)
print(b.size)
print(b.shape)
print(b.max())
xmax =np.max(b[:,0])
ymax=np.max(b[:,1])
print(xmax, "-", ymax)
#set the min and max values on the graph axis

plt.ylim(0,ymax)
plt.xlim(0,xmax)

#plot the data in the file
plt.plot(np.asarray(b))

#plt.xticks()
plt.show()
