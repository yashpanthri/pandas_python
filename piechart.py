import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

labels = np.array(['Python', 'Java', 'C++', 'Ruby']) # doesnt matter if its a list or numpy array or tuple
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

plt.pie(sizes, explode = explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow = True)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Pie Chart')
plt.show()
