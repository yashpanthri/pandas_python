import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

students = pd.DataFrame({
    'student_id': [101, 53, 128, 3],
    'name': ['Ulysses', 'William', 'Henry', 'Henry'],
    'age': [13, 10, 6, 11]
})

print(students.loc[students["student_id"] == 101, ["name", "age"]])