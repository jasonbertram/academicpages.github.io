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

#====================================================================================================

x,y=np.linspace(0,1,1000),np.linspace(0,1,1000)
X, Y = np.meshgrid(x,y)
alphas=np.array([[1,1],[1.5,1.5]])
U = (1-alphas[0,0]*X-alphas[0,1]*Y)*X
V = (1-alphas[1,1]*Y-alphas[1,0]*X)*Y
#speed = np.sqrt(U*U + V*V)

plt.figure(figsize=[4,4])
ax=plt.gca()
ax.set_aspect(1)
plt.tight_layout()
seedpoints=np.concatenate([[[_,0.2-_] for _ in np.arange(0.02,0.2,0.02)],\
            [[float(_)/10,1.-_*0.1] for _ in range(0,11) if _ not in [1,7]]])
ax.streamplot(x, y, U, V,density=100,start_points=seedpoints,linewidth=1.)

z1=np.linspace(0,1,10)
z2=1-z1
ax.plot(z1,(1-alphas[0,0]*z1)/alphas[0,1],'k--',linewidth=2)
ax.plot(z1,(1-alphas[1,0]*z1)/alphas[1,1],'k--',linewidth=2)
#ax1.plot([0,1/alphas[0,0]],[1/alphas[1,1],0],'y',linewidth=2)
ax.set_xlim([0,1])
ax.set_ylim([0,1])

ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_xlabel("Type 1 density",fontsize=20)
ax.set_ylabel("Type 2 density",fontsize=20)

plt.savefig('/home/jbertram/repos/jasonbertram.github.io/images/Kplot.jpg',bbox="tight")