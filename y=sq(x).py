import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 20, 2)
y = x**2
print(f"X: {x}")
print(f"Y: {y}")
plt.xlabel('x-values')
plt.ylabel('y=x\u00B2-values')
# plt.plot(x,y, 'ro')
plt.scatter(x,y, c = 'b')
# plt.plot(x,y, 'r*')
# plt.plot(x,y, 'r*-')
# plt.plot(x,y, 'r--')
plt.plot(x,y, 'r:')
# plt.plot(x,y, 'r*--')
plt.show()