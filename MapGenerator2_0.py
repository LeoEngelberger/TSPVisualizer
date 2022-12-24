import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import sqlite3



class Map_Generator():
    def __init__(self):
        plt.figure()
        plt.figure(figsize=(16*5,9*5))
        self.m = Basemap(resolution='h',projection='merc', llcrnrlat=45.73, urcrnrlat=47.9, llcrnrlon=5.85, urcrnrlon=10.58)
        self.m.drawcoastlines()
        self.m.drawcountries(linewidth=8)
        self.m.fillcontinents((0,0.5,0),(0,0,0.3))

        long = 8.539183
        lat = 47.36865
        x, y = self.m(long, lat)
        self.m.scatter(x, y, marker='o', color='r', zorder=2, s=150)

        plt.savefig('map.png', bbox_inches='tight', pad_inches=0)


test = Map_Generator()