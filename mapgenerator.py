import pygame
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import sqlite3

# Create a new figure
plt.figure()

# Set the dimensions of the figure
plt.figure(figsize=(10, 10))

# Set the map projection.
# You can choose from a variety of map projections.
# Some examples include: 'aeqd', 'moll', 'robin', 'merc'
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)

# Draw the coastlines
m.drawcoastlines()

# Draw country boundaries
m.drawcountries()

# Draw lat/lon grid lines every 30 degrees.
m.drawmeridians(range(-180, 180, 1))
m.drawparallels(range(-90, 90, 1))


plt.autoscale()
# Save the map as an image file
plt.savefig('map.png',bbox_inches='tight')

