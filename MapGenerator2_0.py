import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import sqlite3



class Map_Generator():
    def __init__(self, lef_border, rig_border, top_border, bot_border):
        plt.figure()
        plt.figure(figsize=(16*5,9*5))
        self.m = Basemap(resolution='h',projection='merc', llcrnrlat=lef_border, urcrnrlat=rig_border, llcrnrlon=top_border, urcrnrlon=bot_border)
        self.m.drawcoastlines()
        self.m.drawcountries(linewidth=7)
        self.m.fillcontinents((0,0.5,0),(0,0,0.3))
        self.m.drawmeridians(np.arange(40, 60, 0.5),linewidth=5)
        self.m.drawparallels(np.arange(0, 20, 1),linewidth=5)
        plt.savefig('map.png', bbox_inches='tight', pad_inches=0)


test = Map_Generator(45.73,47.9,5.85,10.58)