import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 4*np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

print(f"X: {x}")
print(f"Y_sin: {y_sin}")
print(f"Y_cos: {y_cos}")

plt.subplot(2, 1, 1)
plt.plot(x,y_sin, 'r--')
plt.xlabel('x (radians)')
plt.ylabel('sin(theta)')
plt.title('Sine Function')

plt.subplot(2, 1, 2)
plt.plot(x,y_cos, 'b--')
plt.xlabel('x (radians)')
plt.ylabel('cos(theta)')
plt.title('Cosine Function')

plt.tight_layout()
plt.show()