import pandas as pd

# Create the DataFrame
employees = pd.DataFrame({
    'name': ['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'],
    'salary': [4548, 28150, 1103, 6593, 74576, 24433]
})

# employees['bonus'] = employees['salary'] * 2
# # employees['bonus'] = pd.Series([1,2,3,4,5,6])

# print(type(employees['bonus']))
# print(employees)
employees = employees.assign(bonus=employees["salary"] * 2)
print(employees['bonus'])