import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


a = [np.random.normal(0, std, 100) for std in range (1, 4)]
plt.boxplot(a, vert=True, patch_artist=False,notch= False)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Boxplot')
plt.show()