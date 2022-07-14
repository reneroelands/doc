# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 09:44:54 2019

@author: r.roelands
"""
from scipy.stats import norm

import numpy as np

import matplotlib.pyplot as plt

mu = 148.0
sigma = 9.5
x1 = 112
x2 = 192
xmin = 100
xmax= 200

x = np.arange(xmin, xmax, 0.001) 
y_flex = norm.pdf(x, mu, sigma)

mu_tool = x1
sigma_tool = 5.0/3

x = np.arange(xmin, xmax, 0.001) 
y = norm.pdf(x, mu, sigma)
y_tool = norm.pdf(x, mu_tool, sigma_tool)

# build the plot
fig, ax = plt.subplots(figsize=(9,6))
#plt.style.use('fivethirtyeight')
ax.plot(x, y*(1.0/y.max()), 'b')
ax.plot(x, y_tool,'k')
ax.plot(x+80, y_tool,'k')

plt.plot([x1,x1],[0,1.5],'r:')
plt.plot([x2,x2],[0,1.5],'r:')
plt.plot([x1-3*sigma_tool, x1-3*sigma_tool],[0,1.5],'k:')
plt.plot([x1+3*sigma_tool, x1+3*sigma_tool],[0,1.5],'k:')
plt.plot([mu-3*sigma, mu-3*sigma],[0,1.5],'b:')
plt.plot([mu+3*sigma, mu+3*sigma],[0,1.5],'b:')
plt.plot([mu, mu],[0,1.5],'b--')

plt.xlim((xmin,xmax))
plt.ylim((0,1.2))
plt.yticks([])
locs, labels = plt.xticks([x1, x1+3*sigma_tool, mu-3*sigma, mu, mu+3*sigma, x2-3*sigma_tool, x2], 
                              ('lower limit', 'meas.', 'lower process', 'nominal', 'upper process', 'meas.', 'upper limit'))
plt.setp(labels, rotation=45)
plt.xlabel('Flexure Force [N]')
plt.ylabel('distribution')
plt.show()
