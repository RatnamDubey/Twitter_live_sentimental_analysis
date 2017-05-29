# -*- coding: utf-8 -*-
"""
Created on Mon May 29 15:58:41 2017

@author: dubey
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("D:\\twitter-out.txt","r").read()
    print(pullData)
    lines = pullData.split('\n')

    xar = []
    yar = []

    x = 0
    y = 0

    for l in lines[-200:]:
        x += 1
        if "positive" in l:
            y += 1
        elif "negative" in l:
            y -= 1


        xar.append(x)
        yar.append(y)
        
    ax1.clear()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()