import pandas as pd

# Create the DataFrame
students = pd.DataFrame({
    'student_id': [32, 217, 779, 849],
    'name': ['Piper', None, 'Georgia', 'Willow'],
    'age': [5, 19, 20, 14]
})

# Remove rows where 'name' column has missing values
students = students.dropna(subset=['name'])

# Display the result
print(students)