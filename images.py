# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:23:22 2018

@author: jbertram
"""

import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=[4,4])
sa=np.linspace(1e-10,1.,10000)
plt.fill_between(sa,sa/(1+0.95*sa),sa/(1-0.95*sa),facecolor='blue',edgecolor='none',label=r'$95\%$ protection')
plt.fill_between(sa,sa/(1+0.5*sa),sa/(1-0.5*sa),facecolor='red',edgecolor='none',label=r'$50\%$ protection')
plt.fill_between(sa,sa/(1+0.1*sa),sa/(1-0.1*sa),facecolor='black',edgecolor='none',label=r'$10\%$ protection')
plt.xlim([0,1])
plt.ylim([0,1])
plt.axes().set_aspect('equal')
ax=plt.gca()
ax.xaxis.set_label_coords(0.5, -0.05)
ax.yaxis.set_label_coords(-0.09,0.5)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_title('Region of stable polymorphism')

#For website
plt.xlabel("Type 1 winter advantage",fontsize=16)
ax.xaxis.set_label_coords(0.5,-0.01)
plt.ylabel("Type 2 summer advantage",fontsize=16)
ax.yaxis.set_label_coords(-0.005,0.5)
ax.legend(loc='lower right',prop={'size':11})

plt.savefig('/home/jbertram/repos/jasonbertram.github.io/images/coex.jpg',bbox_inches='tight')