import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 20, 2)
y = x**2
print(f"X: {x}")
print(f"Y: {y}")
# plt.xlabel('x-values')
# plt.ylabel('y=x\u00B2-values')
plt.subplot(2, 2, 1)
plt.scatter(x, y, c='b')
plt.title('Scatter plot')
plt.xlabel('x-values')
plt.ylabel('y=x\u00B2-values')


plt.subplot(2, 2, 2)
plt.plot(x, y, 'r:')
plt.title('Line plot')
plt.xlabel('x-values')
plt.ylabel('y=x\u00B2-values')


plt.subplot(2, 2, 3)
plt.plot(x, y, 'r*--')
plt.title('Line with markers')
plt.xlabel('x-values')
plt.ylabel('y=x\u00B2-values')


plt.subplot(2, 2, 4)
plt.plot(x, y, 'r--')
plt.title('Dashed line')
plt.xlabel('x-values')
plt.ylabel('y=x\u00B2-values')

plt.show()