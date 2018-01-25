from matplotlib import pyplot as plt
import numpy as np

data = {}
data[' mysql'] = [6.1, 6.3, 6.2, 6.1, 5.7, 6.1, 6.3, 6.7, 5.3, 5.5]
data[' redis + db'] = [70.9, 75.6, 84, 90, 58.7, 91.8, 68.4, 96.4, 74.6, 88]

color_dict = {'DB mysql':'white', 'Redis + DB':'white'}
controls = ['DB mysql', 'Redis +DB']

fig, ax = plt.subplots()

boxplot_dict = ax.boxplot(
    [data[x] for x in ['DB mysql', 'Redis +DB']],
    positions = [1, 1.5],
    labels = controls,
    patch_artist = True,
    widths = 0.25)

i=0
for b in boxplot_dict['boxes']:
    lab = ax.get_xticklabels()[i].get_text()
    b.set_facecolor(color_dict[lab])
    i += 1

ax.set_ylim([0,np.max(data['Redis'])+10])
plt.ylabel("Throughput (Requests per second)")
plt.show()
