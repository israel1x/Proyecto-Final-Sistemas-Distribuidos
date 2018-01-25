from matplotlib import pyplot as plt
import numpy as np

data = {}
data['Just DB'] = [24524, 24333, 24409, 23355, 24459, 24417, 25937, 25511, 25130, 24143]
data['Redis +DB'] = [3432, 3354, 2027, 4888, 6872, 764, 3790, 1413, 1825, 2383]

color_dict = {'Just DB':'white', 'Redis +DB':'white'}
controls = ['Just DB', 'Redis +DB']

fig, ax = plt.subplots()

boxplot_dict = ax.boxplot(
    [data[x] for x in ['Just DB', 'Redis +DB']],
    positions = [1, 1.5],
    labels = controls,
    patch_artist = True,
    widths = 0.25)

i=0
for b in boxplot_dict['boxes']:
    lab = ax.get_xticklabels()[i].get_text()
    b.set_facecolor(color_dict[lab])
    i += 1

ax.set_ylim([0,np.max(data['mysql db'])+500])
plt.ylabel("Average latency (Miliseconds)")
plt.show()
