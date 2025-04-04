import pandas as pd

# Create the DataFrame
students = pd.DataFrame({
    'student_id': [1, 2],
    'name': ['Ava', 'Kate'],
    'age': [6, 15],
    'grade': [73.0, 87.0]  # grade is currently float
})

# Convert the 'grade' column to integers
# students['grade'] = students['grade'].astype(int)

# Display the updated DataFrame
students['grade'] = pd.to_numeric(students['grade'], downcast = 'integer')
# print(students.astype({'grade':int}))
print(students)
