import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# x1 = np.array([2, 4, 5])
# y1 = np.array([10, 15, 5])
x1 = [2, 4, 5]
y1 = [10, 15, 5]
x2 = np.array([10, 12, 14])
y2 = np.array([8, 6, 10])
# plt.bar(x1,y1, color='b')
# plt.bar(x2,y2, color='r')
plt.bar(x1,y1, color='b', label='Bar Type 1')
plt.bar(x2,y2, color='r', label='Bar Type 2')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bar Plot Example')
plt.legend()
plt.show()