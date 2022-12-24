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
m.drawmeridians(range(-180, 180, 30))
m.drawparallels(range(-90, 90, 30))

# Set the real-world coordinates of the location you want to plot
lat = 47.36
lon = 8.539

# Convert the lat/lon coordinates to map projection coordinates
x, y = m(lon, lat)

# Plot the location on the map
m.plot(x, y, 'ro', markersize=10)

plt.autoscale()
# Save the map as an image file
plt.savefig('map.png',bbox_inches='tight')

