#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 15:13:15 2025

@author: nikolamaksimovic
"""

import os
import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import Divider, Size
from matplotlib.cm import ScalarMappable
from matplotlib.colorbar import ColorbarBase
from matplotlib.colors import LinearSegmentedColormap
from mpl_toolkits.axes_grid1 import make_axes_locatable

currentDirectory = os.getcwd()
font = {'family' : 'Helvetica',
        'weight' : 'normal',
        'size'   : 8}
matplotlib.rc('font', **font)


# Read the CSV data as a 2D NumPy array
data = np.loadtxt('250910-14_47_49_galvoscan_Nikola/raw_data/250910-14_47_49_galvoscan_Nikola-image_data.csv', delimiter=',')

fig = plt.figure(figsize=(6, 6))
# The first items are for padding and the second items are for the axes.
# sizes are in inch.
h = [Size.Fixed(0.5), Size.Fixed(2)]
v = [Size.Fixed(0.5), Size.Fixed(2)]
divider = Divider(fig, (0, 0, 1, 1), h, v, aspect=False)
ax = fig.add_axes(divider.get_position(),
                  axes_locator=divider.new_locator(nx=1, ny=1))

# Plot the 2D array as a color plot (heatmap)
plt.imshow(data, cmap='Blues', aspect='auto')
plt.clim([0,250])


# Save the figure as PDF and PNG BEFORE plt.show()
plt.setp(ax.spines.values(), linewidth=0.6)
plt.savefig("NVs_galvo.pdf",format="pdf", bbox_inches="tight")
plt.savefig("NVs_galvo.png",format="png", dpi=300,bbox_inches="tight")


plt.show()


