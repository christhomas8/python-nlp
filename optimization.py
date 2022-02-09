import math
#import numpy as np
from mpl_toolkits.mplot3d import Axes3D  
# Axes3D import has side effects, it enables using projection='3d' in add_subplot
import matplotlib.pyplot as plt
import pylab
#from matplotlib import cm


x = [0,0]
maxG = 0
bestX = [0,0]
xx = []
yy = []
zz = []

while (x[1] < 10):  
    
    x[0] = 0
    while (x[0] < 10):
            
        if (x[0]*x[1] >= 0.75) and (x[0]+x[1] <= 15) and (x[0] < 10) and (x[0] > 0) and (x[1] > 0) and (x[1] < 10):
        
            G = abs(((math.cos(x[0]))**4 + (math.cos(x[1])**4) - 2 * (math.cos(x[0])**2) *
                    (math.cos(x[1])**2))/(math.sqrt((1*x[0]**2)+(2*x[1]**2))))
            if G > maxG:
                maxG = G
                bestX = [x[0],x[1]]   
        else:
            G = 0
        
        xx.append(x[0])
        yy.append(x[1])
        zz.append(G)        
        
        x[0] += 0.1
        
    x[1] += 0.1
         
print("Maximum Value:",maxG,'\n',"Corresponding X",bestX)

#3D Plot
fig = pylab.figure()
ax = Axes3D(fig)

ax.plot_trisurf(xx, yy, zz, cmap='jet')

ax.view_init(30, 240)
ax.set_xlabel('X_1')
ax.set_ylabel('X_2')
ax.set_zlabel('G(x)')
plt.show()
