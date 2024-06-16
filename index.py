#!/usr/bin/python3

#This is a 3D plot figure

#import resources to use
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#Create a figure and a 3D Axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#Generate data for plotting
x = np.linspace(-5,5,100)
y = np.linspace(-5,5,100)
x,y = np.meshgrid(x,y)
z = np.sin(np.sqrt(x**2 + y**2))

#Plot the surface
ax.plot_surface(x,y,z, color='red', cmap='viridis')

#Set labels
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

#Display the plot
plt.show()
