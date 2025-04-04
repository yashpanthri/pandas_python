import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


student_data=[[1, 15],[2, 11],[3, 11],[4, 20]]
employees = pd.DataFrame(np.array(student_data ),
                        columns=['Employee ID', 'Age'])
print(employees.head(3))
array = employees.to_numpy()

print(array)
plt.scatter(employees['Employee ID'], employees['Age'], c = 'r')
plt.title('Employee ID vs Age')
plt.xlabel('Employee ID') # Add label to the X-axis
plt.ylabel('Age')  # Add label to the Y-axis
plt.show()
