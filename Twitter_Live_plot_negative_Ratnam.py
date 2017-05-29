# -*- coding: utf-8 -*-
"""
Created on Mon May 29 17:07:03 2017

@author: dubey
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May 29 15:58:41 2017

@author: dubey
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from wordcloud import WordCloud,STOPWORDS

style.use("ggplot")

fig = plt.figure()


def animate(i):
    pullData = open("D:\\negative.txt","r").read()
    wordcloud = WordCloud(stopwords=STOPWORDS,background_color='black',width=3000, height=2500).generate(pullData)

    plt.figure(1,figsize=(12, 12))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
    
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()