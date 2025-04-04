import pandas as pd

# Create the DataFrame
students = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'first': ['Mason', 'Ava', 'Taylor', 'Georgia', 'Thomas'],
    'last': ['King', 'Wright', 'Hall', 'Thompson', 'Moore'],
    'age': [6, 7, 16, 18, 10]
})
# print(students.rename(columns = {'id': 'student_id','first': 'first_name','last': 'last_name','age': 'age_in_years'}))
print(students.set_axis(['student_id', 'first_name', 'last_name', 'age_in_years'], axis =1))